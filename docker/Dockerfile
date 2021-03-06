# Dockerfile
# Uses multi-stage builds requiring Docker 17.05 or higher
# See https://docs.docker.com/develop/develop-images/multistage-build/

# Creating a python base with shared environment variables
FROM python:3.10.1-slim-buster as python-base

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    POETRY_HOME="/opt/poetry" \
    POETRY_VIRTUALENVS_IN_PROJECT=true \
    POETRY_NO_INTERACTION=1 \
    PYSETUP_PATH="/opt/pysetup" \
    VENV_PATH="/opt/pysetup/.venv"

ENV PATH="$POETRY_HOME/bin:$VENV_PATH/bin:$PATH"


# builder-base is used to build dependencies
FROM python-base as builder-base
RUN apt-get update \
    && apt-get install --no-install-recommends -y \
        curl \
        build-essential \ 
        libatlas-base-dev gfortran nginx supervisor \
        apt-utils


# Install Poetry - respects $POETRY_VERSION & $POETRY_HOME
ENV POETRY_VERSION=1.1.13
RUN curl -sSL https://raw.githubusercontent.com/sdispater/poetry/master/get-poetry.py | python3

# We copy our Python requirements here to cache them
# and install only runtime deps using poetry
WORKDIR $PYSETUP_PATH
COPY ./poetry.lock ./pyproject.toml ./
RUN poetry lock --no-update
RUN poetry install --no-dev  

RUN useradd --no-create-home nginx 
RUN rm /etc/nginx/sites-enabled/default
RUN rm -r /root/.cache

COPY ./server-config/nginx.conf /etc/nginx/
COPY ./server-config/flask-nginx.conf /etc/nginx/conf.d/
COPY ./server-config/uwsqi.ini /etc/uwsgi/
COPY ./server-config/supervisord.conf /etc/

CMD ["/usr/bin/supervisord"]

### DEVELOPMENT ###
###################

# 'development' stage installs all dev deps and can be used to develop code.
# For example using docker-compose to mount local volume under /app
FROM python-base as development
ENV FLASKAPI_ENV = development
ENV FLASK_APP=main

# Copying poetry and venv into image
COPY --from=builder-base $POETRY_HOME $POETRY_HOME
COPY --from=builder-base $PYSETUP_PATH $PYSETUP_PATH

# Copying in our entrypoint
COPY ./docker/docker-entrypoint.sh /docker-entrypoint.sh
RUN chmod +x /docker-entrypoint.sh

# venv already has runtime deps installed we get a quicker install
WORKDIR $PYSETUP_PATH
RUN poetry install

WORKDIR /app
COPY . .

ENV FLASK_APP=main
EXPOSE 8080
ENTRYPOINT /docker-entrypoint.sh $0 $@
CMD ["flask", "run", "--host=0.0.0.0", "--port=8080"]
# CMD ["main.py"]
# CMD ["uwsgi", "--reload", "--host=0.0.0.0", "--port=8000", "main:app"]


# 'lint' stage runs black and isort
# running in check mode means build will fail if any linting errors occur
FROM development AS lint
RUN black --config ./pyproject.toml --check app tests
RUN isort --settings-path ./pyproject.toml . --diff
CMD ["tail", "-f", "/dev/null"]


# 'test' stage runs our unit tests with pytest and
# coverage.  Build will fail if test coverage is under 95%
FROM development AS test
RUN coverage run --rcfile ./pyproject.toml -m pytest ./tests
RUN coverage report --fail-under 40

###### PRODUCTION #####
#######################

# 'production' stage uses the clean 'python-base' stage and copyies
# in only our runtime deps that were installed in the 'builder-base'
FROM python-base as production
ENV FLASKAPI_ENV=production
ENV FLASK_APP=main

COPY --from=builder-base $VENV_PATH $VENV_PATH
# COPY ./docker/gunicorn_conf.py /gunicorn_conf.py

COPY ./docker/docker-entrypoint.sh /docker-entrypoint.sh
RUN chmod +x /docker-entrypoint.sh

COPY ./app /app
WORKDIR /app

ENTRYPOINT /docker-entrypoint.sh $0 $@
CMD ["flask", "run", "--host=0.0.0.0", "--port=8080"]]
# CMD [ "gunicorn", "--worker-class uvicorn.workers.UvicornWorker", "--config /gunicorn_conf.py", "main:app"]

