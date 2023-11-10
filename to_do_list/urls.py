"""to_do_list URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from app.views import listar_tasks, criar_task,detalhe_task, atualizar_status, deletar_task
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.urls import path

schema_view = get_schema_view(
    openapi.Info(
        title="API TO-DO",
        default_version='v1',
        description="API De lista de tarefas",
        contact=openapi.Contact(email="ffrodrigues@inf.ufrgs.br"),
        license=openapi.License(name="Francielle Fernandes Rodrigues"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tasks/', listar_tasks, name='lista_tasks'),  
    path('tasks/create/', criar_task, name='criar_task'),  
    path('tasks/<int:task_id>/', detalhe_task, name='detalhe_task'),
    path('tasks/<int:task_id>/update/', atualizar_status, name='atualizar_status'),
    path('tasks/<int:task_id>/delete/', deletar_task, name='deletar_task'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),  # Alternativa de interface de OPEN API


]
