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

## Idempotencia
- Todo pipeline deve ser idempotente — mesma entrada gera mesma saida
- Usar MERGE/UPSERT com chave de negocio unica
- Delta Lake: usar merge com condicao ON para evitar duplicatas
- Validar se registro ja existe antes de inserir (WHERE NOT EXISTS)
- Usar timestamps de processamento para rastreabilidade

## Retry e Error Handling
- Implementar retry com exponential backoff
- Pattern: 3 tentativas com delays de 2^n segundos (2s, 4s, 8s)
- Sempre validar limites de retry para evitar loops infinitos
- Diferenciar erros transitorios (retry) de permanentes (fail fast)
- Registrar todas as tentativas em logs estruturados

## Logging Estruturado
- Sempre usar JSON para logs em producao
- Campos obrigatorios: timestamp, level, message, pipeline_name, run_id
- Incluir contexto: environment, user, source_table, target_table
- Nunca logar dados sensiveis (PII, credenciais)
- Exemplo Python: usar logging.info(json.dumps({...}))
- Exemplo Spark: usar logger com formato JSON padronizado

**Why:** Padroes consolidados de qualidade, performance e manutencao.
**How to apply:** Aplicar automaticamente em qualquer geracao ou revisao de codigo no projeto.
