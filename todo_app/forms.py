from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['id','task', 'date']

        widgets = {
            'Task': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter task',
                
            }),

            'Deadline': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter deadline',
                
            })
        }