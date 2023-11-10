from django.db import models

# Create your models here.

class Task(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    data_criacao = models.DateTimeField(auto_now_add=True,editable=False)
    data_atualizacao = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.titulo

    class Meta:
        app_label = 'app'  