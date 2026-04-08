## Checklist - PySpark Optimizer

## Codigo
- `.collect()` / `.toPandas()` desnecessarios
- `.count()` usado multiplas vezes sem cache
- UDFs Python (lento) vs funcoes nativas ou Pandas UDF
- Cache/persist em DataFrames reutilizados
- Repartition vs coalesce usado corretamente
- SELECT * evitado
- Filtros aplicados cedo (predicate pushdown)

## Shuffle
- Joins com broadcast quando possivel (<10MB)
- Pre-particionamento antes de groupBy
- Skew join detectado e tratado (salt, AQE skew join)
- Reducao de shuffle stages desnecessarios
- Repartition apenas quando necessario

## Particionamento
- Numero de particoes adequado ao volume
- `spark.sql.shuffle.partitions` ajustado (nao 200 default)
- Coalesce usado para reduzir particoes pequenas
- Particao de escrita configurada (partitionBy)

## Performance
- AQE habilitado (`spark.sql.adaptive.enabled`)
- Broadcast join threshold ajustado
- Storage format otimizado (Parquet, Delta)
- Column pruning validado (leitura minima de colunas)
- Predicate pushdown validado (filtros antes de join)

## Configuracoes Spark
- Executor memory dimensionado
- Executor cores dimensionado
- Dynamic allocation configurado se necessario
- Driver memory suficiente para broadcast
- Compression codec configurado (snappy, zstd)

## Storage
- Formato Parquet ou Delta
- Compression habilitado
- Schema evolution configurado se necessario
- OPTIMIZE + ZORDER em Delta Lake agendados

## Producao
- Erro handling implementado
- Logs estruturados
- Metricas de execucao monitoradas
- Idempotencia validada
