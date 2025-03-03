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
docker build -t task_project:latest .
```
при першому запуску потрібно вказати супер користувача
```
.env
POSTGRES_USER=admin  # тобто відразу створюємо роль
POSTGRES_PASSWORD=
POSTGRES_DB=task_project_database 

docker-compose.yaml
 environment:
      - POSTGRES_USER=${POSTGRES_USER}
      - POSTGRES_PASSWORD=${POSTGRES_PASSWORD}
      - POSTGRES_DB=${POSTGRES_DB}
```

стоврити роль адміна
id_контейнеру = 036d2b182856
task_project_database - назва бази данних
docker exec -it id_контейнеру psql -U super_user -d task_project_database


docker-compose down -v  # зупинити конейнери ти видалити volumes
docker-compose up -d  # запустит в фоновому режимч

перезапустити конейнер та перезібрати образ
docker-compose down --volumes --remove-orphans
docker-compose up --build -d

