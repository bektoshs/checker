from django.db import models

class Website(models.Model):
    address = models.CharField(max_length=255, unique=True)
    status = models.CharField(max_length=50)

    def __str__(self):
        return self.address
