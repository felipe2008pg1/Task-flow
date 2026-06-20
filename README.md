# TaskFlow 🚀

A complete task management system developed with FastAPI, MySQL, and pure JavaScript.

## Features

- User registration
- Task creation
- Status update
- Deleting tasks
- Custom Categories
- Statistics per user
- API REST documented with Swagger
- Integration between frontend and backend

---

## Project Estruture

```text
taskflow/
│
├── backend/
│   ├── .env
│   ├── .env.example
│   ├── crud.py            # Opera CRUD
│   ├── database.py        # Conexion with MySQL
│   ├── main.py            # Aplicattion FastAPI
│   ├── models.py          # SQLAlchemy Models
│   ├── requirements.txt   # Dependences
│   ├── schemas.py         # Schemas Pydantic
│   └── test_db.py         # Database connection test
│
├── database/
│   └── schema.sql         # Database creation script
│
├── frontend/
│   ├── app.js             # Interface logic
│   └── index.html         # Interface web
│
├── .gitignore
├── README.md
└── play.py                # Auxiliary file for testing
```

---

## Database connection test

| Camada | Technology |
|---------|-----------|
| Backend | FastAPI |
| ORM | SQLAlchemy 2.0 |
| Validation | Pydantic |
| DataBase | MySQL 8 |
| Driver | PyMySQL |
| Frontend | HTML5, CSS3 and JavaScript |
| API Docs | Swagger UI |

---

## Pre-requisites

- Python 3.11+
- MySQL 8+
- Git

---

## Database Configuration

Come in MySQL:

```bash
mysql -u root -p
```

Execute the script:

```bash
source database/schema.sql
```

Or:

```bash
mysql -u root -p < database/schema.sql
```

---

## Backend Configuration

Come in folder for backend:

```bash
cd backend
```

Create the virtual environment:

```bash
python -m venv .venv
```

Active the environment:

### Windows

```bash
.venv\Scripts\activate
```

### Linux/Mac

```bash
source .venv/bin/activate
```

Install the dependences:

```bash
pip install -r requirements.txt
```

Copy the file exemple:

```bash
cp .env.example .env
```

Config the database credentials:

```env
DB_HOST=localhost
DB_PORT=3306
DB_NAME=taskflow
DB_USER=root
DB_PASSWORD=sua_senha
```

---

## Testing the Conection with the Database

```bash
python test_db.py
```

---

## Executing the API

```bash
uvicorn main:app --reload
```

Acess:

- API: http://localhost:8000
- Swagger: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

---

## Executing the Frontend

Open directly the file:

```bash
frontend/index.html
```

Or using a server local:

```bash
cd frontend
python -m http.server 3000
```

Acess:

```text
http://localhost:3000
```

---

## Endpoints Available

| Method | Endpoint | Description |
|----------|----------|----------|
| GET | / | Health Check |
| GET | /users | User list |
| POST | /users | Create user |
| GET | /users/{id}/tasks | List Tasks |
| POST | /tasks | Create Tasks |
| PATCH | /tasks/{id} | Update Taks |
| DELETE | /tasks/{id} | Delete Taks |
| GET | /users/{id}/stats | Statistics |
| GET | /users/{id}/categories | Categories |
| POST | /categories | Create categorie |
| DELETE | /categories/{id} | Delete categorie |

---

## Requisition exemple

Crate Task:

```bash
curl -X POST http://localhost:8000/tasks \
-H "Content-Type: application/json" \
-d '{"title":"My Task","priority":"high","user_id":1}'
```

Update status:

```bash
curl -X PATCH http://localhost:8000/tasks/1 \
-H "Content-Type: application/json" \
-d '{"status":"done"}'
```

Consult statistics:

```bash
curl http://localhost:8000/users/1/stats
```

---

## Owner

Desevelop for Felipe.
