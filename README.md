# TaskFlow 🚀

Sistema completo de gerenciamento de tarefas desenvolvido com FastAPI, MySQL e JavaScript puro.

## Funcionalidades

- Cadastro de usuários
- Criação de tarefas
- Atualização de status
- Exclusão de tarefas
- Categorias personalizadas
- Estatísticas por usuário
- API REST documentada com Swagger
- Integração entre frontend e backend

---

## Estrutura do Projeto

```text
taskflow/
│
├── backend/
│   ├── __pycache__/
│   ├── .env
│   ├── .env.example
│   ├── crud.py            # Operações CRUD
│   ├── database.py        # Conexão com MySQL
│   ├── main.py            # Aplicação FastAPI
│   ├── models.py          # Modelos SQLAlchemy
│   ├── requirements.txt   # Dependências
│   ├── schemas.py         # Schemas Pydantic
│   └── test_db.py         # Teste de conexão com banco
│
├── database/
│   └── schema.sql         # Script de criação do banco
│
├── frontend/
│   ├── app.js             # Lógica da interface
│   └── index.html         # Interface web
│
├── .gitignore
├── README.md
└── play.py                # Arquivo auxiliar para testes
```

---

## Tecnologias Utilizadas

| Camada | Tecnologia |
|---------|-----------|
| Backend | FastAPI |
| ORM | SQLAlchemy 2.0 |
| Validação | Pydantic |
| Banco de Dados | MySQL 8 |
| Driver | PyMySQL |
| Frontend | HTML5, CSS3 e JavaScript |
| API Docs | Swagger UI |

---

## Pré-requisitos

- Python 3.11+
- MySQL 8+
- Git

---

## Configuração do Banco de Dados

Entre no MySQL:

```bash
mysql -u root -p
```

Execute o script:

```bash
source database/schema.sql
```

Ou:

```bash
mysql -u root -p < database/schema.sql
```

---

## Configuração do Backend

Entre na pasta do backend:

```bash
cd backend
```

Crie o ambiente virtual:

```bash
python -m venv .venv
```

Ative o ambiente:

### Windows

```bash
.venv\Scripts\activate
```

### Linux/Mac

```bash
source .venv/bin/activate
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

Copie o arquivo de exemplo:

```bash
cp .env.example .env
```

Configure as credenciais do banco:

```env
DB_HOST=localhost
DB_PORT=3306
DB_NAME=taskflow
DB_USER=root
DB_PASSWORD=sua_senha
```

---

## Testando a Conexão com o Banco

```bash
python test_db.py
```

---

## Executando a API

```bash
uvicorn main:app --reload
```

Acesse:

- API: http://localhost:8000
- Swagger: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

---

## Executando o Frontend

Abra diretamente o arquivo:

```bash
frontend/index.html
```

Ou utilize um servidor local:

```bash
cd frontend
python -m http.server 3000
```

Acesse:

```text
http://localhost:3000
```

---

## Endpoints Disponíveis

| Método | Endpoint | Descrição |
|----------|----------|----------|
| GET | / | Health Check |
| GET | /users | Listar usuários |
| POST | /users | Criar usuário |
| GET | /users/{id}/tasks | Listar tarefas |
| POST | /tasks | Criar tarefa |
| PATCH | /tasks/{id} | Atualizar tarefa |
| DELETE | /tasks/{id} | Excluir tarefa |
| GET | /users/{id}/stats | Estatísticas |
| GET | /users/{id}/categories | Categorias |
| POST | /categories | Criar categoria |
| DELETE | /categories/{id} | Excluir categoria |

---

## Exemplos de Requisição

Criar tarefa:

```bash
curl -X POST http://localhost:8000/tasks \
-H "Content-Type: application/json" \
-d '{"title":"Minha tarefa","priority":"high","user_id":1}'
```

Atualizar status:

```bash
curl -X PATCH http://localhost:8000/tasks/1 \
-H "Content-Type: application/json" \
-d '{"status":"done"}'
```

Consultar estatísticas:

```bash
curl http://localhost:8000/users/1/stats
```

---

## Autor

Desenvolvido por Felipe.
