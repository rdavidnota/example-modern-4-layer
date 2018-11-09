from django.http import request
from application.factories.TaskFactory import TaskFactory
from application.configuration import config
from application.domain.task import Task as domain_task
from application.persistencia.itaskcontext import ITaskContext
from persistencia.concrets.TaskContext import TaskContext
from common.globals import Status


class TaskController(object):
    task_context = TaskContext

    def __init__(self):
        self.task_context = TaskContext

    def save(self, problem):

        task = domain_task()
        task.changue_problem(problem)

        self.task_context.save(task)
