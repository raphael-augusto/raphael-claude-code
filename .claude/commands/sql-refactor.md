---
name: sql-refactor
description: Refactor SQL Server queries using CROSS APPLY, derived columns, clear conversions, and comments for readability.
---

You are using the **sql-server-expert** agent.

Goal:
Refactor the provided SQL Server query to:
- Use CROSS APPLY (or OUTER APPLY when needed) to centralize calculations and conversions.
- Split complex expressions into well-named derived columns.
- Improve readability with simple, consistent indentation.
- Add meaningful comments to tables, CTEs, and calculated columns.
- Optionally use CTEs (WITH) or temporary tables when they improve clarity.

When the user pastes a query:
1. Rewrite the query using the agreed coding standards:
   - SELECT columns on separate lines with simple indentation.
   - CROSS APPLY for grouped calculations/conversions.
   - CTEs when helpful to separate logical steps.
2. Add comments explaining:
   - Purpose of each CTE or temp table.
   - Role of each main table in FROM/JOIN.
   - Meaning of each calculated/derived column.
3. Keep changes KISS: do not over-engineer or over-format.

Ask for clarification only if absolutely necessary (e.g., missing aliases or ambiguous intent).
