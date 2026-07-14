# TodoApp — FastAPI REST API & Web Application

Full-stack web application for managing tasks (todo list) with user authentication,
roles (admin/user), and server-rendered pages. The project demonstrates building a
secure, tested backend service in Python with modern production-development tools.

## Technologies

**Backend framework**
- [FastAPI](https://fastapi.tiangolo.com/) — main web framework for building the REST API
- [Uvicorn](https://www.uvicorn.org/) — ASGI server for running the application
- [Pydantic v2](https://docs.pydantic.dev/) — input/output data validation and schema models

**Database**
- [PostgreSQL](https://www.postgresql.org/) — production relational database
- [SQLAlchemy 2.0](https://www.sqlalchemy.org/) (ORM) — model-to-table mapping, queries
- [Alembic](https://alembic.sqlalchemy.org/) — database migrations (schema versioning)
- `psycopg2-binary` — PostgreSQL driver

**Authentication and security**
- JWT tokens ([`python-jose`](https://python-jose.readthedocs.io/)) — stateless authentication
- OAuth2 Password Flow (`OAuth2PasswordBearer`) — standard FastAPI security flow
- [`passlib`](https://passlib.readthedocs.io/) + `bcrypt` — secure password hashing
- Role-based access control (RBAC) — separate permissions for `admin` and `user` roles
- Cookie-based authentication for web pages and Bearer token authentication for API calls

**Frontend (server-side rendering)**
- [Jinja2](https://jinja.palletsprojects.com/) — templating engine for HTML pages
- Bootstrap — styling and responsive layout
- Static assets (CSS/JS) served via FastAPI `StaticFiles`

**Testing**
- [pytest](https://docs.pytest.org/) + `pytest-asyncio` — unit and integration tests
- `httpx` / `TestClient` — testing API endpoints without running a real server
- Separate test database (SQLite) and mocked dependency injection (`get_db`, `get_current_user`)

**Configuration and environment**
- `python-dotenv` — loading environment variables (`.env`) — database configuration without
  hardcoded credentials
- Python virtual environment (`venv`)

## Project architecture

```
App/
├── main.py            # application entry point, router registration
├── database.py        # database connection, SQLAlchemy engine and session
├── models.py           # ORM models (Users, Todos)
├── routers/
│   ├── auth.py         # registration, login, JWT issuance/validation
│   ├── todos.py        # CRUD for tasks (owner-restricted)
│   ├── admin.py        # administrator overview and deletion of all tasks
│   └── users.py        # password change, phone number change
├── templates/          # Jinja2 HTML templates
├── static/             # CSS/JS assets
└── test/               # pytest test suite
alembic/                # database migrations
```

## Key features

- User registration and login with hashed passwords
- Issuing JWT access tokens with an expiration time and user/role data
- CRUD operations on tasks — each user sees and edits only their own tasks
- Admin panel — view and delete all tasks in the system
- Password and user data change with validation of the existing password
- Server-rendered pages (login, registration, task list, editing) with
  cookie-based session protection and automatic redirect to login
- Health-check endpoint (`/healthy`) for service availability monitoring

## Running the project locally

```bash
# 1. Create and activate a virtual environment
python -m venv venv
source venv/bin/activate

# 2. Install dependencies
pip install -r requirements.txt

# 3. Set up environment variables (copy the example and fill in your own values)
cp .env.example .env

# 4. Apply database migrations
alembic upgrade head

# 5. Run the application
uvicorn App.main:app --reload
```

The application is available at `http://localhost:8000`, and the interactive API
documentation (Swagger UI) at `http://localhost:8000/docs`.

## Running tests

```bash
pytest
```
