from django import forms
from . import models


class CalcForm(forms.Form):
    pass


class PostForm(forms.ModelForm):
    """
    Model form for post model
    """

    class Meta:
        model = models.Post
        fields = [
            'title',
            'content',
            'intro_image',
            'categories',
        ]
