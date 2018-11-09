from persistencia.concrets.TaskContext import TaskContext


class TaskFactory:

    def __init__(self, task_type):
        return TaskContext()
