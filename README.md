# Lista de Tarefas em Django

## Descrição
Este é um aplicativo web simples para gerenciar tarefas. Ele permite que os usuários criem, visualizem, atualizem e excluam tarefas.

## Tecnologias Utilizadas
- Python
- Django
- HTML/CSS
- PostgreSQL
- Redis
  
## Instalação
1. Clone o repositório: `git clone https://github.com/franfernandes/to_do_list.git`
2. Instale as dependências: `pip install -r requirements.txt`
3. Execute as migrações do banco de dados: `python3 manage.py migrate`
4. Inicie o servidor local: `python3 manage.py runserver`

## Como Usar
1. Acesse a aplicação em http://localhost:8000/tasks/
2. Crie uma nova tarefa.
3. Visualize, atualize ou exclua tarefas conforme necessário.

## Open API

A documentação da API está disponível através do Swagger e do Redoc.
- Swagger UI: http://localhost:8000/swagger/
- Redoc: http://localhost:8000/redoc/
