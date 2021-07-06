from datetime import datetime
import os

from flask import abort
from peewee import CharField, DateTimeField, Model, SqliteDatabase, TextField

from flask_sqlalchemy import SQLAlchemy
from todo import db


class Task(db.Model):
    __tablename__ = 'tasks'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150))
    content = db.Column(db.String())
    create_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<Task {self.title}>"

    def get_all_task(self):
        pass

    def get_task(self, id):
        pass

    def create_task(self, data):
        pass

    def update_task(self, id, data):
        pass

    def delete_task(self, id):
        pass


# class BaseModel(Model):
#     class Meta:
#         database = db


# class Task(BaseModel):
#     title = CharField(max_length=150)
#     content = TextField()
#     create_at = DateTimeField(default=datetime.now)

#     def __repr__(self):
#         return f"{self.id}, {self.title}, {self.content}, {self.create_at}"

#     def get_all_task(self):
#         tasks = Task.select()
#         tasks_json = []
#         for task in tasks:
#             tasks_json.append(
#                 {"id": task.id, "title": task.title, "content": task.content, "create_at": task.create_at}
#             )
#         return tasks_json

#     def get_task(self, id):
#         try:
#             task = Task.select().where(Task.id == id).get()
#             return task
#         except:
#             abort(404, f"Todo {id} doesn't exist")

#     def create_task(self, data):
#         note = Task(title=data["title"], content=data["content"], done=False)
#         note.save()
#         return note

#     def update_task(self, id, data):
#         try:
#             task = Task.select().where(Task.id == id).get()
#             if not "title" in data:
#                 abort(400)
#             if not "content" in data:
#                 abort(400)
#             task.title = data["title"]
#             task.content = data["content"]
#             task.save()
#             return task
#         except:
#             abort(404, f"Todo {id} doesn't exist")

#     def delete_task(self, id):
#         try:
#             Task.get(Task.id == id).delete_instance()
#         except:
#             abort(404, f"Todo {id} doesn't exist.")


# MODELS = [
#     Task,
# ]


# def reset_db():
#     with db:
#         db.drop_tables(MODELS)
#         db.create_tables(MODELS)
#     DAO = Task()

#     # Populating a dictionary using a dictionary generator
#     i = 0
#     while i < 10:
#         dic = {x: y for x, y in zip(("title", "content"), ("Buy milk", "Buy the most delicious milk"))}
#         DAO.create_task(dic)
#         i += 1

#     # DAO.create_task({"title": "Buy milk", "content": "Buy the most delicious milk"})
#     # DAO.create_task({"title": "Buy bread", "content": "Buy the most delicious bread"})
#     # DAO.create_task({"title": "Buy butter", "content": "Buy the most delicious butter"})
#     # DAO.create_task({"title": "Buy milk", "content": "Buy the most delicious milk"})
#     # DAO.create_task({"title": "Buy bread", "content": "Buy the most delicious bread"})
#     # DAO.create_task({"title": "Buy butter", "content": "Buy the most delicious butter"})
#     # DAO.create_task({"title": "Buy milk", "content": "Buy the most delicious milk"})
#     # DAO.create_task({"title": "Buy bread", "content": "Buy the most delicious bread"})
#     # DAO.create_task({"title": "Buy butter", "content": "Buy the most delicious butter"})
#     # DAO.create_task({"title": "Buy butter", "content": "Buy the most delicious butter"})
