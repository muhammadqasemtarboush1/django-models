from django.db import models
from django.contrib.auth import get_user_model


# Create your models here.
# Snack d
# create Snack model d
# make sure it extends from proper base class d
# add name as a CharField with maximum length of 64 characters. d
# add purchaser ForeignKey related to Django’s built in user model with CASCADE delete option. d
# from django.contrib.auth import get_user_model  d
# add description TextField
class Snack(models.Model):
    name = models.CharField(max_length=255, help_text="Snack Name", default="Snack")
    purchaser = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    description = models.TextField(default='Description', blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Snack"
        verbose_name_plural = "Snacks"
