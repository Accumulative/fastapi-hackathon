FROM python:3.10.10-slim as base
ENV PYTHONUNBUFFERED 0

RUN apt-get update \
  && apt-get -y install libpq-dev gcc g++

# graphviz used for eralchemy2

WORKDIR /app

FROM base as build-phase

COPY requirements.txt .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

FROM build-phase as execution-phase

COPY src/api src/api
COPY alembic alembic/
COPY alembic.ini .

FROM execution-phase as development-api

CMD python -m uvicorn src.api.api:app --reload --port $PORT --host 0.0.0.0 --forwarded-allow-ips '*'

FROM execution-phase as production-api

CMD hypercorn src.api.api:app --worker-class asyncio --bind 0.0.0.0:$PORT
