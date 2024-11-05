from flask import Blueprint, abort, make_response, request, Response
from app.models.task import Task
from ..db import db
from app.routes.routes_utilities import validate_model

tasks_bp = Blueprint("tasks_bp", __name__, url_prefix="/tasks")

@tasks_bp.post("")
def create_task():
    request_body = request.get_json()
    new_task = Task.from_dict(request_body)
    
    db.session.add(new_task)
    db.session.commit()

    response_body = new_task.to_dict()

    return {"task": response_body}, 201

@tasks_bp.get("")
def get_all_tasks():
    query = db.select(Task)

    title_params = request.args.get("title")
    if title_params:
        query = db.select(Task).where(Task.title == title_params)
    
    description_param = request.args.get("description")
    if description_param:
        query = db.select(Task).where(Task.description.like(f"%{description_param}%"))
    
    query = query.order_by(Task.id)

    tasks = db.session.scalars(query)

    tasks_response = []
    for task in tasks:
        tasks_response.append(task.to_dict())
    
    return tasks_response, 200

@tasks_bp.get("/<task_id>")
def get_one_task(task_id):
    task = validate_model(Task, task_id)
    return {"task": task.to_dict()}, 200

@tasks_bp.put("/<task_id>")
def update_task(task_id):
    task = validate_model(Task, task_id)

    request_body = request.get_json()

    task.title = request_body['title']
    task.description = request_body['description']
    db.session.commit()
    
    return {"task": task.to_dict()}, 200





