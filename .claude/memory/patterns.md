---
name: Padroes Tecnicos Validados
description: Padroes de codigo e engenharia validados pelo usuario para uso consistente no projeto
type: feedback
last_updated: 2026-05-05
---

## Como usar

Consultar antes de gerar codigo ou arquitetura. Se identificar padrao novo recorrente → sugerir adicao aqui.

## Formato de entrada

```
### [DOMINIO] — [nome curto]
- Padrao: [descricao tecnica]
- Contexto: [quando aplicar]
- Exemplo: [snippet ou comando]
```

---

## SQL

### SQL — Sem SELECT *
- Padrao: Sempre listar colunas explicitamente
- Contexto: Qualquer query em producao

### SQL — CTEs para complexidade
- Padrao: Queries complexas usam CTEs, nao subqueries aninhadas
- Contexto: Mais de 1 nivel de agregacao ou join

### SQL — CROSS APPLY (SQL Server)
- Padrao: Usar CROSS APPLY para expressoes derivadas complexas
- Contexto: SQL Server T-SQL — substituir subquery correlacionada

### SQL — BigQuery FROM qualificado
- Padrao: Sempre especificar `project.dataset.table` no FROM
- Contexto: BigQuery — evitar ambiguidade de dataset

### SQL — Particionamento obrigatorio BigQuery
- Padrao: Toda tabela BigQuery deve ter partition por data
- Contexto: Criacao de tabelas analiticas — custo e performance

---

## Python / PySpark

### Python — Spark em producao
- Padrao: Spark/PySpark para grandes volumes — evitar Pandas em producao
- Contexto: Datasets > 1M linhas ou pipelines distribuidos

### Python — Funcoes puras em ETL
- Padrao: Preferir funcoes puras e sem estado
- Contexto: Transformacoes ETL — facilita teste e idempotencia

### Python — Nomeacao
- Padrao: snake_case para Python, UPPER_CASE para constantes SQL
- Contexto: Todo codigo novo

### Python — Logs estruturados
- Padrao: JSON para logs em producao
- Contexto: Todo pipeline com execucao em producao
- Exemplo: `logging.info(json.dumps({"pipeline": name, "run_id": id, "status": "ok"}))`

---

## Idempotencia

### Pipeline — Idempotencia obrigatoria
- Padrao: Mesma entrada deve gerar mesma saida
- Contexto: Todo pipeline ETL/ELT

### Pipeline — MERGE com chave unica
- Padrao: Usar MERGE/UPSERT com chave de negocio — nunca INSERT simples
- Contexto: Carga incremental em qualquer banco

### Pipeline — Timestamps de rastreabilidade
- Padrao: Incluir `processed_at`, `run_id` em toda carga
- Contexto: Silver e Gold layers

---

## Error Handling

### Retry — Exponential backoff
- Padrao: 3 tentativas com delay 2^n segundos (2s, 4s, 8s)
- Contexto: Chamadas a APIs externas e operacoes de rede

### Retry — Erro transitorio vs permanente
- Padrao: Retry apenas para erros transitorios (timeout, throttle) — fail fast para permanentes (schema error, auth)
- Contexto: Todo client de API ou conector de banco

---

## Testes

### Testes — Sem mock de banco em integracao
- Padrao: Testes de integracao devem usar banco real (ou container)
- Contexto: Integracao — mocks mascaram divergencia schema/prod
