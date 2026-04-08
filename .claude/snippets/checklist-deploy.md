---
name: Checklist Pre-Deploy
description: Validacoes obrigatorias antes de deploy de pipelines em producao
type: checklist
---

## Codigo

- [ ] Codigo revisado (code review aprovado)
- [ ] Sem hardcoded credentials, tokens ou secrets
- [ ] Variaveis de ambiente usadas para configuracao
- [ ] Logs estruturados (JSON) implementados
- [ ] Error handling com retry e exponential backoff
- [ ] Idempotencia validada (reruns produzem mesmo resultado)
- [ ] Nomes de variaveis e funcoes claros (snake_case Python, UPPER_CASE constantes SQL)

## Testes

- [ ] Testes unitarios passando (cobertura minima 70%)
- [ ] Testes de integracao validados
- [ ] Smoke test em ambiente staging
- [ ] Validacao com dados de producao (sample)
- [ ] Teste de reprocessamento (backfill) validado
- [ ] Performance testada com volume esperado

## SQL / Queries

- [ ] Sem SELECT * em queries de producao
- [ ] Particoes e clustering configurados (BigQuery/Databricks)
- [ ] Queries validadas com EXPLAIN/dry run
- [ ] Indices criados em tabelas SQL Server
- [ ] CTEs usadas para queries complexas (legibilidade)
- [ ] CROSS APPLY usado em SQL Server para calculos derivados

## Dados

- [ ] Schema validado (tipos, nullability, constraints)
- [ ] Data quality checks implementados
- [ ] Deduplicacao de registros garantida
- [ ] Chave de negocio unica definida
- [ ] SCD Type 2 implementado se necessario
- [ ] Validacao de dados de entrada (formato, range, completude)

## Airflow / Orquestracao

- [ ] DAG testada em staging/dev
- [ ] Schedule e timezone validados
- [ ] Retries configurados (max 3 tentativas)
- [ ] Timeout definido para tasks
- [ ] Variables e Connections criadas em producao
- [ ] Dependencias de DAG corretamente mapeadas
- [ ] Email/Slack alerts configurados para falhas
- [ ] Pools configurados para controle de concorrencia

## Databricks

- [ ] Job cluster configurado (evitar all-purpose em prod)
- [ ] Autoscaling ativado (min/max workers definidos)
- [ ] Unity Catalog tables/views criadas
- [ ] Permissoes GRANT configuradas
- [ ] Delta Lake OPTIMIZE + VACUUM agendados
- [ ] Logs de job enviados para cloud storage
- [ ] Secrets em Azure Key Vault ou Databricks Secrets

## BigQuery

- [ ] Tabelas particionadas por data
- [ ] Clustering configurado (ate 4 colunas)
- [ ] Dataset e projeto especificados no FROM
- [ ] Custo estimado validado (dry run)
- [ ] Scheduled queries configuradas se necessario
- [ ] IAM permissions validadas
- [ ] Row-level security configurada se necessario

## Snowflake

- [ ] Warehouse dimensionado corretamente
- [ ] Auto-suspend e auto-resume configurados
- [ ] Transient tables usadas para staging
- [ ] Streams + Tasks configurados para CDC
- [ ] Resource monitor configurado (budget alert)
- [ ] RBAC e permissoes validadas

## Observabilidade

- [ ] Logs estruturados enviados para cloud logging
- [ ] Metricas de execucao monitoradas (duracao, bytes, custo)
- [ ] Alerts configurados (falha, SLA, custo)
- [ ] Data lineage rastreavel
- [ ] Dashboard de monitoramento criado
- [ ] Runbook documentado para troubleshooting

## Seguranca

- [ ] Least privilege aplicado (IAM, RBAC)
- [ ] Secrets em vault (Azure Key Vault, Secret Manager, Databricks Secrets)
- [ ] Dados sensiveis (PII) mascarados ou encriptados
- [ ] Conexoes via private endpoint/link quando possivel
- [ ] Audit logs habilitados
- [ ] Service accounts com permissoes minimas

## Documentacao

- [ ] README atualizado com descricao do pipeline
- [ ] Diagramas de fluxo atualizados
- [ ] Variaveis de ambiente documentadas
- [ ] Dependencias upstream/downstream mapeadas
- [ ] SLA e RTO/RPO definidos
- [ ] Contato de on-call definido

## Rollback e Contingencia

- [ ] Plano de rollback documentado
- [ ] Backup de tabelas criticas antes de deploy
- [ ] Processo de revert validado em staging
- [ ] Dead-letter queue configurada se necessario
- [ ] Monitoramento pos-deploy agendado (primeiras 24h)

## CI/CD

- [ ] Pipeline de CI/CD configurado
- [ ] Deploy automatizado via GitOps
- [ ] Ambientes dev/staging/prod separados
- [ ] Feature flags usadas se necessario
- [ ] Git tags criadas para release
- [ ] Deploy em horario de baixa demanda

## Aprovacao Final

- [ ] Tech lead aprovou
- [ ] Data governance validou compliance
- [ ] Change management ticket criado
- [ ] Stakeholders notificados sobre deploy
- [ ] Post-mortem template preparado (caso necessario)
