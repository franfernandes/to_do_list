from django.shortcuts import render, redirect,get_object_or_404
from .models import Task
from .forms import TaskForm
from django.views.decorators.cache import cache_page
from django.core.cache import cache
from django.utils import timezone 
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from .serializers import TaskSerializer

# Listar todas as tarefas
@cache_page(60)
@swagger_auto_schema(
    methods=['get'],
    operation_summary="Lista todas as tarefas",
    responses={200: 'OK'}
)
@api_view(['GET'])
@permission_classes([AllowAny])
def listar_tasks(request):
    if request.method == 'GET':
        tasks = Task.objects.all()
        return render(request, 'tarefas.html', {'tasks': tasks})

# Criar uma nova tarefa
@swagger_auto_schema(
    methods=['post'],
    operation_summary="Cria uma nova tarefa",
    request_body=TaskSerializer,
    responses={200: 'OK', 400: 'Bad Request'}
)
@api_view(['POST'])
@permission_classes([AllowAny])
def criar_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.save()
            cache.clear()
            return redirect('lista_tasks')
    else:
        form = TaskForm()
    return render(request, 'criar_tarefa.html', {'form': form})


# Exibir detalhes da tarefa
@cache_page(60)
def detalhe_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    cache.clear()
    return render(request, 'detalhes_task.html', {'task': task})

# Atualizar status da tarefa
def atualizar_status(request, task_id):
    task = get_object_or_404(Task, id=task_id)

    if request.method == 'POST':
        task.status = not task.status
        task.data_atualizacao = timezone.now()
        task.save()
    return redirect('lista_tasks')

# Deletar tarefa
def deletar_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)

    if request.method == 'POST':
        task.delete()
        cache.clear()
        return redirect('lista_tasks')

    return render(request, 'confirma_delete.html', {'task': task})
