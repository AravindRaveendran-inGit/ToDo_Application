from django.db import models
from django.contrib.auth.models import User
# Create your models here.

priority_choices = [
    ('🙂 ','low 🙂'),
    ('🤨 ','medium 🤨'),
    (' 😡 ','urgent 😡'),
]
class TaskModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    priority = models.CharField(max_length=7, choices=priority_choices, default='🙂',  null=False, blank=False)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['complete']    
        verbose_name_plural = "Tasks"