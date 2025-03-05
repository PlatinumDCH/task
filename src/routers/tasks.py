from fastapi import APIRouter, Depends, status

from src.database import get_conn_db
from src.services.auth import auth_service
import src.repository.task as repo_task
import src.schemas as sch

router = APIRouter(prefix='/task')

@router.post('/add')
async def task_add(
    content: sch.TaskCreateSchema,
    session = Depends(get_conn_db),
    user = Depends(auth_service.get_current_user)
):
    new_task = await repo_task.create_task(
        content.title,
        content.description, 
        user.id, 
        session)
    return sch.TaskResponseSchema(**new_task.__dict__, task_id=new_task.id)


@router.get('/edit/')
async def get_all_task(
    session = Depends(get_conn_db),
    user = Depends(auth_service.get_current_user)
):
    tasks = await repo_task.get_tasks(user.id, session)
    return [sch.TaskResponseSchema.model_validate(task) for task in tasks]

@router.get("/edit/{item_id}")
async def get_task(
    item_id: int, session = Depends(get_conn_db),
    user = Depends(auth_service.get_current_user)
    ):
    task= await repo_task.get_task_by_id(item_id, user.id, session)
    return sch.TaskResponseSchema(**task.__dict__, task_id=task.id)

@router.put("/edit/{item_id}",)
async def put_edit(
    item_id: int, 
    content: sch.TaskUpdateSchema, 
    session = Depends(get_conn_db),
    user = Depends(auth_service.get_current_user)
    ):
    todo = await repo_task.update_task(user.id, item_id, content.title, content.description, session)
    return sch.TaskResponseSchema(**todo.__dict__, task_id=todo.id)


@router.delete("/delete/{item_id}")
async def delete(
    item_id: int, 
    session = Depends(get_conn_db),
    user = Depends(auth_service.get_current_user)
    ):
    await repo_task.delete_task(user.id, item_id, session)
    return {"message": "Task deleted successfully"}, status.HTTP_200_OK