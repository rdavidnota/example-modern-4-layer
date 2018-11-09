from application.domain.task import Task as domain_task


class ITaskContext:
    def save(self, task : domain_task):
        raise NotImplementedError

    def get_tasks(self):
        raise NotImplementedError
