---
name: Decisoes de Arquitetura
description: Decisoes tecnicas relevantes tomadas no projeto — stack, padroes, ferramentas escolhidas
type: project
last_updated: 2026-05-05
---

## Como usar

Consultar antes de sugerir ferramentas ou arquiteturas. Nao propor substituicoes sem justificativa clara.
Se uma nova decisao relevante for tomada → sugerir adicao aqui.

## Formato de entrada

```
### [AREA] — [decisao]
- Decisao: [o que foi decidido]
- Alternativa rejeitada: [o que foi descartado, se aplicavel]
- Motivo: [por que essa escolha]
```

---

## Stack Principal

### Cloud — GCP como cloud primaria
- Decisao: GCP e a cloud principal
- Servicos em uso: BigQuery, Cloud Composer, Cloud Functions, Cloud Run, GCS, Pub/Sub, Dataflow, IAM, Secret Manager
- Alternativa rejeitada: AWS como primaria

### Banco — BigQuery como analitico primario
- Decisao: BigQuery e o banco analitico primario
- Motivo: Custo-beneficio, integracao nativa GCP, SQL sem servidor

### Banco — SQL Server para OLTP
- Decisao: SQL Server para cargas transacionais
- Contexto: Sistemas operacionais legados e integracao com ecossistema Microsoft

### Linguagem — Python como padrao
- Decisao: Python para pipelines, scripts, APIs e automacao
- Alternativa rejeitada: Scala para Spark (complexidade desnecessaria)

### API — FastAPI para criacao
- Decisao: FastAPI para APIs Python
- Alternativa rejeitada: Flask (sem tipagem nativa), Django (overhead)

---

## Arquitetura de Dados

### Arquitetura — Medallion (Bronze/Silver/Gold)
- Decisao: Medallion com Clean Architecture e DDD
- Motivo: Separacao clara de responsabilidades, rastreabilidade de dados

### ETL — ELT preferido
- Decisao: ELT quando destino suporta transformacao nativa (BigQuery, Databricks)
- Alternativa rejeitada: ETL com transformacao no pipeline (custo de compute desnecessario)

### Orquestracao — Airflow (Cloud Composer)
- Decisao: Apache Airflow via Cloud Composer no GCP
- Alternativa rejeitada: Prefect, Dagster (nao adotados no projeto)

---

## Desenvolvimento

### CI/CD — Git com pipelines declarativos
- Decisao: CI/CD via Git (GitHub Actions ou equivalente)
- Motivo: Rastreabilidade, revisao de codigo, rollback facil

### Infra — IaC obrigatorio para recursos cloud
- Decisao: Todo recurso cloud deve ter representacao em Terraform
- Motivo: Reproducibilidade, auditoria, disaster recovery
