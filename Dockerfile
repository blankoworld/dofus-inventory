FROM alpine:3.4

MAINTAINER Olivier DOSSMANN, dockerfile@dossmann.net

ENV APP_DIR /opt/dmap
ENV DB_DIR /opt/database
ENV STATIC_ROOT $APP_DIR/static

COPY . $APP_DIR

WORKDIR $APP_DIR

RUN mkdir -p $APP_DIR/static $DB_DIR

RUN apk --no-cache --update add \
        build-base \
        linux-headers \
        mailcap \
        py-configobj \
        python3 \
        python3-dev && \
    python3 -m ensurepip && \
    pip3 install --upgrade pip && \
    pip install --no-cache-dir --upgrade -r requirements.txt && \
    python3 manage.py collectstatic --noinput --clear -v 1 && \
    chown -R guest:users $APP_DIR && \
    chmod -R 550 $APP_DIR && \
    apk del \
        build-base \
        linux-headers \
        python3-dev && \
    rm -rf /var/cache/apk/*

VOLUME $DB_DIR

ENTRYPOINT ["./docker-entrypoint.sh"]

EXPOSE 8000
CMD ["production"]
