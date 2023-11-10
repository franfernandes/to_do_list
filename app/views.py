from django.shortcuts import render, redirect,get_object_or_404
from .models import Task
from .forms import TaskForm
from django.views.decorators.cache import cache_page
from django.core.cache import cache

# Listar todas as tarefas
@cache_page(60)
def listar_tasks(request):
    if request.method == 'GET':
        tasks = Task.objects.all()
        return render(request, 'tarefas.html', {'tasks': tasks})

# Criar uma nova tarefa
def criar_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            cache.clear()
            return redirect('lista_tasks')
    else:
        form = TaskForm()
    return render(request, 'criar_tarefa.html', {'form': form})

# Exibir detalhes da tarefa
@cache_page(60)
def detalhe_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    return render(request, 'detalhes_task.html', {'task': task})

# Atualizar status da tarefa
def atualizar_status(request, task_id):
    task = get_object_or_404(Task, id=task_id)

    if request.method == 'POST':
        task.status = not task.status
        task.save()
        cache.clear()

    return redirect('detalhe_task', task_id=task.id)

#Deletar tarefa
def deletar_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)

    if request.method == 'POST':
        task.delete()
        cache.clear()
        return redirect('lista_tasks')

    return render(request, 'confirma_delete.html', {'task': task})