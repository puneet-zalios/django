FROM python:3.6-alpine

WORKDIR /app

ARG UID
ARG GID
ARG USER="fusion"
RUN test -n "$UID"
RUN test -n "$GID"

COPY ./fusion/requirements.txt /app

RUN apk --no-cache add shadow \
    gcc \
    musl-dev \
    autoconf \
    automake \
    make \
    libtool \
    nasm \
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

RUN chown $USER:$USER .
USER $USER

COPY --chown=$USER:$USER . /app

ENTRYPOINT ["/usr/bin/dumb-init", "--"]
