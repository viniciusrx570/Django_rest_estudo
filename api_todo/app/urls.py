from django.urls import  path
from .views import TodoListAndCreate, TodoDetailChangeAndDelete

urlpatterns = [
    path('', TodoListAndCreate.as_view()),
    path('<int:pk>/', TodoDetailChangeAndDelete.as_view()),
]
