from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=100, verbose_name="full name")
    email = models.EmailField(max_length=100)

    def __str__(self):
    	return str(self.email)
