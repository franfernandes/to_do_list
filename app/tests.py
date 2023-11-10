from django.test import TestCase

# Create your tests here.
from django.urls import reverse
from .models import Task

class TaskAPITestCase(TestCase):
    def setUp(self):
        self.task = Task.objects.create(titulo='Teste', descricao='Testes Unitarios para uma tarefa')

    def test_detalhe_task(self):
        response = self.client.get(reverse('detalhe_task', args=[self.task.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Teste')