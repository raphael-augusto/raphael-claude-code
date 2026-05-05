# Cloud Architecture Review — Checklist

## Resiliência e HA
- [ ] Sem SPOF: componentes críticos com redundância (multi-zone ou multi-region)?
- [ ] Retry idempotente em todas as integrações críticas?
- [ ] DLQ configurado em filas/tópicos?
- [ ] Circuit breaker ou timeout em dependências externas?
- [ ] Backup com RTO/RPO definidos e testados?
- [ ] Failover documentado e testável?

## Segurança
- [ ] Sem recursos com acesso público sem justificativa?
- [ ] IAM com least privilege (sem `*` em actions ou resources)?
- [ ] Secrets em vault (Key Vault / Secret Manager / Secrets Manager)?
- [ ] Tráfego entre componentes criptografado (TLS)?
- [ ] Isolamento de ambiente (dev não acessa prod)?
- [ ] Audit logging habilitado em recursos críticos?
- [ ] Network: private endpoints onde possível?

## Custo
- [ ] Compute rightsized para o workload real?
- [ ] Serverless/auto-scaling onde carga é variável?
- [ ] Storage com lifecycle policy para dados frios/arquivados?
- [ ] Egress cross-region minimizado?
- [ ] Recursos de dev com auto-shutdown?
- [ ] Reserved capacity apenas para baseline estável?

## Observabilidade
- [ ] Logs estruturados (JSON) em todos os componentes?
- [ ] Métricas de latência, erro e throughput coletadas?
- [ ] Alertas configurados para SLO breach?
- [ ] Tracing distribuído para sistemas com múltiplos saltos?
- [ ] Dashboard de health disponível para oncall?

## Complexidade
- [ ] Cada componente resolve um problema real e necessário?
- [ ] Sem abstrações prematuras sem benefício demonstrado?
- [ ] Documentação de fluxo de dados atualizada?
- [ ] Runbook de operação existente?

## Dados
- [ ] Classificação de dados (PII, confidencial) mapeada?
- [ ] Retenção de dados definida e implementada?
- [ ] Backup de dados críticos em região separada?
- [ ] Sem dados de prod expostos em ambientes não-prod?
