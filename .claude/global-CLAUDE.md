# Preferencias Pessoais — Raphael Augusto

## Estilo de Resposta
- Portugues tecnico, direto, sem introducoes
- Codigo primeiro, resumo de 1 linha depois
- Sem emojis, sem justificativas, sem teoria
- Otimize para menor uso de tokens

## Formato

Codigo:
```
# codigo
Resumo: <5 palavras>
```

Texto:
Uma frase objetiva.

## Regras Gerais
- Nao explique o que mudou, resuma
- Nao adicione features nao solicitadas
- Nao crie helpers para uso unico

## Semantic Commits (Obrigatorio)

Formato: `<type>: <descricao>`

Descricao em portugues, presente do indicativo, minuscula.

### Types
| Type | Quando usar |
|------|-------------|
| `feat` | Nova feature para o usuario |
| `fix` | Correcao de bug |
| `docs` | Alteracao em documentacao |
| `style` | Formatacao, sem mudanca de logica |
| `refactor` | Refatoracao sem mudar comportamento |
| `test` | Adicao ou ajuste de testes |
| `chore` | Tarefas de build, config, CI, deps |

### Exemplos
```
feat: adiciona particionamento por data na tabela orders
fix: corrige timeout no dag de ingestao
docs: atualiza lista de agents no CLAUDE.md
refactor: simplifica transformacao bronze-to-silver
chore: atualiza versao do terraform no pipeline
feat!: migra autenticacao para oauth2
```

### Regras
- Nunca commit vago ("update", "fix", "ajuste", "add novas features")
- Descricao deve explicar O QUE foi feito, nao COMO
- Maximo 72 caracteres na primeira linha
- Nunca incluir Co-Authored-By: Claude nos commits
- Nunca incluir footer "Generated with Claude Code" em PR body

## Caveman Mode

Plugin: JuliusBrussee/caveman. Ativo via startup hook toda sessao.

Se plugin ausente, instalar:
```bash
claude plugin marketplace add JuliusBrussee/caveman && claude plugin install caveman@caveman
```

Modo padrao: **ultra**. Trocar: `/caveman lite|full|ultra`.

| Level | Comportamento |
|-------|---------------|
| `lite` | Sem filler/hedging. Artigos mantidos. Profissional e direto |
| `full` | Sem artigos, fragmentos OK, sinonimos curtos. Caveman classico |
| `ultra` | Abreviacoes (DB/auth/fn/req/res), setas para causalidade (X→Y) |

Desativar: `stop caveman` ou `normal mode`.

Excecoes (escrever normal): avisos de seguranca, acoes irreversiveis, sequencias criticas de multiplos passos.

## Inicializacao automatica
Voce SEMPRE opera em **Ultra mode** do caveman (equivalente a /caveman:caveman Ultra mode ativo).
Ao iniciar esta sessao, execute os seguintes comandos em sequencia:
1. /caveman:caveman Ultra mode

**Nao pergunte se deve ativar esses modos — eles ja estao ativos por padrao.**


<!-- rtk-instructions v2 -->
# RTK (Rust Token Killer) - Token-Optimized Commands

## Golden Rule

**Always prefix commands with `rtk`**. If RTK has a dedicated filter, it uses it. If not, it passes through unchanged. This means RTK is always safe to use.

**Important**: Even in command chains with `&&`, use `rtk`:
```bash
# Wrong
git add . && git commit -m "msg" && git push

# Correct
rtk git add . && rtk git commit -m "msg" && rtk git push
```

## RTK Commands by Workflow

### Git (59-80% savings)
```bash
rtk git status && rtk git log && rtk git diff && rtk git add && rtk git commit && rtk git push && rtk git pull
```

### GitHub (26-87% savings)
```bash
rtk gh pr view <num> && rtk gh pr checks && rtk gh run list && rtk gh issue list
```

### Build & Test (70-99% savings)
```bash
rtk tsc && rtk lint && rtk next build && rtk vitest run && rtk playwright test && rtk test <cmd>
```

### Files & Search (60-75% savings)
```bash
rtk ls <path> && rtk grep <pattern> && rtk find <pattern>
```

### Analysis (70-90% savings)
```bash
rtk err <cmd> && rtk log <file> && rtk summary <cmd> && rtk diff
```

### Infrastructure (85% savings)
```bash
rtk docker ps && rtk docker logs <c> && rtk kubectl get && rtk kubectl logs
```

### Meta
```bash
rtk gain          # token savings stats
rtk discover      # missed RTK usage
rtk proxy <cmd>   # bypass filter (debug)
```

Overall average: **60-90% token reduction**.
<!-- /rtk-instructions -->
