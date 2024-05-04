from django import forms
from tracker.models import Task
from django.contrib.auth.models import User

class AddTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('time_spent', 'task',)
    
    def __init__(self, *args, **kwargs):
        super(AddTaskForm, self).__init__(*args, **kwargs)

        self.fields['time_spent'].label = ''
        self.fields['time_spent'].widget.attrs['class'] = 'form-control'
        self.fields['time_spent'].widget.attrs['placeholder'] = 'Time spent'
        self.fields['time_spent'].help_text = ''

        self.fields['task'].label = ''
        self.fields['task'].widget.attrs['class'] = 'form-control'
        self.fields['task'].widget.attrs['placeholder'] = 'Task'
        self.fields['task'].help_text = ''