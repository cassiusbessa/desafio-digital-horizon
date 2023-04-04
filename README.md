# Desafio Digital Horizon

1 - Descreva o que é uma API RESTful e explique suas características:

- Uma API RESTful é tipo um garçom em um restaurante que sabe exatamente o que você quer e como quer. Ele sabe que se você pedir um prato de macarrão, ele deve trazer o prato de macarrão e não uma pizza. E assim como o garçom, a API sabe exatamente como trazer as informações que você precisa de forma organizada e estruturada.
  São, portanto, um conjunto de padrões e convenções de arquiteturas para criar e expor uma api na web. Suas caracteríscas incluem:
  Cliente-Server: separa o cliente do servido, sendo ambientes de desenvolvimento separados;
  Stateless: cada requisição é independente e autônoma e deve conter nela mesma todas as informações necessárias para ser processada;
  Cacheable: o servidor deve informar se a reposta pode ser cacheada ou não;
  Layered System: o sistema deve ser separado em camadas, de forma que cada camada tem responsabilidades específicas e se comunica apenas com as adjacentes;
  Uniform Interface: para facilitar o uso, as respostas devem ser uniformes e padronizadas;

# DecisionMake(Requisitos 2 a 8)

Para resolver os requisitos de 2 a 8, resolvi desenvolver uma api usando Conventional Commits, TDD, DDD, Clean Architecture e SOLID. Avaliando o prazo de entrega, julguei ser capaz de entregar um projeto desacoplado e bem estruturado e com grande cobertura de testes.
Para implementar o Clean Architecture com DDD, dividi o projeto em Domain(entidade e regras de negócio abstratas), Data(implementação das regras de negócio e protocolos do repositório), Infra (dependencias externas como libs, e banco de dados) Presentation(parte que irá externar a api). Ainda que Infra e Data possam em alguns casos estar juntos, eu gosto de separar para facilitar a visualização.
Como infra utilizei postgres como DB já que foi a stack pedido na vaga(imagino que seja a usada pelo time).
Para testar usei unittest já que ele é o mais recomendado para testar classes.

## Rodando a aplicação

Certifique-se que as portas 5432 e 5000 estão livres. Na pasta RAIZ da aplicação (não na src), rode os comandos após clonar o projeto:

```bash
$ docker compose up -d
```

Com esse comando você montará um container com o PostGres e subirá as tabelas para a db, para mais detalhes você pode conferir a arquivo Dockerfile e docker-compose na raíz do projeto.

```bash
$ bash startApp.bash
```

Esse comando rodará um script que instalará todas as dependencies necessárias para a execução da api, criará e ativará o ambiente venv e rodará a api na porta 5000. Você pode conferir o script na raiz do projeto.

## Princípios

- Single Responsibility Principle (SRP)
- Open Closed Principle (OCP)
- Liskov Substitution Principle (LSP)
- Interface Segregation Principle (ISP)
- Dependency Inversion Principle (DIP)
- Small Commits

> ## Design Patterns

- Factory
- Adapter
- Dependency Injection

> ## Metodologias e Designs

- TDD
- Clean Architecture
- DDD
- Conventional Commits
- Use Cases

> ## Bibliotecas e Ferramentas

- Python
- Flask
- Flake8
- Black
- Psycopg2
- asgiref
- pyjwt
- Unittest

## Melhorias

- Salvar o password do usuário criptografado;
- Corrigir alguns tipos inconsistentes;
- Testar o retorno das rotas;
- Também dockerizar a Api;

## Rotas

- Criar usuários: [POST] http://localhost:5000/users
  Endpoint para criar usuário, deve receber um json com os campos:
  fullname, email, password e retorna todos os dados do usuário criado

- [POST] http://localhost:5000/login
  Endpoint para validar as credencias do usuário. Deve receber um json com os campos email e password, então valida os campos, retornando, em caso de sucesso, todos os dados do usuário e um jwtToken.

- [GET] http://localhost:5000/users
  Endpoint que retornará todos os usuário cadastrados. É uma rota protegida e precisa receber em seu header no campo Authorization um token válido e então retornará todos os dados de todos os usuários.
