# Claude Agents & Commands
## Guia Completo de Referencia

---

**Autor:** Raphael
**Versao:** 2.0
**Ultima atualizacao:** Janeiro 2026

---

## Sumario

1. [Visao Geral](#1-visao-geral)
2. [Arquitetura do Sistema](#2-arquitetura-do-sistema)
3. [Agentes Especializados](#3-agentes-especializados)
4. [Commands Inteligentes](#4-commands-inteligentes)
5. [MCP Server de Documentacao](#5-mcp-server-de-documentacao)
6. [Fluxos de Trabalho](#6-fluxos-de-trabalho)
7. [Referencia Rapida](#7-referencia-rapida)

---

## 1. Visao Geral

### O que e este sistema?

Um ecossistema de agentes IA especializados para engenharia de software, integrados ao Claude Code.

### Componentes

| Componente | Quantidade | Funcao |
|------------|------------|--------|
| Super Agente | 1 | Resolve 80% dos casos |
| Agentes Especializados | 12 | Dominios especificos |
| Commands | 17 | Atalhos inteligentes |
| MCP Server | 1 | Consulta documentacoes |

### Principios

- **KISS** — Simplicidade acima de tudo
- **Portugues tecnico** — Direto e limpo
- **Foco em producao** — Codigo pronto para deploy

---

## 2. Arquitetura do Sistema

```
┌─────────────────────────────────────────────────────────────┐
│                      CLAUDE CODE                             │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  ┌─────────────────────────────────────────────────────┐    │
│  │           ULTIMATE-ENGINEERING-ARCHITECT             │    │
│  │                   (SUPER AGENTE)                     │    │
│  │                                                      │    │
│  │  Arquitetura | Backend | Frontend | Data | Cloud     │    │
│  │  Performance | Refactoring | Docs | Research         │    │
│  └─────────────────────────────────────────────────────┘    │
│                            │                                 │
│              ┌─────────────┼─────────────┐                  │
│              ▼             ▼             ▼                  │
│  ┌──────────────┐ ┌──────────────┐ ┌──────────────┐        │
│  │    DATA      │ │   BACKEND    │ │   FRONTEND   │        │
│  │   ENGINEER   │ │   ARCHITECT  │ │   ARCHITECT  │        │
│  └──────────────┘ └──────────────┘ └──────────────┘        │
│                                                              │
│  ┌──────────────┐ ┌──────────────┐ ┌──────────────┐        │
│  │  PERFORMANCE │ │  REFACTORING │ │   SECURITY   │        │
│  │   ENGINEER   │ │    EXPERT    │ │   ENGINEER   │        │
│  └──────────────┘ └──────────────┘ └──────────────┘        │
│                                                              │
│  ┌──────────────┐ ┌──────────────┐ ┌──────────────┐        │
│  │  TECHNICAL   │ │ REQUIREMENTS │ │    DEEP      │        │
│  │    WRITER    │ │   ANALYST    │ │   RESEARCH   │        │
│  └──────────────┘ └──────────────┘ └──────────────┘        │
│                                                              │
│  ┌──────────────┐ ┌──────────────┐ ┌──────────────┐        │
│  │   SYSTEM     │ │   LEARNING   │ │ TECH STACK   │        │
│  │  ARCHITECT   │ │    GUIDE     │ │  RESEARCHER  │        │
│  └──────────────┘ └──────────────┘ └──────────────┘        │
│                                                              │
├─────────────────────────────────────────────────────────────┤
│                      MCP SERVER                              │
│  ┌─────────────────────────────────────────────────────┐    │
│  │  GCP | Python | Spark | Beam | SQL | Databricks     │    │
│  └─────────────────────────────────────────────────────┘    │
└─────────────────────────────────────────────────────────────┘
```

---

## 3. Agentes Especializados

### 3.1 ultimate-engineering-architect

> **O agente que resolve tudo.**

**Dominio:** Arquitetura, Data, Backend, Frontend, Cloud, Performance, Refatoracao, Requisitos, Documentacao, Pesquisa, Ensino

**Stack:** Python, FastAPI, Node, Angular, SQL, Azure, GCP, AWS, Databricks

**Ativacao:**
```
/agent ultimate-engineering-architect
```

---

### 3.2 data-engineer-expert

**Dominio:** ETL/ELT, Databricks, Spark, SQL Server, BigQuery, Airflow

**Ativacao:**
```
/agent data-engineer-expert
```

---

### 3.3 backend-architect

**Dominio:** APIs FastAPI/Node, Seguranca, Escalabilidade, Integridade

**Ativacao:**
```
/agent backend-architect
```

---

### 3.4 system-architect

**Dominio:** Microservices, DDD, CQRS, Event-driven

**Ativacao:**
```
/agent system-architect
```

---

### 3.5 performance-engineer

**Dominio:** SQL lento, CPU alta, API lenta, Gargalos

**Ativacao:**
```
/agent performance-engineer
```

---

### 3.6 refactoring-expert

**Dominio:** KISS, SOLID, Clean Code, Reducao de complexidade

**Ativacao:**
```
/agent refactoring-expert
```

---

### 3.7 security-engineer

**Dominio:** Autenticacao, Autorizacao, RBAC, Rate limiting

**Ativacao:**
```
/agent security-engineer
```

---

### 3.8 technical-writer

**Dominio:** APIs docs, Guias, Tutoriais, Especificacoes

**Ativacao:**
```
/agent technical-writer
```

---

### 3.9 requirements-analyst

**Dominio:** PRDs, User stories, Criterios de aceitacao

**Ativacao:**
```
/agent requirements-analyst
```

---

### 3.10 deep-research-agent

**Dominio:** Investigacoes tecnicas, Comparacoes, Sinteses

**Ativacao:**
```
/agent deep-research-agent
```

---

### 3.11 learning-guide

**Dominio:** Conceitos, Codigo, Passo a passo

**Ativacao:**
```
/agent learning-guide
```

---

### 3.12 frontend-architect

**Dominio:** Angular, React, UI escalavel

**Ativacao:**
```
/agent frontend-architect
```

---

### 3.13 tech-stack-researcher

**Dominio:** Comparacao de tecnologias, Benchmarks, Custos

**Ativacao:**
```
/agent tech-stack-researcher
```

---

## 4. Commands Inteligentes

### Tabela de Referencia

| Command | Funcao | Agente |
|---------|--------|--------|
| `/new-task` | Analisar e planejar tarefa | ultimate |
| `/code-explain` | Explicar codigo | ultimate |
| `/code-optimize` | Otimizar codigo | ultimate |
| `/code-cleanup` | Refatorar codigo | ultimate |
| `/feature-plan` | Planejar feature | ultimate |
| `/lint` | Ajustar lint | ultimate |
| `/docs-generate` | Criar documentacao | technical-writer |
| `/api-new` | Criar nova API | ultimate |
| `/api-test` | Gerar testes | ultimate |
| `/api-protect` | Seguranca de API | security-engineer |
| `/component-new` | Criar componente | ultimate |
| `/page-new` | Criar pagina | ultimate |
| `/etl-new` | Criar pipeline ETL | data-engineer |
| `/sql-optimize` | Otimizar SQL | data-engineer |
| `/lakehouse-model` | Medallion architecture | data-engineer |
| `/types-gen` | Gerar typings | ultimate |
| `/edge-function-new` | Criar funcao Supabase | ultimate |

---

## 5. MCP Server de Documentacao

### Ferramentas

| Tool | Descricao |
|------|-----------|
| `list_docs` | Lista documentacoes disponiveis |
| `get_doc` | Busca doc especifica |
| `search_docs` | Pesquisa termo nas docs |

### Tecnologias Suportadas

| Tech | Topicos |
|------|---------|
| `gcp` | bigquery, storage, dataflow, pubsub |
| `python` | official, pandas, numpy |
| `spark` | official, pyspark, sql |
| `beam` | official, python_sdk, transforms |
| `sql` | tsql, functions, procedures |
| `databricks` | official, unity_catalog, delta, sql |

### Exemplos

```
# Listar todas as docs
list_docs

# Buscar doc do Spark
get_doc tech=spark topic=pyspark

# Pesquisar termo
search_docs query="window function" tech=sql
```

---

## 6. Fluxos de Trabalho

### Fluxo 1: Novo ETL

```
1. /etl-new
2. Descreva origem, transformacao e destino
3. Receba pipeline pronto
```

### Fluxo 2: Otimizacao SQL

```
1. /sql-optimize
2. Cole a query
3. Receba versao otimizada
```

### Fluxo 3: Nova API

```
1. /api-new
2. Descreva endpoints
3. Receba codigo FastAPI/Node
```

### Fluxo 4: Documentacao

```
1. /docs-generate
2. Indique o codigo/API
3. Receba documentacao
```

---

## 7. Referencia Rapida

### Atalhos mais usados

```bash
# Tarefa generica
/agent ultimate-engineering-architect

# ETL/Data
/agent data-engineer-expert

# Seguranca
/agent security-engineer

# Documentacao
/docs-generate

# Otimizar SQL
/sql-optimize
```

### Estrutura de Diretorios

```
.claude/
├── agents/           # Definicoes dos agentes
├── commands/         # Commands personalizados
├── mcp/
│   ├── docs_server.py
│   ├── googleGCP.json
│   ├── python.json
│   ├── spark.json
│   ├── apachebeam.json
│   ├── sql.json
│   └── databricks.json
├── settings.json
└── docs/
    └── AGENTS_GUIDE.md
```

---

**Fim do Documento**

*Para converter em PDF: Use VS Code + Markdown PDF ou Pandoc*
