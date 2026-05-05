# Databricks Optimizer — Checklist

## Cluster
- [ ] Job Cluster (ephemeral) em prod — não All-Purpose?
- [ ] Auto-scaling configurado com min/max workers adequados?
- [ ] Spot instances habilitadas onde tolerável?
- [ ] DBR version atualizada (LTS recomendado para prod)?
- [ ] SQL Warehouse: serverless para analytics ad-hoc, classic para carga previsível?

## Delta Live Tables
- [ ] Modo `triggered` vs `continuous` escolhido conscientemente (custo vs latência)?
- [ ] Expectations definidas para qualidade dos dados?
- [ ] Pipeline em modo `production` (não `development`) em prod?
- [ ] Event log consultado para falhas antes de qualquer outra análise?
- [ ] Tabelas de saída particionadas corretamente?

## Auto Loader
- [ ] Checkpoint path em storage persistente (GCS/ADLS/S3)?
- [ ] Schema explícito fornecido para dados sem schema confiável?
- [ ] `schemaEvolutionMode` configurado conforme necessidade?
- [ ] `maxFilesPerTrigger` ou `maxBytesPerTrigger` ajustado para latência?

## Unity Catalog
- [ ] Namespace correto: `catalog.schema.table`?
- [ ] External Location configurada para acesso a storage?
- [ ] Managed Identity / Service Principal sem credenciais em código?
- [ ] Permissões no nível mais específico possível (table > schema > catalog)?
- [ ] Managed vs External table: implicações de VACUUM/lifecycle consideradas?

## Delta Lake
- [ ] `OPTIMIZE + ZORDER` agendado para tabelas > 10GB?
- [ ] `VACUUM` com `retentionDuration >= 7 days`?
- [ ] CDF (Change Data Feed) habilitado para pipelines incrementais downstream?
- [ ] Liquid Clustering em tabelas com padrão de query variável?
- [ ] Time Travel testado para rollback de emergência?

## DAB (CI/CD)
- [ ] `run_as` com service principal em prod?
- [ ] Job Cluster definido por task (não All-Purpose)?
- [ ] `bundle validate` no pipeline antes de deploy?
- [ ] Targets dev/prod com hosts distintos?
- [ ] Secrets via Databricks Secret Scope (nunca hardcoded)?
