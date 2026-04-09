---
name: Semantic Commits Obrigatorio
description: Todos os commits devem seguir Conventional Commits com type, scope opcional e descricao em portugues
type: feedback
---

Todos os commits devem seguir o padrao Semantic Commits definido no CLAUDE.md.
Formato: `<type>(<scope>): <descricao em portugues>`

**Why:** Manter historico git limpo, rastreavel e consistente. Commits vagos como "update" ou "add features" nao comunicam o que mudou.
**How to apply:** Antes de commitar, validar que a mensagem segue o formato. Rejeitar mensagens vagas. Usar scopes para contexto quando a mudanca e especifica de um dominio.
