from django.conf import settings
from django.db import models
from django.utils import timezone

class Form(models.Model):
    name = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    email = models.EmailField()
    phone = models.CharField(max_length=11)
    cep = models.CharField(max_length=8)
    home_number = models.CharField(max_length=8)
    complement = models.TextField()
    cpf = models.CharField(max_length=11)


    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name
