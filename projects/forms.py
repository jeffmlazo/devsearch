from django.forms import ModelForm
from django import forms
from .models import Project, Review


class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'featured_image', 'description',
                  'demo_link', 'source_link', 'tags']
        widgets = {
            'tags': forms.CheckboxSelectMultiple(),
        }

    def __init__(self, *args, **kwargs):
        super(ProjectForm, self).__init__(*args, **kwargs)

        # All input fields will have 'input' class
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})

        # self.fields['title'].widget.attrs.update(
        #     {'class': 'input--text', 'placeholder': 'Enter Text'})

        # self.fields['description'].widget.attrs.update(
        #     {'class': 'input--textarea', 'placeholder': 'Enter Description'})


class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['value', 'body']

    labels = {
        'value': 'Place your vote',
        'body': 'Add a comment with your vote',
    }

    def __init__(self, *args, **kwargs):
        super(ReviewForm, self).__init__(*args, **kwargs)

        # All input fields will have 'input' class
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})
