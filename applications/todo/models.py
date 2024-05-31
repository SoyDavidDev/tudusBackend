# Django imports
from django.db import models

# Local imports
from applications.user.models import User
from applications.lists.models import List



class Todo(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    completed = models.BooleanField(default=False, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    list_id = models.ForeignKey(
        List,
        on_delete=models.CASCADE,
        related_name='todos'
    )
    user_id = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='todos'
    )

    class Meta:
        verbose_name = 'Todo'
        verbose_name_plural = 'Todos'
        ordering = ['-id']
    

    def __str__(self):
        return self.title + ' - ' + self.list_id.title + ' - ' + self.user_id.username