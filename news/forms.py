from django import forms
from news.models import Category


class CreateCategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].label = "Nome"
        self.fields['name'].type = "text"
        self.fields['name'].name = "name"
        self.fields['name'].max_length = 200
        self.fields['name'].required = True
