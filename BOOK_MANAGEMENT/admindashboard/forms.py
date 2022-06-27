from django import forms

class BookForm(forms.Form):
    title = forms.CharField(label='Book title',max_length=50)
    author = forms.CharField(label='Book Author',max_length=50)
    category = forms.CharField(label='Category', max_length=20)