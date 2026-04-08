# Checklist - Medallion Validator

## Bronze
- Dados brutos preservados
- Sem transformacoes de negocio
- Schema original mantido
- Metadados de ingestao presentes
- Particao por data de ingestao
- Append-only (sem deletes)

## Silver
- Deduplicacao implementada
- Schema validado e enforced
- Data quality checks
- Tipos de dados corretos
- Nullability tratada
- SCD Type 2 se historico necessario
- Particao por data de negocio

## Gold
- Agregacoes por dominio de negocio
- Joins desnormalizados
- Metricas de negocio calculadas
- Otimizado para query (clustering/indexes)
- Documentacao de metricas
- SLA definido

## Geral
- Separacao clara de responsabilidades
- Lineage rastreavel (bronze → silver → gold)
- Idempotencia em todos pipelines
- Naming convention consistente
- Governanca (permissoes por camada)
