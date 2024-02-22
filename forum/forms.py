from django import forms
from forum.models import Topic, Comment

class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['title', 'content']

class CommentForm(forms.ModelForm):

    content = forms.CharField(
        label='Content',
        widget=forms.Textarea(
            attrs={
                "class": "form-control"
            },
        ),
    )
    class Meta:
        model = Comment
        fields = ['content']