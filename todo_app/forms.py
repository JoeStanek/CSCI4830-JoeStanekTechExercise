from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['id','task']

        widgets = {
            'Task': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter task',
            })
        }