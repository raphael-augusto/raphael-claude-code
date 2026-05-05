# Snowflake Optimizer — Checklist

## Custo de Warehouse
- [ ] `AUTO_SUSPEND = 60` configurado em todos os warehouses?
- [ ] `AUTO_RESUME = TRUE` ativo?
- [ ] Warehouse size adequado para o workload (XS para dev, S/M para batch, M/L para dbt pesado)?
- [ ] Multi-cluster apenas onde há concorrência real?
- [ ] Sem warehouse rodando fora de horário sem cron justificado?
- [ ] `WAREHOUSE_METERING_HISTORY` consultado para identificar picos de custo?

## Performance de Query
- [ ] `QUERY_HISTORY` com `BYTES_SCANNED` alto → pruning ineficiente?
- [ ] Clustering key alinhada com colunas de filtro mais frequentes?
- [ ] `SYSTEM$CLUSTERING_INFORMATION` consultado para tabelas lentas?
- [ ] Clustering apenas em tabelas > 1TB?
- [ ] `SEARCH OPTIMIZATION` para lookup de valor específico em tabelas grandes?
- [ ] `RESULT_CACHE` aproveitado em queries repetitivas sem mudança de dados?

## Tipos de Tabela
- [ ] Staging → `TRANSIENT` (sem fail-safe)?
- [ ] Dados temporários de sessão → `TEMPORARY`?
- [ ] Dados críticos com auditoria → `PERMANENT`?
- [ ] Tabelas de staging sem `FAIL_SAFE` para reduzir custo de storage?

## Streams + Tasks (CDC)
- [ ] `SYSTEM$STREAM_HAS_DATA` verificado antes de Task rodar?
- [ ] Task com warehouse adequado (não superprovisionado)?
- [ ] Schedule de Task correto (não rodando desnecessariamente)?
- [ ] `MERGE` no Task idempotente?
- [ ] Stream `APPEND_ONLY` quando só há inserts?
- [ ] Error handling na Task (notificação em falha)?

## Snowpipe
- [ ] Stage separado para error files?
- [ ] `COPY_OPTIONS (ON_ERROR = CONTINUE)` para dados sujos?
- [ ] Monitoramento via `COPY_HISTORY`?

## Snowpark
- [ ] Snowpark Python em vez de Stored Procedure JavaScript?
- [ ] Sem `.collect()` em DataFrames grandes?
- [ ] DataFrame API preferida sobre SQL string dinâmico onde possível?

## Segurança e Governança
- [ ] Sem credenciais hardcoded em scripts?
- [ ] `SCIM` ou SSO configurado?
- [ ] RBAC com roles bem definidas (não ACCOUNTADMIN para aplicações)?
- [ ] Network Policy restringindo acesso por IP onde aplicável?
