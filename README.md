# A Fast API Template

## Commands

### Create a Virtual Environment¶

```
python -m venv .venv
```

### Activate the Virtual Environment

```
.venv\Scripts\Activate.ps1
```

### Install Packages

```
pip install -r requirements.txt
```

### Run FastAPI Dev Server

```
fastapi dev app/main.py --port 8080
```

### .env example (place it in `app/`)

```
DATABASE_URL=postgresql://postgres:password@localhost:5430/template
POSTGRES_USER=postgres
POSTGRES_PASSWORD=password
POSTGRES_DB=template
SECRET_KEY=adsfghjklqwertyuiopzxcvbnm1234567890
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```
