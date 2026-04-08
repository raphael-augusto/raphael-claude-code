---
name: Git Branch - Sempre usar dev
description: Todo trabalho deve ser feito na branch dev, nunca commit direto em main ou prod
type: feedback
---

Sempre trabalhar na branch dev. Nunca fazer commit ou push direto em main ou prod.

**Why:** Usuario quer proteger main/prod de alteracoes diretas, independente da estrutura de branching.
**How to apply:** Antes de commitar, verificar se esta em dev. Se nao estiver, fazer checkout para dev primeiro.
