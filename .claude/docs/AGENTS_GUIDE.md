# Claude Agents & Commands — Full Documentation

Author: Raphael
Version: 2.0
Scope: Guia oficial para uso dos agentes personalizados do Claude

# 1. Overview

Este documento explica:

O que são os Agentes

O que são os Commands

Como ativar manualmente cada agente

Como os commands ativam automaticamente o agente certo

Quando usar cada um

Seu sistema Claude agora é composto por:

1 Super Agente (principal)

12 agentes especializados

Commands inteligentes que chamam automaticamente o agente ideal

Tudo baseado no modelo KISS, respostas diretas, português técnico e foco em produção.

# 2. Lista de Agentes

A seguir, uma descrição clara do propósito de cada agente.

## 2.1 ultimate-engineering-architect (SUPER AGENTE)

Função: Engenheiro master unificado para todo o ciclo:
Arquitetura, Data Engineering, Backend, Frontend, Cloud, Performance, Refatoração, Requisitos, Documentação, Pesquisa e Ensino.

Use quando:
Você quer uma resposta completa, rápida e precisa sobre QUALQUER área técnica.

Ativação manual:

/agent ultimate-engineering-architect

## 2.2 data-engineer-expert

Especialista em:

ETL/ELT

Databricks

Spark

SQL Server / BigQuery / PostgreSQL

Orquestração (Airflow, Functions, Jobs)

Otimização de queries

Ativação manual:

/agent data-engineer-expert

## 2.3 backend-architect

Arquitetura back-end com foco em:

APIs FastAPI / Node

Segurança

Escalabilidade

Integridade de dados

## 2.4 system-architect

Arquitetura de sistemas e aplicações:

Microservices

DDD

CQRS

Event-driven

Componentização

## 2.5 tech-stack-researcher

Compara tecnologias e ajuda a tomar decisões:

Multicloud

Ferramentas

Custos/benefícios

Alternativas técnicas

Benchmarks

## 2.6 performance-engineer

Especialista em identificar gargalos reais:

SQL lento

CPU alta

Lentidão em API

Performance Angular/Node

## 2.7 refactoring-expert

Refatora e melhora código sem mudar comportamento:

KISS

SOLID

Clean Code

Redução de complexidade

## 2.8 technical-writer

Documentação:

APIs

Guias

Tutoriais

Especificações

## 2.9 requirements-analyst

Transforma ideias vagas em requisitos:

PRDs

User stories

Critérios de aceitação

## 2.10 deep-research-agent

Pesquisa profunda e complexa:

Investigações técnicas

Comparações extensas

Sínteses de informação

## 2.11 learning-guide

Explica e ensina:

Conceitos

Código

Passo a passo

## 2.12 frontend-architect

Arquitetura:

Angular

React

UI escalável e acessível

## 2.13 security-engineer

Especialista em segurança:

Autenticação

Autorização

RBAC

Rate limiting

Validações

# 3. Como usar um Agente diretamente

Use o padrão:

/agent NOME_DO_AGENT
<mensagem>


Exemplos:

Arquitetura
/agent ultimate-engineering-architect
Desenhe a arquitetura para meu novo ETL no GCP.

SQL
/agent data-engineer-expert
Otimize essa query.

Documentação
/agent technical-writer
Crie a documentação da API de produtos.

Requisitos
/agent requirements-analyst
Transforme esse problema em requisitos funcionais.

# 4. Como usar Commands (automático)

Commands são “atalhos inteligentes”.

Você não precisa escolher o agente — ele já vem embutido.

