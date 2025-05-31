from rest_framework import serializers
from api.models.todo_model import Todo

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ['id', 'title', 'description', 'completed', 'created_at', 'updated_at']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].help_text = 'Título de la tarea'
        self.fields['description'].help_text = 'Descripción de la tarea'
        self.fields['completed'].help_text = 'Indica si la tarea está completada'
        self.fields['created_at'].help_text = 'Fecha y hora de creación de la tarea'
        self.fields['updated_at'].help_text = 'Fecha y hora de actualización de la tarea'