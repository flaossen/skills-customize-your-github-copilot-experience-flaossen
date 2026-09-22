# 📘 Atividade: Building REST APIs com FastAPI

## 🎯 Objetivo

Aprenda a criar uma API REST em Python usando o framework FastAPI, definindo rotas HTTP, validando dados com modelos e organizando operações CRUD para um recurso simples.

## 📝 Tarefas

### 🛠️ Criar endpoints básicos

#### Descrição

Configure a aplicação FastAPI no arquivo inicial e crie endpoints para consultar a API e listar os itens disponíveis.

#### Requisitos

O programa concluído deve:

- Criar uma aplicação FastAPI na variável `app`.
- Implementar `GET /` retornando uma mensagem informando que a API está funcionando.
- Implementar `GET /tasks` retornando a lista de tarefas cadastradas.
- Iniciar corretamente com `uvicorn starter-code:app --reload`.
- Exibir a documentação interativa em `/docs`.

### 🛠️ Implementar operações CRUD

#### Descrição

Complete a API para permitir criar, consultar, atualizar e excluir tarefas usando os métodos HTTP apropriados.

#### Requisitos

O programa concluído deve:

- Implementar `POST /tasks` para criar uma tarefa.
- Implementar `GET /tasks/{task_id}` para consultar uma tarefa pelo identificador.
- Implementar `PUT /tasks/{task_id}` para atualizar uma tarefa existente.
- Implementar `DELETE /tasks/{task_id}` para excluir uma tarefa.
- Retornar status HTTP `404` quando o identificador não existir.
- Retornar a tarefa criada ou atualizada no corpo da resposta.

Exemplo de requisição:

```bash
curl -X POST http://127.0.0.1:8000/tasks \
  -H "Content-Type: application/json" \
  -d '{"title":"Estudar FastAPI","completed":false}'
```

### 🛠️ Validar dados da API

#### Descrição

Use modelos Pydantic para garantir que as tarefas recebam dados válidos e que as respostas sigam um formato consistente.

#### Requisitos

O programa concluído deve:

- Criar um modelo de entrada com um título obrigatório e não vazio.
- Definir `completed` como um campo booleano com valor padrão `False`.
- Validar o corpo das requisições automaticamente com Pydantic.
- Retornar erro de validação para requisições com título ausente ou vazio.
- Definir um modelo de resposta que inclua `id`, `title` e `completed`.
- Verificar pelo menos uma requisição válida e uma inválida na documentação `/docs` ou com `curl`.
