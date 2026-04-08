---
description: Detecta engine SQL e otimiza query automaticamente
---

Analise a query fornecida pelo usuario e determine qual engine SQL esta sendo usado:

## Deteccao de Engine

**BigQuery** → usar skill `bigquery-review`
- Detectar: ` \`project.dataset.table\` `, `PARTITION BY DATE(`, `CLUSTER BY`, `ARRAY`, `STRUCT`, `UNNEST`, `SAFE_CAST`

**SQL Server** → usar agent `sql-expert`
- Detectar: `CROSS APPLY`, `OUTER APPLY`, `TRY_CONVERT`, `GETDATE()`, `DATEADD`, `dbo.`, `ISNULL(`, `TOP`

**Snowflake** → usar agent `data-engineer-expert` (Snowflake section)
- Detectar: `FLATTEN`, `LATERAL FLATTEN`, `VARIANT`, `TIME_TRAVEL`, `SHOW`, `$1`, `METADATA$`

**Databricks SQL** → usar skill `bigquery-review` (similar syntax)
- Detectar: `delta.`, `OPTIMIZE`, `ZORDER`, `MERGE INTO`, `VACUUM`

**PostgreSQL** → usar agent `sql-expert`
- Detectar: `LATERAL`, `::`, `RETURNING`, `JSONB`, `pg_`

## Acao

1. Identifique o engine baseado nas keywords acima
2. Chame o skill/agent correspondente
3. Se ambiguo, pergunte ao usuario qual engine
4. Otimize para performance, custo e legibilidade

$ARGUMENTS
