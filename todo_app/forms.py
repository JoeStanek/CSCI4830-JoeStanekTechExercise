from django import forms
from .models import contact

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['id','Task']

        widgets = {
            'Task': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter task',
            })
        }