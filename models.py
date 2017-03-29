from peewee import *
import datetime

db = SqliteDatabase('posts.db')

class Post(Model):
    #If there is no primary key set, peewee will do it automatically
    id = PrimaryKeyField()
    date = DateTimeField(default = datetime.datetime.now)
    title = CharField()
    text = TextField()

    class Meta:
        database = db

def initialize_db():
    db.connect()
    db.create_tables([Post], safe=True)