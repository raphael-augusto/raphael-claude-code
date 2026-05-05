# ETL Design — Checklist

## Arquitetura ETL/ELT
- [ ] Fontes, destinos, frequência e volume identificados?
- [ ] Batch vs streaming vs híbrido definido?
- [ ] Separação clara extract / transform / load?
- [ ] Orquestrador escolhido (Airflow, Composer, MWAA, Step Functions)?
- [ ] Estrutura de pastas por domínio/camada definida?
- [ ] Configuração por ambiente (dev/staging/prod)?
- [ ] Secrets via vault (nunca hardcoded)?

## Operação
- [ ] Idempotência garantida em todos os pipelines?
- [ ] Retry com backoff implementado?
- [ ] DLQ ou tratamento de falha definido?
- [ ] Reprocessamento seguro (sem duplicidade)?
- [ ] Logs estruturados (JSON)?
- [ ] Alertas configurados?
- [ ] Governança e permissões por camada?

## Medallion Architecture (Bronze/Silver/Gold)

### Bronze
- [ ] Dados brutos preservados sem transformação de negócio?
- [ ] Schema original mantido?
- [ ] Metadados de ingestão presentes (`_ingestion_timestamp`, `_source_file`)?
- [ ] Partição por data de ingestão?
- [ ] Append-only (sem deletes)?

### Silver
- [ ] Deduplicação implementada?
- [ ] Schema validado e enforced?
- [ ] Data quality checks ativos?
- [ ] Tipos de dados corretos; nullability tratada?
- [ ] SCD Type 2 configurado se histórico necessário?
- [ ] Partição por data de negócio?

### Gold
- [ ] Agregações por domínio de negócio?
- [ ] Joins desnormalizados para analytics?
- [ ] Métricas de negócio calculadas?
- [ ] Otimizado para BI (clustering/indexes)?
- [ ] Documentação de métricas presente?
- [ ] SLA de freshness definido?

### Geral Medallion
- [ ] Lineage rastreável (bronze → silver → gold)?
- [ ] Naming convention consistente entre camadas?
- [ ] Separação clara de responsabilidades entre camadas?
