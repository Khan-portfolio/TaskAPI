from fastapi import HTTPException, status
from repositories.repository import TaskRepository
from schemas.schemas import TaskAddScheme

class TaskServices:
    def __init__(self, task_repo: TaskRepository):
        self.task_repo = task_repo

    async def get_all_tasks(self):
        task = await self.task_repo.get_all_tasks()
        if not task:
            return {"message": None}
        return task
    
    async def get_task_by_id(self, task_id: int):
        task = await self.task_repo.get_by_id(task_id)
        if not task:
            raise HTTPException(
                status_code = status.HTTP_404_NOT_FOUND,
                detail = f"There is no task with {task_id} id"
                )
        return [{"Task": task}]

    async def create_new_task(self, data: TaskAddScheme):
        return await self.task_repo.add_task(data)
    
    async def update_task_status(self, task_id: int, status: bool):
        task = await self.task_repo.get_by_id(task_id)
        if not task:
            raise HTTPException(
                status_code = status.HTTP_404_NOT_FOUND,
                detail = f"Task with {task_id} id was not found"
            )
        
        await self.task_repo.update_task_by_id(task_id, status)
        return {"message": "Updated successfully"}
    
    async def delete_task(self, task_id: int):
        task = await self.task_repo.get_by_id(task_id)
        if not task:
            raise HTTPException(
                status_code = status.HTTP_404_NOT_FOUND,
                detail = f"Task with {task_id} was not found"
            )
        
        await self.task_repo.delete_task_by_id(task_id)
        return {"message": "Deleted"}