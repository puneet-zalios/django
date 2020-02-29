FROM python:3.8-slim

WORKDIR /app

ARG UID
ARG GID
ARG USER="fusion"
RUN test -n "$UID"
RUN test -n "$GID"

COPY ./fusion/requirements.txt /app

RUN apt-get update && \
    apt-get install -y gcc wget unzip libaio1 && \
    groupadd -g $GID -r $USER \
    && useradd -u $UID -r -g $USER $USER \
    && pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir --no-use-pep517 -r requirements.txt \
    && chown -R $USER:$USER /var/run/ \
    && wget -O /usr/bin/dumb-init https://github.com/Yelp/dumb-init/releases/download/v1.2.2/dumb-init_1.2.2_amd64 \
    && mkdir -p /opt/oracle \
    && wget -O /opt/oracle/instantclient-basic.zip https://download.oracle.com/otn_software/linux/instantclient/19600/instantclient-basic-linux.x64-19.6.0.0.0dbru.zip \
    && cd /opt/oracle/ \
    && unzip instantclient-basic.zip \
    && sh -c "echo /opt/oracle/instantclient_19_6 > /etc/ld.so.conf.d/oracle-instantclient.conf" \
    && ldconfig \
    && chmod +x /usr/bin/dumb-init

RUN chown $USER:$USER .
USER $USER

COPY --chown=$USER:$USER . /app

ENTRYPOINT ["/usr/bin/dumb-init", "--"]
