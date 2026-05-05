# AWS Data Debug — Checklist

## Glue
- [ ] Logs em CloudWatch `/aws-glue/jobs/error` consultados?
- [ ] DPU adequado para o workload (não superprovisionado)?
- [ ] Pushdown predicates habilitados para leitura do Glue Catalog?
- [ ] Job bookmarks configurados para jobs incrementais?
- [ ] Schema do Glue Catalog atualizado após mudanças?
- [ ] IAM role com acesso ao S3, Glue Catalog e KMS (se criptografado)?

## EMR Serverless
- [ ] Application em estado `STARTED` antes de submeter job?
- [ ] IAM execution role com acesso ao S3 e Glue Catalog?
- [ ] Logs em S3 configurados para debug?
- [ ] AQE habilitado (`spark.sql.adaptive.enabled=true`)?
- [ ] Driver/executor memory adequados para o volume de dados?

## Kinesis
- [ ] `GetRecords.IteratorAgeMilliseconds` monitorado (lag)?
- [ ] Shards suficientes para throughput (1MB/s write por shard)?
- [ ] Enhanced Fan-Out para múltiplos consumers?
- [ ] DLQ implementado via Lambda ou Firehose?
- [ ] Retention period adequado (padrão 24h, máx 365 dias)?

## Athena
- [ ] Formato Parquet/ORC (não CSV/JSON)?
- [ ] Partições definidas e filtro por partição no WHERE?
- [ ] Workgroup com limite de bytes por query?
- [ ] Result cache habilitado?
- [ ] `MSCK REPAIR TABLE` executado após novos dados particionados?

## Redshift
- [ ] Sort key alinhada com filtros frequentes?
- [ ] VACUUM e ANALYZE executados após cargas grandes?
- [ ] `COPY` command usado para cargas bulk (não INSERT individual)?
- [ ] `SVL_QUERY_REPORT` consultado para diagnóstico de skew?
- [ ] Redshift Serverless vs provisioned avaliado para o padrão de uso?

## Step Functions
- [ ] Retry com exponential backoff configurado por estado?
- [ ] Timeout por estado definido (evitar execução infinita)?
- [ ] DLQ ou state de fallback para falhas não recuperáveis?
- [ ] Execução consultada via `executionId` para erro exato?

## S3 / Storage
- [ ] Lifecycle policy configurada (IA após 30d, Glacier após 90d)?
- [ ] Particionamento por data no path?
- [ ] Versionamento habilitado apenas onde necessário (custo)?
- [ ] Requester Pays para dados compartilhados entre contas?

## IAM e Segurança
- [ ] Roles com least privilege (sem `s3:*` sem necessidade)?
- [ ] Sem credenciais hardcoded (usar IAM roles, não access keys)?
- [ ] KMS para dados sensíveis em S3, Redshift, Kinesis?
- [ ] VPC endpoints para Glue/S3 em ambientes privados?
