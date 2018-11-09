from application.persistencia.itaskcontext import ITaskContext
from application.domain.task import Task as domain_task
from persistencia.models import Task as task_repository
from common.globals import Status


class TaskContext(ITaskContext):
    task_model = task_repository()

    def __init__(self):
        self.task_model = task_repository()

    def save(self, task):
        self.task_model.problem = task.problem
        self.task_model.status = task.status.value
        self.task_model.date = task.date
        self.task_model.save()

    def get_tasks(self):
        results = self.task_model.objects.all()
        tasks = []
        for result in results:
            task = domain_task()

            task.problem = result.problem
            task.status = Status(result.status)
            task.date = result.date
            tasks.append(task)
        return tasks
