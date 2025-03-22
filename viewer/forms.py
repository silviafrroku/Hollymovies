from django.core.exceptions import ValidationError
from django.forms import (Form, CharField, IntegerField, DateField,
                          Textarea, ModelChoiceField, ModelForm)
from datetime import date
from .models import Genre, Movie ,Director


def date_validator(value):
    if value <date(year = 1970,month= 1, day=1):
        raise ValidationError("Date can not be older than 1970-01-01")
    return value

class MovieForm(Form):
    title = CharField(max_length=128)
    ratting = IntegerField(min_value=1,max_value=10)
    released = DateField()
    description = CharField(widget=Textarea)
    genre = ModelChoiceField(queryset=Genre.objects)




    def clean_title(self):
        return self.cleaned_data["title"].capitalize()

    def clean_ratting(self):
        if 3 < self.cleaned_data["ratting"] < 5:
            raise ValidationError("The ratting can not be betwen 3 and 5")
        return self.cleaned_data["ratting"]
    
    def clean(self):
        if self.cleaned_data['genre'].name == 'Action' and self.cleaned_data['rating']>=8:
            raise ValidationError('Action movies canot be that good')
        return super().clean()

class MovieModelForm(ModelForm):
    class Meta :
        model = Movie
        fields = '__all__'
    ratting = IntegerField(min_value=1,max_value=10)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'



class DirectorModelForm(ModelForm):
    class Meta:
        model = Director
        fields = '__all__'