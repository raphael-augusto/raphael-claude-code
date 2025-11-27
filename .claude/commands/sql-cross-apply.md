---
name: sql-cross-apply
description: Rewrite complex SQL Server expressions into CROSS APPLY blocks with clear derived columns and proper comments.
---

You are using the **sql-server-expert** agent.

Goal:
Given a SQL Server query or business rule, rewrite the logic so that:
- All complex calculations and conversions are grouped into one or more CROSS APPLY blocks.
- Each expression becomes a named derived column with a clear alias.
- The final SELECT is clean, referencing only the derived names.
- The code is easy to read, with:
  - Simple indentation.
  - Comments on tables, CTEs, and key calculated columns.

Steps:
1. If the user provides raw business rules (not a query yet):
   - First build a KISS base query.
   - Then move calculations/conversions into CROSS APPLY.
2. If the user provides an existing query:
   - Identify repeated or complex expressions.
   - Move these into CROSS APPLY with clear aliases.
3. Always:
   - Add comments (`--`) explaining intent of each major piece.
   - Prefer CTEs when multiple steps are needed.

Output:
- A complete T-SQL query ready to run in SQL Server.
- With CROSS APPLY, comments, and simple formatting.
