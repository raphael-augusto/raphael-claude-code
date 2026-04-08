# Checklist - dbt Reviewer

## Estrutura
- Modelos em pastas staging/intermediate/marts
- Naming convention: stg_, int_, fct_, dim_
- One model per file
- {{ ref() }} usado (nao hardcoded tables)
- {{ source() }} usado para raw data

## SQL
- CTEs nomeadas e comentadas
- Sem SELECT *
- Filtros aplicados cedo
- Joins otimizados
- Window functions necessarias

## Materialization
- table para grandes agregacoes
- view para transformacoes leves
- incremental para append-only com merge
- ephemeral para CTEs reutilizaveis
- unique_key definida em incrementals
- partitioning configurado (BigQuery)

## Testes
- unique em chaves primarias
- not_null em colunas obrigatorias
- relationships em foreign keys
- accepted_values em enums
- testes customizados se necessario

## Documentacao
- schema.yml presente
- descriptions em models
- descriptions em columns criticas
- meta tags aplicadas
- lineage validado no DAG

## Performance
- Incremental models para grandes volumes
- Clustering configurado (BigQuery, Databricks)
- Indexes sugeridos (Snowflake, Postgres)
- Queries com EXPLAIN validadas
