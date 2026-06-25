from sqlalchemy import select, delete, update
from sqlalchemy.ext.asyncio import AsyncSession
from models.model import TaskModel
from schemas.schemas import TaskAddScheme

class TaskRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_by_id(self, task_id: int):
        result = await self.session.execute(select(TaskModel).where(TaskModel.id == task_id))
        return result.scalar_one_or_none()
    
    async def get_all_tasks(self) -> list[TaskModel]:
        result = await self.session.execute(select(TaskModel))
        return list(result.scalars().all())
    
    async def add_task(self, data: TaskAddScheme) -> TaskModel | None:
        task_dict = data.model_dump()
        task = TaskModel(**task_dict)

        self.session.add(task)
        await self.session.commit()
        await self.session.refresh(task)
        return task
    
    async def update_task_by_id(self, task_id: int, status: bool):
        await self.session.execute(update(TaskModel).where(TaskModel.id == task_id).values(status=status))
        await self.session.commit()
        return {"Update": True}
    
    async def delete_task_by_id(self, task_id: int):
        await self.session.execute(delete(TaskModel).where(TaskModel.id == task_id))
        await self.session.commit()
        return {"Delete": True}