from django.core.exceptions import ValidationError
from todo.models.todo_model import Todo

def create_todo(data: dict) -> Todo:
  title = data.get('title')
  if not title:
    raise ValidationError('Title is required')
  
  description = data.get('description')
  if not description:
    raise ValidationError('Description is required')
  
  completed = data.get('completed', False)
  
  return Todo.objects.create(title=title, description=description, completed=completed)

def get_todos():
  return Todo.objects.order_by('created_at')

def get_todo(pk: int) -> Todo:
  try:
    return Todo.objects.get(pk=pk)
  except Todo.DoesNotExist:
    raise ValidationError(f'TODO with id {id} does not exist')

def update_todo(pk: int, data: dict) -> Todo:
  todo = get_todo(pk)
  
  for field in ('title', 'description', 'completed'):
    if field in data:
      setattr(todo, field, data[field])
  
  todo.save()
  return todo


def delete_todo(pk: int):
  todo = Todo.objects.get(pk=pk)
  todo.delete()
