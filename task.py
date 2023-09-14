class Task:
    def __init__(self, title, description=None, completed=False):
        self.title = title
        self.description = description
        self.completed = completed

    def mark_completed(self):
        self.completed = True

    def __str__(self):
        status = "Completed" if self.completed else "Not Completed"
        task_info = f"Title: {self.title}\nStatus: {status}\n"
        if self.description:
            task_info += f"Description: {self.description}\n"
        return task_info
