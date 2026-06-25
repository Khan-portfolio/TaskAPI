from fastapi import Depends, APIRouter
from typing import Annotated

from schemas.schemas import TaskAddScheme
from repositories.repository import TaskRepository
from dependency.dependencies import TaskServiceDep

router = APIRouter(
    prefix="/tasks",
    tags=["Задачи"]
)



@router.get("")
async def tasks_get(service: TaskServiceDep):
    return await service.get_all_tasks()

@router.get("/{task_id:int}")
async def task_by_id(task_id: int, service: TaskServiceDep):
    return await service.get_task_by_id(task_id)

@router.post("")
async def task_add(service: TaskServiceDep, data: Annotated[TaskAddScheme, Depends()]):
    return await service.create_new_task(data)

@router.patch("")
async def put_task(service: TaskServiceDep, task_id: int,  status: bool):
    return await service.update_task_status(task_id, status)

@router.delete("")
async def task_del(service: TaskServiceDep, task_id: int):
    return await service.delete_task(task_id)