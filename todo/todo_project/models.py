from django.db import models

# Create your models here.
class TodoListItem(models.Model):
    content = models.TextField() 
    date= models.DateField(auto_now_add=True)