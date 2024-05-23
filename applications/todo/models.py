from django.db import models

from applications.user.models import User
from applications.lists.models import List
# Create your models here.


class Todo(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    completed = models.BooleanField(default=False)
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

    def __str__(self):
        return self.name + ' - ' + self.list_id.name + ' - ' + self.user_id.username