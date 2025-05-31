from rest_framework import viewsets, status
from rest_framework.response import Response
from todo.serializers.todo_serializers import TodoSerializer
from todo.models.todo_model import Todo  # Asegúrate que existe este modelo
from todo.services.todo_services import (
    get_todos, get_todo, create_todo, update_todo, delete_todo
)
from drf_spectacular.utils import extend_schema, extend_schema_view

@extend_schema(tags=['To-Dos'])
@extend_schema_view(
    list=extend_schema(summary="Listar TO-DOs", description="Lista todos los TO-DOs disponibles."),
    retrieve=extend_schema(summary="Obtener un TO-DO por ID", description="Obtiene un TO-DO específico según su ID."),
    create=extend_schema(summary="Crear un TO-DO", description="Crea un nuevo TO-DO."),
    update=extend_schema(summary="Actualizar un TO-DO", description="Actualiza completamente un TO-DO existente."),
    partial_update=extend_schema(summary="Actualizar parcialmente un TO-DO", description="Actualiza parcialmente un TO-DO existente."),
    destroy=extend_schema(summary="Eliminar un TO-DO", description="Elimina un TO-DO según su ID.")
)
class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

    def list(self, request, *args, **kwargs):
        todos = get_todos()
        serializer = self.get_serializer(todos, many=True)
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        try:
            todo = get_todo(int(kwargs['pk']))
            serializer = self.get_serializer(todo)
            return Response(serializer.data)
        except Todo.DoesNotExist:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        todo = create_todo(serializer.validated_data)
        response_serializer = self.get_serializer(todo)
        return Response(response_serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            todo = update_todo(int(kwargs['pk']), serializer.validated_data)
            response_serializer = self.get_serializer(todo)
            return Response(response_serializer.data)
        except Todo.DoesNotExist:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)

    def partial_update(self, request, *args, **kwargs):
        try:
            todo = get_todo(int(kwargs['pk']))
            serializer = self.get_serializer(todo, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            todo = update_todo(int(kwargs['pk']), serializer.validated_data)
            response_serializer = self.get_serializer(todo)
            return Response(response_serializer.data)
        except Todo.DoesNotExist:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)

    def destroy(self, request, *args, **kwargs):
        try:
            delete_todo(int(kwargs['pk']))
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Todo.DoesNotExist:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)