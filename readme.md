### Installing Virtual Environment

```bash
python -m venv fastapi-venv
```

### Activate the Environment

```bash
source fastapi-venv/bin/activate
```

### Install dependences

```bash
pip install -r requiredments.txt
```

### Running Migrations 

```bash
alembic upgrade head
```

### Downgrading Migrations 

```bash
alembic downgrade revision_id
```

### Install pre-commit hooks

```bash
pip install pre-commit
pre-commit install
```

### Starting the Server

```bash
uvicorn app.main:app --reload --port 8000
```

### Creating Migration 

```bash
alembic revision --autogenerate -m "Message"
```
