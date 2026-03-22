# Checklist - BigQuery Review

## Query
- SELECT *
- DISTINCT desnecessário
- ORDER BY desnecessário
- Funções em colunas filtradas
- Filtros aplicados cedo
- JOIN correto
- Cardinalidade validada
- QUALIFY/ROW_NUMBER corretos
- UNNEST controlado

## Estrutura física
- Tabela particionada
- Coluna de partição adequada
- Clustering útil
- Tabela incremental
- Tabela intermediária necessária

## Custo
- Leitura de colunas mínima
- Scan de partições limitado
- Reprocessamento total evitado
- Dry run recomendado
- Tabelas muito grandes identificadas

## Produção
- Idempotência
- Duplicidade
- Tratamento de null
- Tratamento de cast
- Compatibilidade com pipeline