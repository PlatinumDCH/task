from fastapi import HTTPException
from sqlalchemy import select
from src.models import Task
from typing import Optional

async def get_task_object(item_id: int, owner_id: int, session):
    result = await session.execute(select(Task).filter(Task.id == item_id, Task.owner_id == owner_id))
    task = result.scalars().first()
    if not task:
        raise HTTPException(
            status_code=404,
            detail='Task not found'
        )
    return task


async def create_task(
        title: str, 
        description: Optional[str],  
        user_id: int, 
        session):
    new_task = Task(title=title,description=description,owner_id=user_id)
    session.add(new_task)
    await session.commit()
    await session.refresh(new_task)
    return new_task

async def get_task_by_id(item_id: int, owner_id: int, session):
    return await get_task_object(item_id, owner_id, session)

async def get_tasks(owner_id: int, session):
    result = await session.execute(select(Task).filter(Task.owner_id == owner_id))
    tasks = result.scalars().all()
    if not tasks:
        raise HTTPException(
            status_code=404,
            detail='No tasks found'
        )
    return tasks

async def update_task(owner_id: int, item_id: int, title, description, session):
    task = await get_task_object(item_id, owner_id, session)
    task.title = title
    task.description = description
    await session.commit()
    await session.refresh(task)
    return task

async def delete_task(owner_id: int, item_id: int, session):
    task = await get_task_object(item_id, owner_id, session)
    await session.delete(task)
    await session.commit()
    