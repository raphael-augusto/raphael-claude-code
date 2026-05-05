---
name: sql-refactor
description: Refactor and optimize SQL Server queries — CROSS APPLY, CTEs, derived columns, engine detection, comments and readability.
---

You are using the **sql-expert** agent.

## Detect SQL Engine

Before refactoring, identify the engine from keywords:

- **SQL Server** → `CROSS APPLY`, `OUTER APPLY`, `TRY_CONVERT`, `GETDATE()`, `DATEADD`, `dbo.`, `ISNULL(`, `TOP`
- **BigQuery** → `` `project.dataset.table` ``, `PARTITION BY DATE(`, `CLUSTER BY`, `ARRAY`, `STRUCT`, `UNNEST`, `SAFE_CAST`
- **Snowflake / Databricks** → route to `data-engineer-expert`
- **Ambiguous** → ask the user

## SQL Server Refactor Goal

Transform the provided query to:

1. Use `CROSS APPLY` (or `OUTER APPLY`) to centralize all calculations, type conversions, and reusable expressions into named derived columns
2. Use CTEs (`WITH`) to separate logical steps when > 1 step needed
3. Keep the final `SELECT` clean — reference only derived names
4. Add comments: `--` on each CTE purpose, each main table in FROM/JOIN, each calculated column
5. Consistent indentation (4 spaces), each clause on its own line

**When user provides raw business rules (no query):**
1. Build a KISS base query first
2. Then move calculations into CROSS APPLY

**When user provides existing query:**
1. Identify repeated or complex expressions
2. Move them into CROSS APPLY with clear aliases
3. Preserve original logic exactly

## BigQuery Refactor Goal

Use CTEs to separate logical steps. No CROSS APPLY (not supported). Use `SAFE_CAST` for external data.

## Output

Complete query ready to run, with CROSS APPLY/CTEs, comments and simple formatting.

$ARGUMENTS
