# SQL Refactor Checklist

## Pre-Refactor
- [ ] Query original copiada/preservada
- [ ] Output esperado documentado (colunas, cardinalidade)
- [ ] Engine confirmada: SQL Server / BigQuery / Snowflake

## Estrutura
- [ ] Subconsultas correlacionadas no SELECT → CROSS APPLY
- [ ] Subconsultas correlacionadas no WHERE → JOIN ou EXISTS
- [ ] Logica repetida 2x+ → CTE nomeada
- [ ] Colunas calculadas reutilizadas → CROSS APPLY alias ou CTE

## Naming
- [ ] CTEs nomeadas por responsabilidade (sem `cte_1`, `temp`, `sub`)
- [ ] Aliases descritivos (sem `x`, `t`, `a`, `b`)
- [ ] Aliases de tabela consistentes com abreviacao do nome

## SQL Server Especifico
- [ ] TOP 1 + ORDER BY dentro de CROSS APPLY (nao subconsulta)
- [ ] OUTER APPLY quando nullable (LEFT JOIN semantics)
- [ ] Sem SELECT * em CTEs intermediarias

## Validacao
- [ ] Output identico ao original (colunas + dados)
- [ ] Plano de execucao comparado (nao piorou)
- [ ] Sem logica de negocio alterada
