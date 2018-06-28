from celery import current_app


def is_task_exist(module_name: str, task_name: str) -> bool:
    return combine_task_path(module_name, task_name) in current_app.tasks


def combine_task_path(module_name: str, task_name: str) -> str:
    return ('.').join([module_name, task_name])
