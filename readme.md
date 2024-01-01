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

### Starting the Server

```bash
uvicorn app.main:app --reload --port 8000
```
