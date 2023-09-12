
# Install

```bash
python3 -m virtualenv ./venv
source ./venv/bin/activate
pip install -r requirements.txt
pip install -r requirements-dev.txt
pip install -r ./src/cli/requirements.txt
```

# Docker

```bash
docker-compose up -d db pgadmin
```

# Run API

```bash
python3 -m uvicorn src.api.api:app --reload --port 8002 --host 0.0.0.0 --forwarded-allow-ips '*'
```

# Alembic

## alembic generate migration

DATABASE_HOST="localhost" alembic revision -m "add: user table"

## alembic migrate

DATABASE_HOST="localhost" alembic upgrade head

# CLI 

## run cli command 

DATABASE_HOST="localhost" python3 -m src.cli hello-world command

# Linting

```bash
black src tests
flake8 src tests
```