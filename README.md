# Escola API

Bem-vindo à **Escola API**, uma API desenvolvida com [**Django Rest Framework**](https://www.django-rest-framework.org/) para gerenciar informações de uma escola. Esta API permite o gerenciamento de estudantes, cursos e matrículas. Desenvolvida para fins de estudo.

## Índice

- [Escola API](#escola-api)
  - [Índice](#índice)
  - [Recursos](#recursos)
  - [Instalação](#instalação)
  - [Configuração](#configuração)
  - [Uso](#uso)
  - [Autenticação](#autenticação)
  - [Rotas](#rotas)
    - [Alunos](#alunos)
    - [Cursos](#cursos)
    - [Matrículas](#matrículas)

## Recursos

A Escola API oferece os seguintes recursos:

- **Gerenciamento de Alunos**: Cadastro, atualização, listagem e remoção de estudantes.
- **Gerenciamento de Cursos**: Cadastro, atualização, listagem e remoção de cursos.
- **Gerenciamento de Matrículas**: Registro e listagem de matrículas de estudantes em cursos.

## Instalação

1. **Clone o repositório:**

    ```bash
    git clone https://github.com/seu-usuario/escola-api.git
    cd escola-api
    ```

2. **Crie um ambiente virtual:**

    ```bash
    python -m venv venv
    source venv/bin/activate  # No Windows use `venv\Scripts\activate`
    ```

3. **Instale as dependências:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Realize as migrações do banco de dados:**

    ```bash
    python manage.py migrate
    ```

5. **Inicie o servidor:**

    ```bash
    python manage.py runserver
    ```

## Configuração

- **Configurações de Banco de Dados**: As configurações do banco de dados podem ser ajustadas no arquivo `settings.py`.
- **Variáveis de Ambiente**: Utilize um arquivo `.env` para gerenciar variáveis de ambiente sensíveis, como chaves de API e credenciais do banco de dados.

## Uso

Para interagir com a API, você pode usar ferramentas como `curl`, `Postman`, `Insomnia`, ou qualquer cliente HTTP.

Exemplo de um body `Json` de criação de um estudante:

```
{
    "nome": "João Silva",
    "cpf": "12345678910",
    "data_nascimento": "2002-04-21"
}
```
## Autenticação

A API utiliza 'BasicAuthentication' do Django Rest Framework para autenticação. 

## Rotas
A comunicação com a API é feita através de Json objects.
### Alunos

- **GET /alunos/**: Lista todos os estudantes.
- **POST /alunos/**: Cria um novo estudante.
- **GET /alunos/{id}/**: Detalhes de um estudante específico.
- **PUT /alunos/{id}/**: Atualiza um estudante.
- **DELETE /alunos/{id}/**: Remove um estudante.

### Cursos

- **GET /cursos/**: Lista todos os cursos.
- **POST /cursos/**: Cria um novo curso.
- **GET /cursos/{id}/**: Detalhes de um curso específico.
- **PUT /cursos/{id}/**: Atualiza um curso.
- **DELETE /cursos/{id}/**: Remove um curso.

### Matrículas

- **GET /matriculas/**: Lista todas as matrículas.
- **POST /matriculas/**: Cria uma nova matrícula.
- **GET /matriculas/{id}/**: Detalhes de uma matrícula específica.
- **DELETE /matriculas/{id}/**: Remove uma matrícula.
- **GET /aluno/{id}/matriculas/**: Lista os cursos em que um determinado estudante está matriculado.
- **GET /curso/{id}/matriculas/**: Lista os alunos matriculados em um determinado curso.

Este projeto foi desenvolvido durante a formação [Django REST APIs: crie aplicações REST em Python](https://cursos.alura.com.br/formacao-django-rest) da Alura.

