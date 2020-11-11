FROM python:3.6-alpine

WORKDIR /app

ARG UID
ARG GID
ARG USER="fusion"
RUN test -n "$UID"
RUN test -n "$GID"

RUN apk --no-cache add shadow \
    gcc \
    musl-dev \
    autoconf \
    automake \
    make \
    libtool \
    nasm \
    libnsl \
    libaio \
    postgresql-dev \
    python3-dev \
    freetype-dev \
    libffi-dev \
    tiff \
    tiff-dev \
    tk-dev \
    tcl-dev \
    postgresql \
    postgresql-dev \
    jpeg \
    jpeg-dev \
    zlib \
    zlib-dev \
    nodejs \
    yarn \
    libmemcached \
    libmemcached-dev \
    && addgroup -g $GID -S $USER \
    && adduser -u $UID -S -G $USER $USER

COPY ./fusion/requirements.txt /app

RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir --no-use-pep517 -r requirements.txt \
    #&& apk del \
    #    tiff-dev \
    #    tcl-dev \
    #    jpeg-dev \
    #    zlib-dev \
    #    postgresql-dev \
    #    libmemcached-dev \
    && rm -rf /var/cache/apk/* \
    && chown -R $USER:$USER /var/run/ \
    && wget -O /usr/bin/dumb-init https://github.com/Yelp/dumb-init/releases/download/v1.2.2/dumb-init_1.2.2_amd64 \
    && chmod +x /usr/bin/dumb-init

ADD ./instantclient_19_6/ /usr/local/lib/
RUN ln -s /usr/lib/libnsl.so.2 /usr/lib/libnsl.so.1
RUN ln -s /lib/ld-musl-x86_64.so.1  /usr/lib/libresolv.so.2
RUN ln -s /lib/ld-musl-x86_64.so.1 /lib/ld-linux-x86-64.so.2
RUN chown $USER:$USER .
USER $USER

COPY --chown=$USER:$USER . /app

ENTRYPOINT ["/usr/bin/dumb-init", "--"]
