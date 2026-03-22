# Claude Agents — Guia Minimalista

## Agentes

| Agente | Quando usar |
|--------|-------------|
| `ultimate-engineering-architect` | **80% dos casos** — resolve tudo |
| `data-engineer-expert` | ETL, Spark, SQL, Databricks, GCP |
| `backend-architect` | APIs, seguranca backend |
| `security-engineer` | Auth, RBAC, validacoes |
| `technical-writer` | Documentacao |
| `performance-engineer` | Gargalos, otimizacao |
| `refactoring-expert` | Clean code, KISS |

**Ativacao:** `/agent NOME`

---

## Commands

| Command | Funcao |
|---------|--------|
| `/new-task` | Planejar tarefa |
| `/code-cleanup` | Refatorar |
| `/sql-optimize` | Otimizar SQL |
| `/etl-new` | Criar ETL |
| `/api-new` | Criar API |
| `/docs-generate` | Documentacao |

---

## MCP Docs

```
list_docs                           # Lista docs
get_doc tech=spark topic=pyspark    # Busca doc
search_docs query="join" tech=sql   # Pesquisa
```

**Techs:** gcp, python, spark, beam, sql, databricks

---

## Regra de Ouro

> Nao sabe qual usar? `/agent ultimate-engineering-architect`
