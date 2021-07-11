from datetime import datetime

from flask import abort

from todo import db


class Task(db.Model):
    __tablename__ = "tasks"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150))
    content = db.Column(db.String())
    create_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<Task {self.title}>"

    def get_all_task(self):
        tasks = Task.query.all()
        results = [
            {"id": task.id, "title": task.title, "content": task.content, "create_at": task.create_at} for task in tasks
        ]
        return results

    def create_task(self, data):
        task = Task(title=data["title"], content=data["content"])
        db.session.add(task)
        db.session.commit()
        return task

    def get_task(self, id):
        task = Task.query.get_or_404(id)
        return task

    def update_task(self, id, data):
        task = Task.query.get_or_404(id)
        if not "title" in data:
            abort(400)
        if not "content" in data:
            abort(400)
        task.title = data["title"]
        task.content = data["content"]
        db.session.add(task)
        db.session.commit()
        return task

    def delete_task(self, id):
        task = Task.query.get_or_404(id)
        db.session.delete(task)
        db.session.commit()
