from django.db import models

from applications.user.models import User
# Create your models here.

class List(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user_id = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='lists'
    )

    def __str__(self):
        return self.name + ' - ' + self.user_id.username
