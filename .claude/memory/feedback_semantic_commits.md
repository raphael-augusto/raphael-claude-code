---
name: Semantic Commits Obrigatorio
description: Todos os commits devem seguir Conventional Commits com type e descricao em portugues, sem scope
type: feedback
---

Todos os commits devem seguir o padrao Semantic Commits definido no CLAUDE.md.
Formato: `<type>: <descricao em portugues>`

**Why:** Manter historico git limpo, rastreavel e consistente. Commits vagos como "update" ou "add features" nao comunicam o que mudou.
**How to apply:** Antes de commitar, validar que a mensagem segue o formato. Rejeitar mensagens vagas. Sem scope — manter simples.
