from django.db import models


class Status(models.Model):
    status = models.CharField('Status', max_length=100)

    def __str__(self):
        return self.status

