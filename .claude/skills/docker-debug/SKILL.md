---
name: docker-debug
description: Debuga e revisa containers Docker — Dockerfile, docker-compose, falhas de build/runtime, redes, volumes, registry e segurança.
tools: Read, Grep, Glob, Bash
---

# Docker Debug

Especialista em containers Docker. Debug de builds e runtime, review de Dockerfile e compose, foco em produção e segurança.

## Quando usar esta skill

Use quando o usuário:
- tiver build de imagem falhando
- tiver container com falha ao iniciar, crashando ou com comportamento inesperado
- quiser revisar Dockerfile para produção (tamanho, segurança, camadas)
- quiser debugar docker-compose (rede, volumes, dependências entre serviços)
- quiser configurar registry (push/pull, autenticação, tags)
- tiver problema de permissão, volume ou rede entre containers
- quiser reduzir tamanho de imagem ou otimizar cache de layers
- quiser configurar healthcheck ou limites de recursos

## Objetivo

Identificar causa do problema ou risco no Dockerfile/compose, propor menor correção segura e eficiente.

## Como agir

1. **Entender contexto**
   - Erro: build / runtime / rede / volume / registry?
   - Base image atual?
   - Ambiente: dev local / CI/CD / produção (K8s, ECS, Cloud Run)?
   - `docker-compose` ou apenas `docker run`?

2. **Localizar arquivos relevantes**
   - `Dockerfile` (e variantes: `Dockerfile.dev`, `Dockerfile.prod`)
   - `docker-compose.yml`, `docker-compose.override.yml`
   - `.dockerignore`
   - `.env` ou `--env-file`
   - CI/CD que faz build/push

3. **Diagnóstico de build com falha**
   - Erro de `COPY` / `ADD`: arquivo não existe no contexto de build → checar `.dockerignore` e path
   - Erro de `RUN`: comando falhou → rodar `docker build --progress=plain` para ver output completo
   - Cache não aproveitado: `COPY requirements.txt` antes de `COPY .` para aproveitar layer cache
   - Base image não encontrada: tag errada ou registry sem autenticação

4. **Diagnóstico de container com falha**
   - `docker logs <container>` → checar stderr para erro real
   - `docker inspect <container>` → exit code, env vars, mounts
   - Exit code 1: erro da aplicação → checar logs
   - Exit code 137: OOMKill → aumentar `--memory` limit
   - Exit code 126/127: comando não encontrado → PATH errado ou binário ausente na imagem
   - Container para imediatamente: `CMD` incorreto ou processo não roda em foreground

5. **Diagnóstico docker-compose**
   - Serviço não sobe na ordem certa: `depends_on` sem `condition: service_healthy` não garante app pronta
   - Rede: serviços na mesma rede custom se comunicam por nome do serviço
   - Volume não persiste: bind mount com path relativo errado → usar path absoluto ou named volume
   - Conflito de porta: `ports: "8080:8080"` já em uso no host

6. **Boas práticas Dockerfile**

   **Multi-stage build (redução de tamanho)**
   - Stage `builder` com ferramentas de build
   - Stage final só com artefatos necessários
   - Imagens finais: `python:3.12-slim`, `node:20-alpine`, `distroless`

   **Cache de layers (ordem importa)**
   - Dependências antes do código (`COPY requirements.txt` → `RUN pip install` → `COPY .`)
   - Instruções que mudam raramente primeiro

   **Segurança**
   - `USER nonroot` ou criar usuário sem privilégio
   - Sem `sudo` ou `--privileged` sem necessidade
   - Sem credenciais em `ENV` ou `ARG` que ficam no histórico da imagem
   - `.dockerignore` excluindo `.env`, `.git`, `*.key`, `node_modules`
   - Base image com tag específica (não `:latest`)
   - Scan de vulnerabilidades: `docker scout` ou `trivy`

   **Tamanho**
   - `apt-get install` com `--no-install-recommends` e limpeza em um único `RUN`
   - `pip install --no-cache-dir`
   - `npm ci --only=production` (sem devDependencies)

7. **Registry**
   - Autenticação: `docker login <registry>` ou via `--password-stdin`
   - Tag semântica: `image:1.2.3` em prod (nunca `:latest`)
   - Multi-platform build: `docker buildx build --platform linux/amd64,linux/arm64`

## Formato da resposta

### Resumo do problema
### Causa raiz identificada
### Correção recomendada (com Dockerfile/compose corrigido quando aplicável)
### Impacto (tamanho, segurança, performance)
### Próximos passos

## Regras

- Não inventar causa sem evidência no Dockerfile, compose ou logs
- Citar arquivo e linha quando possível
- Não reescrever Dockerfile inteiro — corrigir apenas o necessário
- Priorizar: segurança > corretude > tamanho > performance de build

## Arquivo de apoio

Consulte sempre:
- `checklist.md`
