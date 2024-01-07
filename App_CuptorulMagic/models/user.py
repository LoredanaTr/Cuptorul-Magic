from django.db import models


class CustomUser(models.Model):
    name = models.CharField(max_length=200) #acest char este echivalentul unui string sis e regaseste in modelele python
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=50)
    is_logged = models.BooleanField(default=False) #ianite de a se inregistra un utilizator va fi by default=false

    def __str__(self): #metoda super
        return f'User (name = {self.name}, email = {self.email})'

