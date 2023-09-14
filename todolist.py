import json

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def list_tasks(self):
        return self.tasks

    def complete_task(self, task_title):
        for task in self.tasks:
            if task.title == task_title:
                task.mark_completed()
                return True
        return False

    def delete_task(self, task_title):
        for task in self.tasks:
            if task.title == task_title:
                self.tasks.remove(task)
                return True
        return False

    def save_tasks(self, filename):
        with open(filename, 'w') as file:
            json.dump([task.__dict__ for task in self.tasks], file)

    def load_tasks(self, filename):
        try:
            with open(filename, 'r') as file:
                data = json.load(file)
                self.tasks = [Task(**task_data) for task_data in data]
        except FileNotFoundError:
            pass
