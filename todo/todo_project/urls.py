from django.urls import path
from . import views
app_name = 'todo_project'
urlpatterns = [
    path('', views.index, name='index'),
    path('todo/', views.todo_projectView, name='todo1'),
    path('addTodoItem/',views.addTodoView), 
    path('deleteTodoItem/<int:i>/', views.deleteTodoView), 
] 