from django import forms
from .import models

class NewStory(forms.ModelForm):
    class Meta:
        model = models.Story
        fields = ['title','body','slug','thumb']
