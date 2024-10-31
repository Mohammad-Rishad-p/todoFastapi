from tortoise.models import Model
from tortoise.fields import IntField, BooleanField, CharField

# Defining model class 'ToDo' to represnt a title for todo task, its status and task's description
class ToDo(Model):
    id = IntField(pk=True) #sets id as primary key
    title = CharField(max_length=100, null=False)  
    description = CharField(max_length=100, null=False)
    done = BooleanField(default=False, null=False)