## 4.1 Listagem completa (com agentes internos)
Command	Função	Agente acionado
/new-task	Analisar e planejar tarefa	ultimate-engineering-architect
/code-explain	Explicar código	ultimate-engineering-architect
/code-optimize	Otimizar código	ultimate-engineering-architect
/code-cleanup	Refatorar código	ultimate-engineering-architect
/feature-plan	Planejar nova feature	ultimate-engineering-architect
/lint	Ajustar lint e melhorias	ultimate-engineering-architect
/docs-generate	Criar documentação	technical-writer
/api-new	Criar nova API	ultimate-engineering-architect
/api-test	Gerar cenários de teste	ultimate-engineering-architect
/api-protect	Segurança de API	security-engineer
/component-new	Criar componente Angular/React	ultimate-engineering-architect
/page-new	Criar página	ultimate-engineering-architect
/etl-new	Criar pipeline ETL	data-engineer-expert
/sql-optimize	Otimizar SQL	data-engineer-expert
/lakehouse-model	Criar medallion architecture	data-engineer-expert
/types-gen	Gerar typings	ultimate-engineering-architect
/edge-function-new	Criar função Supabase	ultimate-engineering-architect
# 5. Quando usar Agente vs Command
Situação	Recomenda
Quer processo padronizado	Command
Quer controle total	/agent
Não sabe qual usar	ultimate-engineering-architect
# 6. Exemplos práticos (copiar e colar)
Backend + Cloud
/agent ultimate-engineering-architect
Monte a arquitetura FastAPI -> Azure Functions -> Databricks -> SQL.

Otimização SQL
/sql-optimize
Otimize essa query do BigQuery.

Criar ETL
/etl-new
Crie um pipeline que lê dados do SAP, processa e envia ao BigQuery.

Documentação
/docs-generate
Documente a API GET /orders com exemplos.

Refatorar código
/code-cleanup
Refatore esse arquivo Python para ficar KISS.

Pesquisa profunda
/agent deep-research-agent
Pesquise benchmarks reais entre Azure Functions vs Cloud Run.

# 7. Como Claude escolhe automaticamente um agente

Mesmo sem comando, o sistema entende:

SQL → data-engineer-expert

Arquitetura → ultimate

Segurança → security-engineer

Performance → performance-engineer

Documentação → technical-writer

Requisitos → requirements-analyst

# 8. Dica de ouro

Para 80% dos casos:

/agent ultimate-engineering-architect


É o agente que resolve tudo com a sua stack:

Python

FastAPI

Node

TS/Angular

SQL

Azure

GCP

AWS

Databricks

# 9. Estrutura recomendada de diretórios (opcional)
.claude/
  agents/
  commands/
  mcp/
    docs_server.py
    googleGCP.json
    python.json
    spark.json
    apachebeam.json
    sql.json
    databricks.json
  settings.json
docs/
  AGENTS_GUIDE.md   ← este arquivo
  ARCHITECTURE.md
  ETL_GUIDE.md

# 10. MCP Server — Consulta de Documentacoes

## 10.1 O que e

Servidor MCP local que consulta documentacoes oficiais de:
- Google Cloud Platform (BigQuery, Storage, Dataflow, Pub/Sub)
- Python (oficial, pandas, numpy)
- Apache Spark (PySpark, SparkSQL)
- Apache Beam (SDK Python, transforms)
- SQL Server (T-SQL, procedures, performance)
- Databricks (Unity Catalog, Delta Lake, Workflows)

## 10.2 Localizacao

```
.claude/mcp/docs_server.py
```

## 10.3 Ativacao

Reinicie o Claude Code no diretorio do projeto.
O servidor e carregado automaticamente via `.claude/settings.json`.

## 10.4 Ferramentas disponiveis

| Tool | Descricao | Exemplo |
|------|-----------|---------|
| `list_docs` | Lista todas as documentacoes | — |
| `get_doc` | Busca doc de tecnologia | `get_doc(tech="spark", topic="pyspark")` |
| `search_docs` | Busca termo nas docs | `search_docs(query="window function", tech="sql")` |

## 10.5 Tecnologias e topicos

| Tech | Topicos disponiveis |
|------|---------------------|
| `gcp` | bigquery, storage, dataflow, pubsub |
| `python` | official, pandas, numpy |
| `spark` | official, pyspark, sql |
| `beam` | official, python_sdk, transforms |
| `sql` | tsql, functions, procedures |
| `databricks` | official, unity_catalog, delta, sql |

## 10.6 Exemplos de uso

Listar docs:
```
list_docs
```

Buscar doc especifica:
```
get_doc tech=databricks topic=delta
```

Pesquisar termo:
```
search_docs query="partition by" tech=spark
```

## 10.7 Adicionar novas documentacoes

Edite o dicionario `DOCS` em `.claude/mcp/docs_server.py`:

```python
DOCS = {
    "nova_tech": {
        "topico1": "https://url-da-doc.com",
        "topico2": "https://outra-url.com",
    },
}
```

# 11. Fim da documentacao
