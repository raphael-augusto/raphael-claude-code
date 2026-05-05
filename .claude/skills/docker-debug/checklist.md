# Docker Debug — Checklist

## Dockerfile
- [ ] Base image com tag específica (não `:latest`)?
- [ ] Multi-stage build para reduzir tamanho da imagem final?
- [ ] Dependências copiadas antes do código (cache de layers)?
- [ ] `--no-install-recommends` em apt-get + limpeza no mesmo RUN?
- [ ] `--no-cache-dir` em pip install?
- [ ] `.dockerignore` configurado (`.env`, `.git`, `node_modules`, `*.key`)?
- [ ] `USER` não-root definido no Dockerfile?
- [ ] Sem credenciais em `ENV` ou `ARG` (ficam no histórico da imagem)?
- [ ] `HEALTHCHECK` definido para apps que precisam de readiness?

## Segurança
- [ ] Imagem escaneada por vulnerabilidades (docker scout / trivy)?
- [ ] Sem `--privileged` sem necessidade documentada?
- [ ] Sem `cap_add: ALL`?
- [ ] Sem secrets em variáveis de ambiente visíveis no inspect?
- [ ] Registry privado com autenticação configurada?

## docker-compose
- [ ] `depends_on` com `condition: service_healthy` para serviços que precisam estar prontos?
- [ ] Rede customizada definida (não usar rede default)?
- [ ] Named volumes para dados persistentes (não bind mounts em prod)?
- [ ] `restart: unless-stopped` em serviços de produção?
- [ ] `.env` file com valores reais fora do Git?
- [ ] Portas expostas apenas as necessárias?

## Runtime
- [ ] `--memory` e `--cpus` limits configurados?
- [ ] Logs com `--log-driver json-file --log-opt max-size=10m`?
- [ ] Exit code verificado (`docker inspect --format='{{.State.ExitCode}}'`)?

## Registry e Tags
- [ ] Tag semântica em prod (não `:latest`)?
- [ ] Multi-platform build quando necessário (linux/amd64, linux/arm64)?
- [ ] Autenticação via `--password-stdin` (não flag `-p`)?
