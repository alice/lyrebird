from django.db import models

class Word(models.Model):
    base_form = models.CharField(max_length=150)

    def __unicode__(self):
        return self.base_form

class Language(models.Model):
    name = models.CharField(max_length=150)

# Create your models here.
