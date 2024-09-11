from django import forms
from django_quill.forms import QuillFormField


class AddCommentForm(forms.Form):
    content = forms.CharField(max_length=511, widget=forms.Textarea, label="Comment")


class PostCreationForm(forms.Form):
    title = forms.CharField(max_length=255, required=True)
    #hashtags = 
    main_image = forms.ImageField(allow_empty_file=False, required=True)
    content = QuillFormField(required=True)
