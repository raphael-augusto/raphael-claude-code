# Checklist - SQL Server Performance

## Query
- SELECT *
- DISTINCT desnecessário
- ORDER BY necessário
- Conversão implícita
- Funções em predicado
- OR excessivo
- EXISTS / IN apropriado
- JOIN correto
- Cardinalidade controlada

## Performance
- Índice existente
- Índice faltando
- Predicado sargável
- Agregação eficiente
- CROSS APPLY útil
- Temp table necessária
- Table variable adequada
- Parameter sniffing possível

## Operação
- Locking
- Blocking
- Volume alto
- Compatibilidade com procedure/view
- Risco de regressão