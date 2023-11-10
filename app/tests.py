from django.test import TestCase
from django.urls import reverse
from .models import Task

class TaskAPITestCase(TestCase):
    def setUp(self):
        self.task = Task.objects.create(titulo='Teste', descricao='Testes Unitários para uma tarefa')
    
    ## Teste para Ler detalhes de uma tarefa específica
    def test_detalhe_task(self):
        response = self.client.get(reverse('detalhe_task', args=[self.task.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Teste')

    ## Teste para Criar uma nova tarefa
    def test_criar_task(self):
        task_data = {
            'titulo': 'Tarefa de teste',
            'descricao': 'Tarefa criada para teste',
            'status': False
        }

        response = self.client.post(reverse('criar_task'), data=task_data, follow=True)

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Tarefa de teste')
        self.assertTrue(Task.objects.filter(titulo='Tarefa de teste').exists())

    ## Teste para Atualizar status de uma tarefa
    def test_atualizar_status(self):
        response = self.client.post(reverse('atualizar_status', args=[self.task.id]))
        self.assertEqual(response.status_code, 302) 

        updated_task = Task.objects.get(id=self.task.id)
        self.assertNotEqual(self.task.status, updated_task.status)

        self.assertNotEqual(self.task.data_atualizacao, updated_task.data_atualizacao)

    ## Teste para Deletar uma tarefa
    def test_deletar_task(self):
        self.assertEqual(Task.objects.count(), 1)
        response = self.client.post(reverse('deletar_task', args=[self.task.id]))

        self.assertEqual(response.status_code, 302)  
        self.assertEqual(Task.objects.count(), 0)  

        self.assertRedirects(response, reverse('lista_tasks'))
