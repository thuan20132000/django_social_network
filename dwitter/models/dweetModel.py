
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class Dweet(models.Model):
    user = models.ForeignKey(
        User,
        related_name="dweets",
        on_delete=models.DO_NOTHING
    )
    body = models.CharField(max_length=140)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return (
            f"{self.user} "
            f"{self.created_at:%Y-%m-%d %H:%M}: "
            f"{self.body[:30]} "
        )
    
