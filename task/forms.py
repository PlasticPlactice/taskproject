from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    last_day = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = Task
        fields = ('title', 'last_day', 'priority', 'status')
