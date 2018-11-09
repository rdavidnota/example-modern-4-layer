from django.shortcuts import render
from application.controllers.TaskController import TaskController
from django.http import HttpResponse


# Create your views here.


def save_task(request, problem):
    task_controller = TaskController
    problem = 'error'
    task_controller.save(problem)

    return HttpResponse('OK')
