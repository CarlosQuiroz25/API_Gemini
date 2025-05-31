from rest_framework.routers import DefaultRouter
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView
from todo.views.todo_views import TodoViewSet

router = DefaultRouter()
router.register(r'todos', TodoViewSet, basename='todo')

urlpatterns = [
  path('', include(router.urls)),
  path('docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'), 
  path('schema/', SpectacularAPIView.as_view(), name='schema'),
  path('redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]