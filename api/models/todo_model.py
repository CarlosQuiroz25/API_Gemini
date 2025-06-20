from django.db import models

class Todo(models.Model):
  id = models.AutoField(primary_key=True)
  title = models.CharField(max_length=100)
  description = models.TextField()
  completed = models.BooleanField(default=False)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.title