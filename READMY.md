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

при першому запуску потрібно вказати супер користувача

```
.env
POSTGRES_USER=admin
POSTGRES_PASSWORD=
POSTGRES_DB=task_project_database 
```

```
docker-compose.yaml
 environment:
      - POSTGRES_USER=${POSTGRES_USER}
      - POSTGRES_PASSWORD=${POSTGRES_PASSWORD}
      - POSTGRES_DB=${POSTGRES_DB}
```

стоворити роль адміна
id_контейнеру = docker ps
docker exec -it <id container> psql -U <standart role> -d <database name>


docker-compose down -v  
docker-compose up -d

docker-compose down --volumes --remove-orphans
docker-compose up --build -d

