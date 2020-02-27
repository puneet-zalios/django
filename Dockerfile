FROM python:3.8-slim

WORKDIR /app

ARG UID
ARG GID
ARG USER="fusion"
RUN test -n "$UID"
RUN test -n "$GID"

COPY ./fusion/requirements.txt /app

RUN apt-get update && \
    apt-get install -y gcc wget && \
    groupadd -g $GID -r $USER \
    && useradd -u $UID -r -g $USER $USER \
    && pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir --no-use-pep517 -r requirements.txt \
    && chown -R $USER:$USER /var/run/ \
    && wget -O /usr/bin/dumb-init https://github.com/Yelp/dumb-init/releases/download/v1.2.2/dumb-init_1.2.2_amd64 \
    && chmod +x /usr/bin/dumb-init

RUN chown $USER:$USER .
USER $USER

COPY --chown=$USER:$USER . /app

ENTRYPOINT ["/usr/bin/dumb-init", "--"]
