from django import forms

class CreateForm(forms.Form):
    name = forms.CharField(label='TODO', max_length=160)
    deadline = forms.DateTimeField()
    fortschritt = forms.IntegerField()