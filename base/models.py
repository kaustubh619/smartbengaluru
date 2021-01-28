from django.db import models

# Create your models here.
class Application(models.Model):
    name = models.CharField(max_length=100, unique=True)
    url = models.URLField()
    logo = models.ImageField(upload_to='logo')

    def __str__(self):
        return str(self.name)
