# raphael-claude-code

Configuracao pessoal do Claude Code para engenharia de dados — production-ready, cross-platform (Windows + Mac).

---

## Estrutura

```
.claude/
├── CLAUDE.md              # Contexto do projeto (stack, agents, skills, commands)
├── global-CLAUDE.md       # Preferencias pessoais (caveman, RTK, commits, estilo)
├── settings.json          # MCP servers, hooks, permissions versionadas
├── settings.local.json    # Permissions locais (nao versionado)
├── agents/                # Agents especializados
├── commands/              # Slash commands
├── skills/                # Skills por dominio
├── snippets/              # Templates de codigo prontos
├── memory/                # Memoria persistente entre sessoes
├── mcp/                   # MCP servers customizados
└── scripts/               # Scripts de automacao
```

---

## Setup em nova maquina

```bash
git clone https://github.com/raphael-augusto/raphael-claude-code
```

Abrir o projeto no Claude Code. O hook `sync-global.sh` sincroniza `global-CLAUDE.md` para `~/.claude/CLAUDE.md` automaticamente na primeira tool use. Zero passos manuais.

---

## Agents

| Agent | Especialidade |
|-------|--------------|
| `data-engineer-expert` | ETL/ELT, Spark, Airflow, Databricks, GCP, Snowflake, AWS |
| `sql-expert` | SQL Server T-SQL + BigQuery, CROSS APPLY, CTEs, performance |
| `cloud-solution-architect` | Azure, GCP, AWS, Kubernetes, networking, seguranca, custo |
| `orchestrator` | Coordena multiplos agents em tarefas complexas |
| `deep-research-agent` | Pesquisa tecnica profunda com evidencias |
| `tech-lead` | Code review, PR, mentoring, quality gate |
| `ci-cd-engineer` | CI/CD, GitOps, Terraform, DAB, containers |
| `critic-agent` | Validacao de saidas, quality gate, deteccao de inconsistencias |
| `model-router` | Seleciona modelo Claude por complexidade e impacto |
| `ultimate-engineering-architect` | Fallback generalista |

---

## Skills

| Skill | Dominio |
|-------|---------|
| `bigquery-review` | Review queries BQ (custo, performance, particionamento) |
| `airflow-investigator` | Falhas em DAGs Airflow/Composer |
| `pyspark-optimizer` | Performance PySpark/Spark (shuffle, cache, partitions) |
| `dbt-reviewer` | Review modelos dbt (SQL, testes, documentacao) |
| `medallion-validator` | Validacao Medallion Architecture (Bronze/Silver/Gold) |
| `etl-architecture` | Arquitetura ETL/ELT, Medallion, organizacao de pipelines |
| `gcp-function-debug` | Debug Cloud Functions e Cloud Run |
| `sqlserver-performance` | Performance tuning SQL Server T-SQL |

---

## Commands

| Comando | Funcao |
|---------|--------|
| `/analyze-pipeline` | Detecta tipo de pipeline e chama skill apropriada |
| `/optimize-query` | Detecta engine SQL e otimiza automaticamente |
| `/sql-refactor` | Refatora SQL com CROSS APPLY e CTEs |
| `/sql-cross-apply` | Converte expressoes complexas em CROSS APPLY |
| `/new-task` | Analisa complexidade e cria plano de implementacao |
| `/use` | Ativa qualquer agent pelo nome |

---

## Snippets

Templates prontos em `.claude/snippets/`:

| Arquivo | Conteudo |
|---------|----------|
| `airflow-dag-template.py` | DAG base com TaskFlow API |
| `bigquery-merge-incremental.sql` | Merge incremental BigQuery |
| `databricks-auto-loader.py` | Auto Loader com cloudFiles |
| `pyspark-bronze-to-silver.py` | Transformacao Medallion PySpark |
| `snowflake-stream-task.sql` | CDC com Streams+Tasks Snowflake |
| `logging-structured.py` | Logger JSON estruturado |
| `checklist-deploy.md` | Checklist pre-deploy |
| `glossary.md` | Glossario de termos do projeto |

---

## MCP Server

`docs-server` — consulta documentacao tecnica sem sair do Claude:

```
list_docs                          # lista todas as docs disponiveis
get_doc(tech, topic?)              # busca doc de uma tecnologia
search_docs(query, tech)           # busca termo em uma tecnologia
```

Tecnologias: `gcp`, `python`, `spark`, `beam`, `sql`, `databricks`, `airflow`

---

## Automacao (hooks)

**sync-global.sh** — sincroniza `global-CLAUDE.md` para `~/.claude/CLAUDE.md` em todo tool use.
- Pure bash, diff apenas, overhead < 1ms
- Cross-platform: Windows (Git Bash) e Mac

---

## Stack

Python · SQL Server · BigQuery · GCP · Azure · AWS · Databricks · Spark · PySpark · Apache Airflow · Snowflake · FastAPI · dbt · Delta Lake · Medallion Architecture
