# GitHub Actions Debug — Checklist

## Trigger
- [ ] Evento correto: `push`, `pull_request`, `schedule`, `workflow_dispatch`?
- [ ] Branch filter correto: `branches: [main]` ou `branches-ignore`?
- [ ] Path filter causando bloqueio inesperado?
- [ ] Workflow file em `.github/workflows/` (não em subpasta)

## Jobs e Steps
- [ ] `needs:` correto entre jobs dependentes?
- [ ] `if:` condicional bloqueando execução indevidamente?
- [ ] `timeout-minutes` adequado para o job?
- [ ] `runs-on` correto (ubuntu-latest, windows-latest, self-hosted)?

## Actions e Versões
- [ ] Versões de actions fixas com SHA ou tag (não `@main`)?
- [ ] `actions/checkout@v4` presente como primeiro step?
- [ ] Actions customizadas com path correto em `uses:`?
- [ ] Actions deprecated ou removidas?

## Secrets e Variáveis
- [ ] Secrets referenciados existem no repo/org (Settings → Secrets)?
- [ ] `${{ secrets.VAR }}` vs `${{ env.VAR }}` usado corretamente?
- [ ] Variáveis de ambiente definidas no nível correto (job vs step)?
- [ ] Sem hardcode de credenciais em steps

## Permissões
- [ ] `permissions:` definido no nível correto (workflow ou job)?
- [ ] `contents: read`, `packages: write`, etc. conforme necessidade?
- [ ] GITHUB_TOKEN com escopo suficiente para a operação?

## Cache e Dependências
- [ ] `actions/cache` com key e restore-keys corretos?
- [ ] Hash do arquivo de lock incluso na cache key?
- [ ] Dependências instaladas antes do step que as usa?

## Segurança
- [ ] Sem `pull_request_target` com código não confiável
- [ ] Sem `${{ github.event.issue.title }}` em comandos shell (injection risk)
- [ ] OIDC para cloud auth (sem secrets de longa duração)?
