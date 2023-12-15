from .models import Post
from django.forms import ModelForm, TextInput

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ["title", "post"]
        widjets = {
            "title": TextInput(attrs={
                'class':"form-control",
                'placeholder': "Название"
            }),
            "post": TextInput(attrs={
                'class': "form-control",
                'placeholder': "Введите описание"
            })
        }