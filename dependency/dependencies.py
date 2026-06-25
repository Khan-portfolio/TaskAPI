from typing import Annotated
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from repositories.repository import TaskRepository
from service.service import TaskServices
from models.model import new_session

async def get_session():
    async with new_session() as session:
        yield session

SessionDep = Annotated[AsyncSession,Depends(get_session)]

async def get_task_repo(session: SessionDep) -> TaskRepository:
    return TaskRepository(session)

TaskRepoDep = Annotated[TaskRepository, Depends(get_task_repo)]

def get_task_service(repo: TaskRepoDep) -> TaskServices:
    return TaskServices(repo)

TaskServiceDep = Annotated[TaskServices, Depends(get_task_service)]