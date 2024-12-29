FROM python:3.13

ENV APP_USER="portfolio" \
    APP_DIR="/src"
ARG UID=1000
ARG GID=1000
RUN (groupadd -g ${GID} -r ${APP_USER} \
    || groupmod --new-name ${APP_USER} `getent group ${GID} | cut --delimiter=: -f1`) \
    && useradd -u ${UID} -r -m \
    -g ${APP_USER} ${APP_USER} \
    -s /usr/sbin/nologin \
    --home-dir ${APP_DIR}

COPY . /src

RUN pip install -r /src/requirements.txt

COPY --chown=${APP_USER}:${APP_USER} . /code
USER ${APP_USER}
WORKDIR /src

ENTRYPOINT ["python", "manage.py"]