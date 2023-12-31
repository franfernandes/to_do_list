from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['titulo', 'descricao', 'status']
        labels = {'titulo': 'Titulo da Tarefa', 'descricao': 'Descrição da tarefa'}
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Título da tarefa'}),
            'descricao': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Descrição da tarefa'}),
        }
