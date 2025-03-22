from django.db import models
from django.db.models import (CharField,
                              IntegerField,
                              DateField,
                              TextField,
                              ForeignKey,
                              DO_NOTHING,
                              DateTimeField)



# Create your models here.

class Genre(models.Model):

    name = CharField(max_length = 128)

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = CharField(max_length=128, null=False)
    ratting = IntegerField()
    released = DateField(null=True)
    description = TextField()
    created = DateTimeField(auto_now_add = True)
    genre = ForeignKey("Genre", on_delete=DO_NOTHING)



    def __repr__(self):
        return f'{self.title} - {self.released}'

    def __str__(self):
        return f'{self.title} - {self.released}'

class Director(models.Model):
    name = CharField(max_length=30, null=False)
    surname = CharField(max_length=30, null=False)

    def __repr__(self):
        return f'{self.name} {self.surname}'

    def __str__(self):
        return f'{self.name} {self.surname}'
