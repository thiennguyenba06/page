from django.db import models

# Create your models here.
class todo(models.Model):
    content = models.TextField(default = '')
    status = models.BooleanField(default = False)
    def __str__(self) -> str:
        return self.content
    