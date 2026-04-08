---
name: Padroes Tecnicos Validados
description: Padroes de codigo e engenharia validados pelo usuario para uso consistente no projeto
type: feedback
---

- Usar Spark/PySpark para grandes volumes — evitar Pandas em producao
- Evitar SELECT * em todas as queries SQL
- Particionamento por data obrigatorio em tabelas BigQuery
- Preferir funcoes puras e sem estado em ETL
- Nomeacao snake_case para Python, UPPER_CASE para constantes SQL
- Queries complexas: usar CTEs, nao subqueries aninhadas
- BigQuery: sempre especificar dataset e projeto no FROM
- SQL Server: usar CROSS APPLY para expressoes derivadas complexas
- Logs estruturados (JSON) em todos os pipelines
- Testes unitarios com dados minimos — sem mocks de banco em integracao

**Why:** Padroes consolidados de qualidade, performance e manutencao.
**How to apply:** Aplicar automaticamente em qualquer geracao ou revisao de codigo no projeto.
