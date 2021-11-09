from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class RolesUser(models.Model):
    ROLES_TYPE = (
        ("doctor", "Doctor"),
        ("paciente", "Paciente"),
    )


    user = models.OneToOneField(User, verbose_name=("User"), on_delete=models.CASCADE)
    rol = models.CharField(choices=ROLES_TYPE, max_length=20)

    class Meta:
        verbose_name = ("Roles User")
        verbose_name_plural = ("Roles User")
    
    def __str__(self):
        return self.user.username



class CustomSettings(models.Model):
    SECTIONS = (
        ("SECTION_ONE",'Section one'),
        ("SECTION_TWO",'Section two'),
        ("SECTION_THREE",'Section three'),
        ("SECTION_FOUR",'Section four'),
    )

    id_provider = models.SmallIntegerField()
    id_section = models.CharField(choices=SECTIONS, max_length=100)
    configurations = models.JSONField()
    photo = models.ImageField(upload_to='css/images/')

    def __str__(self):
        return self.id_provider