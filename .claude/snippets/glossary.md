---
name: Glossario Tecnico
description: Termos e conceitos do dominio de engenharia de dados
type: reference
---

## Arquiteturas

**Medallion Architecture**
Padrao de organizacao de data lakehouse em 3 camadas:
- Bronze: dados brutos, sem transformacao
- Silver: dados limpos, deduplicados, com schema validado
- Gold: dados agregados, prontos para analytics e BI

**Clean Architecture**
Separacao de camadas com dependencias invertidas:
- Domain (regras de negocio puras)
- Application (use cases, orquestracao)
- Infrastructure (adapters, repositories, APIs externas)

**DDD (Domain-Driven Design)**
Modelagem focada no dominio de negocio com bounded contexts, aggregates, entities e value objects.

**ELT vs ETL**
- ETL: Extract → Transform → Load (transforma antes de carregar)
- ELT: Extract → Load → Transform (carrega bruto, transforma no destino)
- ELT preferido em BigQuery/Snowflake (processamento nativo)

---

## Conceitos de Dados

**CDC (Change Data Capture)**
Captura de mudancas incrementais em banco de dados (insert/update/delete).

**Idempotencia**
Propriedade de uma operacao que, executada multiplas vezes com mesma entrada, produz o mesmo resultado.

**Particionamento**
Divisao fisica de tabela em segmentos por coluna (ex: data) para otimizar scans e reduzir custo.

**Clustering**
Ordenacao co-localizada de dados em storage para melhorar pruning de leitura (BigQuery, Databricks).

**Schema Evolution**
Capacidade de alterar schema sem quebrar pipelines (adicionar colunas, mudar tipos com compatibilidade).

**Time Travel**
Consulta de versoes anteriores de dados em Delta Lake, BigQuery, Snowflake.

**ACID**
Atomicidade, Consistencia, Isolamento, Durabilidade — garantias transacionais de banco de dados.

---

## Databricks / Spark

**Delta Lake**
Camada de storage com ACID, schema enforcement, time travel sobre Parquet.

**Unity Catalog**
Metastore unificado com governanca, lineage, fine-grained access control.

**Auto Loader**
Ingestao incremental de arquivos de cloud storage com schema inference.

**DLT (Delta Live Tables)**
Framework declarativo para pipelines com data quality expectations.

**Photon**
Engine nativo C++ da Databricks para acelerar SQL e DataFrames.

**OPTIMIZE + ZORDER**
Compactacao de arquivos Delta + co-localizacao de dados por colunas especificas.

**VACUUM**
Limpeza de arquivos antigos alem do retention period em Delta Lake.

---

## BigQuery

**Particionamento por Ingestao**
Particao automatica por _PARTITIONTIME baseada em tempo de insercao.

**Particionamento por Coluna**
Particao customizada por coluna DATE/TIMESTAMP/INTEGER.

**Clustering**
Ordenacao de dados por ate 4 colunas para melhorar filtro.

**Slot**
Unidade de processamento paralelo no BigQuery.

**BI Engine**
Cache in-memory para queries rapidas em dashboards.

**Federated Query**
Consulta de dados externos (Cloud SQL, Spanner) sem mover para BigQuery.

---

## Airflow

**DAG (Directed Acyclic Graph)**
Grafo de tarefas com dependencias sem ciclos.

**Operator**
Unidade de trabalho atomica (PythonOperator, BigQueryOperator, etc).

**Sensor**
Operador que espera condicao externa (arquivo, tabela, datetime).

**XCom**
Mecanismo de troca de dados entre tasks (chave-valor).

**Pool**
Controle de concorrencia para limitar tasks paralelas.

**Backfill**
Reexecucao de DAG para periodos historicos.

**Catchup**
Execucao automatica de DAG runs perdidos entre start_date e now.

---

## Snowflake

**Virtual Warehouse**
Cluster de computacao separado de storage, escalavel independentemente.

**Zero-Copy Cloning**
Clonagem instantanea de tabela/schema sem duplicar dados.

**Time Travel**
Consulta de estado passado da tabela (ate 90 dias).

**Fail-safe**
Recuperacao de dados por Snowflake apos Time Travel (7 dias adicionais).

**Snowpipe**
Ingestao continua serverless de arquivos de cloud storage.

**Stream**
Objeto CDC que rastreia mudancas em tabela.

**Task**
Agendamento SQL nativo para pipelines.

**Materialized View**
View pre-computada e auto-mantida.

---

## Padroes de Pipeline

**Incremental Load**
Carregar apenas novos registros desde ultima execucao.

**Full Refresh**
Reprocessar todos os dados do zero.

**Upsert / Merge**
Atualizar se existe, inserir se nao existe (MERGE em SQL).

**SCD Type 2**
Slowly Changing Dimension com historico de mudancas (versoes temporais).

**Deduplicacao**
Remocao de duplicatas por chave de negocio usando QUALIFY ROW_NUMBER.

**Watermark**
Timestamp limite para processar eventos atrasados em streaming.

---

## Observabilidade

**Data Lineage**
Rastreamento de origem e transformacoes de dados.

**Data Quality**
Validacao de completude, unicidade, consistencia, formato.

**Monitoring**
Metricas de execucao: duracao, falhas, bytes processados, custo.

**Alerting**
Notificacao automatica de falhas ou violacoes de SLA.

**Tracing**
Rastreamento distribuido de requisicoes em sistemas.

---

## Seguranca

**Least Privilege**
Conceder apenas permissoes minimas necessarias.

**RBAC (Role-Based Access Control)**
Controle de acesso baseado em papeis.

**Column Masking**
Ocultacao dinamica de colunas sensiveis por politica.

**Row-Level Security**
Filtragem dinamica de linhas baseada em usuario/grupo.

**Service Account**
Identidade nao-humana para automacao (GCP, Azure).

**Managed Identity**
Identidade gerenciada pela cloud sem credenciais explicitas (Azure).

**Secret Manager**
Armazenamento seguro de credenciais e API keys.
