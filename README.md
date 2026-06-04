# TaskFlow Core 🚀
> Console administrativo de alta performance para gerenciamento de fluxos de trabalho e controle de payloads de tarefas.

O **TaskFlow** é um ecossistema completo focado em arquitetura backend assíncrona, utilizando **FastAPI** para o roteamento de alta velocidade, **MySQL** como camada de persistência relacional estável e um painel frontal responsivo construído em **JavaScript Vanilla**.

---

## 📂 Arquitetura do Repositório

taskflow/├── .venv/               # Ambiente virtual isolado Python├── .vscode/             # Escopo de workspace (launch.json, settings.json)├── backend/│   ├── pycache/     # Arquivos de bytecode compilados│   ├── .env             # Variáveis confidenciais de produção (Ignorado)│   ├── .env.example     # Template estrutural para o deploy│   ├── crud.py          # Queries estruturadas e manipulação via ORM│   ├── database.py      # Engine de conexão e sessão do SQLAlchemy│   ├── main.py          # Ponto de entrada FastAPI e middleware CORS│   ├── models.py        # Esquemas de tabelas relacionais do banco│   ├── requirements.txt # Manifesto de dependências do ecossistema│   ├── schemas.py       # Validadores estáticos de dados (Pydantic)│   └── test_db.py       # Script isolado para validação de handshake com o banco├── database/│   └── schema.sql       # Script DDL para inicialização das tabelas no MySQL├── frontend/│   └── index.html       # Interface única (Layout Premium + Lógica Síncrona)├── .gitignore           # Diretivas de exclusão do controle de versão├── play.py              # Script utilitário para execuções rápidas└── README.md            # Documentação técnica do sistema
---

## 🛠️ Pré-requisitos Operacionais

* **Runtime:** Python 3.11 ou superior
* **Engine Relacional:** MySQL Server 8.0+
* **Interface:** Qualquer navegador moderno com suporte a ES6+

---

## 🚀 Setup do Ambiente

### 1. Camada de Persistência (MySQL)
Abra a linha de comando do seu banco de dados e execute o script DDL para subir a estrutura de tabelas:

```bash
# Autenticação no servidor local
mysql -u root -p

# Execução do script estrutural
source /caminho/para/taskflow/database/schema.sql
Alternativa direta via terminal:Bashmysql -u root -p < database/schema.sql
2. Engine do Backend (FastAPI)Navegue até o diretório do servidor, instale os pacotes necessários e configure os ponteiros de ambiente:Bash# Acessar diretório raiz do backend
cd backend

# Instanciar ambiente virtual isolado
python -m venv .venv

# Inicializar ambiente virtual
source .venv/bin/activate      # Linux/Mac
.venv\Scripts\activate         # Windows

# Instalação em lote das dependências
pip install -r requirements.txt

# Clonar arquivo de configuração de variáveis
cp .env.example .env
Abra o arquivo .env gerado e insira suas credenciais locais do MySQL:Ini, TOMLDB_HOST=localhost
DB_PORT=3306
DB_NAME=taskflow
DB_USER=root
DB_PASSWORD=sua_senha_aqui
Iniciar o Servidor APIBashuvicorn main:app --reload --port 8000
Endpoint Base: http://localhost:8000Swagger UI (Docs Interativos): http://localhost:8000/docs3. Interface Visual (Frontend)O painel administrativo foi unificado em um único arquivo para mitigar problemas latentes de cache de scripts estáticos.Bash# Execução nativa (Linux/Mac)
open frontend/index.html

# Execução via servidor HTTP embarcado do Python
cd frontend && python -m http.server 3000
Acesse o painel local através do endereço: http://localhost:3000🗺️ Mapeamento de Endpoints (API Rest)CamadaMétodoEndpointFunção SistêmicaCoreGET/Health Check / Validação de IntegridadeUsersGET/usersColeta de usuários cadastradosUsersPOST/usersInserção de novo registro (E-mail único)TasksGET/users/{id}/tasksBusca indexada de tarefas por UIDTasksPOST/tasksRegistro de tarefa vinculadaTasksPATCH/tasks/{id}Atualização pontual de estado (Concluir)TasksDELETE/tasks/{id}Remoção física da tarefa no bancoStatsGET/users/{id}/statsAgrupamento de volumetria analíticaCategoryGET/users/{id}/categoriesListagem de escopos do usuárioCategoryPOST/categoriesInstanciação de nova categoriaCategoryDELETE/categories/{id}Expulsão de categoria por ID🧪 Casos de Teste Estruturados (cURL)Inserir Nova Tarefa pendente no pipelineBashcurl -X POST http://localhost:8000/tasks \
  -H "Content-Type: application/json" \
  -d '{"title": "Otimizar Queries Relacionais", "priority": "Alta", "user_id": 1}'
Alterar Estado para Concluída (Requisição de Patch)Bashcurl -X PATCH http://localhost:8000/tasks/1 \
  -H "Content-Type: application/json" \
  -d '{"status": "Concluída"}'
💻 Stack TecnológicoBackend Framework: FastAPI (ASGI)ORM / Abstração de Dados: SQLAlchemy 2.0Data Validation: Pydantic v2Database Driver: PyMySQLInterface UI: HTML5 / CSS3 Avançado (Glassmorphism & Dark Mode) / JS Vanilla (Manipulação de DOM assíncrona)
