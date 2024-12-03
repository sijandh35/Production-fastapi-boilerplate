from fastapi import APIRouter
from celery.result import AsyncResult
from workers.shared_tasks import high_priority_task, default_task, low_priority_task

router = APIRouter()

import json

@router.post("/tasks/high-priority")
async def send_high_priority_task(data: dict):
    print("code started",data)
    task = high_priority_task.apply_async(args=[json.dumps(data)])  # Serialize data
    return {"task_id": task.id, "status": "Task sent to high-priority queue"}


@router.post("/tasks/default")
async def send_default_task(data: dict):
    """Send a task to the default queue."""
    task = default_task.apply_async(args=[data])  # Send task to Celery
    return {"task_id": task.id, "status": "Task sent to default queue"}

@router.post("/tasks/low-priority")
async def send_low_priority_task(data: dict):
    """Send a task to the low-priority queue."""
    task = low_priority_task.apply_async(args=[data])  # Send task to Celery
    return {"task_id": task.id, "status": "Task sent to low-priority queue"}

@router.get("/tasks/status/{task_id}")
async def get_task_status(task_id: str):
    """Get the status of a task by ID."""
    result = AsyncResult(task_id)
    return {"task_id": task_id, "status": result.status, "result": result.result}
