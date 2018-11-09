from common.globals import Status
from datetime import datetime


class Task:
    problem = ''
    status = Status.New
    date = datetime.now()

    def __init__(self):
        self.problem = ''
        self.status = Status.New
        self.date = datetime.now()

    def changue_problem(self, problem):
        self.problem = problem
        self.status = Status.New
        self.date = datetime.now()

    def mark_as_reported(self):
        self.status = Status.Report
        self.date = datetime.now()

    def mark_as_closed(self):
        self.status = Status.Close
        self.date = datetime.now()
