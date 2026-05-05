---
name: sql-refactor
description: Refatora SQL Server T-SQL para legibilidade, performance e padronizacao — CROSS APPLY, CTEs, aliases, remocao de subconsultas correlacionadas.
tools: Read, Edit, Write, Grep, Glob
---

# sql-refactor

Refatoracao SQL Server T-SQL. KISS. Zero redundancia. Zero subconsulta correlacionada desnecessaria.

---

## Quando Usar

- Query com subconsultas correlacionadas no SELECT ou WHERE
- Logica repetida em multiplos lugares da query
- Query ilegivel por ausencia de CTEs ou aliases
- OUTER APPLY / CROSS APPLY necessario para latest-per-group
- Coluna derivada reutilizada sem nome explicito

---

## Processo

1. Ler query original
2. Identificar subconsultas → candidatos a CTE ou CROSS APPLY
3. Nomear CTEs por responsabilidade (`cte_vendas_mes`, `cte_ultimo_pedido`)
4. Converter subconsultas correlacionadas em CROSS APPLY quando retornam linha unica por join
5. Extrair colunas calculadas repetidas para CTE ou CROSS APPLY alias
6. Validar: output identico, plano de execucao nao piorado

---

## Padroes

### CROSS APPLY — latest-per-group
```sql
-- Antes
SELECT c.id, (SELECT TOP 1 p.valor FROM pedidos p WHERE p.cliente_id = c.id ORDER BY p.data DESC) AS ultimo_valor
FROM clientes c

-- Depois
SELECT c.id, ult.valor AS ultimo_valor
FROM clientes c
CROSS APPLY (
    SELECT TOP 1 p.valor
    FROM pedidos p
    WHERE p.cliente_id = c.id
    ORDER BY p.data DESC
) ult
```

### CTE — logica reutilizada
```sql
WITH vendas_mes AS (
    SELECT cliente_id, SUM(valor) AS total, COUNT(*) AS qtd
    FROM pedidos
    WHERE data >= DATEADD(MONTH, -1, GETDATE())
    GROUP BY cliente_id
)
SELECT c.nome, vm.total, vm.qtd
FROM clientes c
JOIN vendas_mes vm ON vm.cliente_id = c.id
```

### CROSS APPLY — coluna calculada reutilizada
```sql
SELECT o.id, calc.margem, calc.margem * 0.1 AS comissao
FROM orders o
CROSS APPLY (SELECT (o.receita - o.custo) AS margem) calc
```

---

## Regras

- Nomes de CTE descritivos em `snake_case`
- CROSS APPLY para row-returning subqueries (1 linha por driver)
- OUTER APPLY quando resultado pode ser NULL (LEFT JOIN semantics)
- Sem alias generico (`x`, `t1`, `sub`) — nome deve refletir conteudo
- Nunca reescrever logica de negocio — apenas estrutura
- Se query for BigQuery/Snowflake: usar CTEs apenas (sem CROSS APPLY)
