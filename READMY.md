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