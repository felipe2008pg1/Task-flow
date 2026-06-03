# TaskFlow 🚀
Gerenciador de tarefas com **FastAPI** + **MySQL** + **HTML/CSS/JS puro**

## Estrutura do Projeto

```
taskflow/
├── backend/
│   ├── main.py          # Aplicação FastAPI + rotas
│   ├── models.py        # Modelos SQLAlchemy (ORM)
│   ├── schemas.py       # Schemas Pydantic (validação)
│   ├── crud.py          # Operações de banco de dados
│   ├── database.py      # Conexão com MySQL
│   ├── requirements.txt
│   └── .env.example
├── database/
│   └── schema.sql       # Script de criação do banco
└── frontend/
    └── index.html       # Interface web completa
```

## Pré-requisitos

- Python 3.11+
- MySQL 8.0+
- Navegador moderno

---

## 1. Configurar o Banco de Dados

```bash
# Acessar o MySQL
mysql -u root -p

# Executar o schema
source /caminho/para/taskflow/database/schema.sql
```

Ou via linha de comando:
```bash
mysql -u root -p < database/schema.sql
```

---

## 2. Configurar o Backend

```bash
cd backend

# Criar ambiente virtual
python -m venv .venv
source .venv/bin/activate      # Linux/Mac
# .venv\Scripts\activate       # Windows

# Instalar dependências
pip install -r requirements.txt

# Configurar variáveis de ambiente
cp .env.example .env
# Edite o .env com suas credenciais do MySQL
```

### `.env`
```
DB_HOST=localhost
DB_PORT=3306
DB_NAME=taskflow
DB_USER=root
DB_PASSWORD=sua_senha
```

### Iniciar a API
```bash
uvicorn main:app --reload --port 8000
```

A API estará disponível em: http://localhost:8000  
Documentação interativa: http://localhost:8000/docs

---

## 3. Abrir o Frontend

Abra diretamente no navegador:
```bash
# Linux/Mac
open frontend/index.html

# Ou use um servidor local
cd frontend && python -m http.server 3000
# Acesse: http://localhost:3000
```

---

## Endpoints da API

| Método   | Endpoint                         | Descrição              |
|----------|----------------------------------|------------------------|
| `GET`    | `/`                              | Health check           |
| `GET`    | `/users`                         | Listar usuários        |
| `POST`   | `/users`                         | Criar usuário          |
| `GET`    | `/users/{id}/tasks`              | Listar tarefas         |
| `POST`   | `/tasks`                         | Criar tarefa           |
| `PATCH`  | `/tasks/{id}`                    | Atualizar tarefa       |
| `DELETE` | `/tasks/{id}`                    | Deletar tarefa         |
| `GET`    | `/users/{id}/stats`              | Estatísticas           |
| `GET`    | `/users/{id}/categories`         | Listar categorias      |
| `POST`   | `/categories`                    | Criar categoria        |
| `DELETE` | `/categories/{id}`               | Deletar categoria      |

---

## Exemplos de Uso (curl)

```bash
# Criar uma tarefa
curl -X POST http://localhost:8000/tasks \
  -H "Content-Type: application/json" \
  -d '{"title":"Minha tarefa","priority":"high","user_id":1}'

# Atualizar status
curl -X PATCH http://localhost:8000/tasks/1 \
  -H "Content-Type: application/json" \
  -d '{"status":"done"}'

# Ver estatísticas
curl http://localhost:8000/users/1/stats
```

---

## Tecnologias

| Camada   | Tecnologia                          |
|----------|-------------------------------------|
| Backend  | FastAPI, SQLAlchemy, Pydantic       |
| Banco    | MySQL 8.0                           |
| ORM      | SQLAlchemy 2.0                      |
| Frontend | HTML5, CSS3, JavaScript (Vanilla)   |
| Driver   | PyMySQL                             |