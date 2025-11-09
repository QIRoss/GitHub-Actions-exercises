# GitHub Actions com FastAPI

Este repositório demonstra um pipeline CI/CD completo usando GitHub Actions com FastAPI.

## Funcionalidades

- ✅ CI/CD com GitHub Actions
- ✅ Build de imagem Docker
- ✅ Testes automatizados com pytest
- ✅ Deploy automático para self-hosted runner
- ✅ FastAPI com endpoints REST

## Estrutura do Pipeline

1. **Testes**: Executa testes automatizados
2. **Build**: Constrói e faz push da imagem Docker para GitHub Container Registry
3. **Deploy**: Faz deploy automático na máquina Ubuntu com self-hosted runner

## Como usar

1. Clone o repositório
2. Configure o self-hosted runner na sua máquina Ubuntu
3. Faça push para o branch `main` para acionar o pipeline

## Endpoints

- `GET /` - Mensagem de boas-vindas
- `GET /health` - Health check da aplicação
- `GET /items` - Lista todos os items
- `GET /items/{id}` - Busca item por ID
- `POST /items` - Cria novo item