from django import forms
from .models import Post, UploadFiles

class NewPost(forms.ModelForm):
    class Meta:
        model = Post
        fields =  ('title', 'body','subject_name')

        widgets = {
            'title': forms.TextInput(attrs={
                'name':"post_title",
                'type':"text",
                'class':"form-control",
                'id':"exampleFormControlInput1",
                'placeholder':"Title",}),
            
            'body': forms.Textarea(attrs={
                'name':"post_text",
                'type':"text",
                'class':"form-control",
                'id':"exampleFormControlTextarea1",
                'placeholder':"Text",}),
        }

class NewPostUploads(forms.ModelForm):
    class Meta:
        model = UploadFiles
        fields =  ('file_upload',)

        widgets = {
            'file_upload': forms.ClearableFileInput(attrs={
                'name':"file",
                'type':"file",
                'multiple': True}),
        }
