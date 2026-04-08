---
description: Detecta tipo de pipeline e chama skill/agent especializado para analise
---

Analise o pipeline fornecido pelo usuario e determine qual skill ou agent especializado deve ser usado:

## Deteccao de Tipo

**Airflow DAG** → usar skill `airflow-investigator`
- Detectar: `from airflow import DAG`, `@dag`, `PythonOperator`, `dag_id`

**PySpark/Databricks** → usar skill `pyspark-optimizer`
- Detectar: `from pyspark`, `spark.read`, `DataFrame`, `.withColumn`, `Databricks`

**dbt** → usar skill `dbt-reviewer`
- Detectar: `{{ ref(`, `{{ source(`, `dbt_project.yml`, `models/`, `.sql` com Jinja

**BigQuery SQL** → usar skill `bigquery-review`
- Detectar: `FROM \`project.dataset.table\``, `PARTITION BY`, `CLUSTER BY`

**SQL Server** → usar agent `sql-expert`
- Detectar: `CROSS APPLY`, `TRY_CONVERT`, `GETDATE()`, `dbo.`

**Medallion Architecture** → usar skill `medallion-validator`
- Detectar: mentions de `bronze`, `silver`, `gold`, `lakehouse`, estrutura de pastas

**Pipeline generico** → usar agent `data-engineer-expert`
- Default se nenhum padrão acima detectado

## Acao

1. Identifique o tipo baseado nas keywords acima
2. Chame o skill/agent correspondente com contexto completo
3. Se ambiguo, pergunte ao usuario qual tipo

$ARGUMENTS
