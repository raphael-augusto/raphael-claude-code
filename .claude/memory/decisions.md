---
name: Decisoes de Arquitetura
description: Decisoes tecnicas relevantes tomadas no projeto — stack, padroes, ferramentas escolhidas
type: project
---

- Stack principal: Python + SQL Server + BigQuery + GCP + Databricks + Spark/PySpark
- BigQuery e o banco analitico primario no momento (uso intenso, priorizar nas sugestoes)
- GCP e a cloud principal (uso completo: BigQuery, Cloud Composer, Cloud Functions, Cloud Run, GCS, Pub/Sub, Dataflow, IAM, Secret Manager)
- APIs: consome e cria APIs com Python (FastAPI para criacao, requests/httpx para consumo)
- Arquitetura: Medallion (Bronze/Silver/Gold) com Clean Architecture e DDD
- Orquestracao: Apache Airflow (Cloud Composer no GCP)
- Padrao de ETL: ELT preferido quando o destino suporta transformacao nativa (BigQuery, Databricks)
- CI/CD via Git com pipelines declarativos

**Why:** Decisoes alinhadas com o perfil tecnico do usuario e stack da empresa.
**How to apply:** Respeitar essas escolhas ao sugerir solucoes — nao propor substituicoes sem justificativa clara.
