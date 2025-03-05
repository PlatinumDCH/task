# FastAPiI + Sqlalhemy + PostgreSQL + Alembic + Doscker
----
Проект: API для управління користувачами та їх задачами.
Ціль: Створити Rest Api з утентифікацією та Crud-операціями для користувачів та
їх задач

Стек:
- Backend: FastApi
- Database: PostgreSQL
- ORM: SQLAlchemy
- Migration: Alembic
- Conteinerization: Docker
----
Functional API

1.User
- Registration (email, password, name)
- Autorization (JWT)
- User profile
- Delete accont

2.Task
- Create task
- Check all task user
- Update task
- Delete task

3.Extra
- Logging
- Error handling
- Documentation Swagger/OpenApi

commands

```
створити image проєкту
docker build -t task_project:latest .
```

```
docker-compose down -v  
docker-compose up -d
```
```
docker-compose down --volumes --remove-orphans
docker-compose up --build -d
```
```
docker-compose down --volumes --remove-orphans
docker-compose up --build -d
```

```
docker-compose exec web alembic revision --autogenerate -m "Initial migration"
docker-compose exec web alembic upgrade head
```
```
.env
POSTGRES_USER=
POSTGRES_PASSWORD=
POSTGRES_DB=
```

```
docker-compose.yaml
 environment:
      - POSTGRES_USER=${POSTGRES_USER}
      - POSTGRES_PASSWORD=${POSTGRES_PASSWORD}
      - POSTGRES_DB=${POSTGRES_DB}
```
```
створити нову роль user
docker exec -it <container_id> psql -U postgres -d task_project_database
CREATE ROLE "user" WITH LOGIN PASSWORD 'user123';
GRANT ALL PRIVILEGES ON DATABASE task_project_database TO "user";
```