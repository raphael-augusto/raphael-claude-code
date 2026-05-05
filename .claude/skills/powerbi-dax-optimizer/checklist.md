# Power BI DAX Optimizer — Checklist

## Corretude
- [ ] Medidas usam agregacao (SUM, COUNT, etc.) — nao coluna direta?
- [ ] Contexto de filtro correto em cada `CALCULATE`?
- [ ] `RELATED()` usado apenas dentro de iterador (contexto de linha)?
- [ ] Relacionamentos inativos ativados com `USERELATIONSHIP` onde necessario?
- [ ] `DIVIDE` em vez de `/` para evitar erro de divisao por zero?
- [ ] Time intelligence com Date Table marcada?
- [ ] Sem circular dependency entre medidas?

## Performance
- [ ] `VAR` usado para evitar recalculo de expressao repetida?
- [ ] `FILTER` em tabela grande substituido por filtro direto em `CALCULATE`?
- [ ] Sem iteradores aninhados desnecessarios?
- [ ] `COUNTROWS(FILTER(...))` substituido por `CALCULATE(COUNTROWS(...), filtro)`?
- [ ] `IF` sem recalcular a mesma expressao nos dois branches?
- [ ] Cadeia de medidas referenciando medidas: avaliar aplanamento?

## Padronizacao
- [ ] PascalCase em medidas expostas?
- [ ] Prefixo `_` em medidas auxiliares?
- [ ] Unidade no nome quando relevante (R$, %, Qtd)?
- [ ] Comentarios em logica nao obvia?
- [ ] Medidas agrupadas em tabela de medidas dedicada (nao espalhadas)?

## Time Intelligence
- [ ] Date Table dedicada e marcada como tabela de datas?
- [ ] Coluna de data continua (sem lacunas) na Date Table?
- [ ] Funcoes TOTALYTD/TOTALMTD usam coluna de data correta?
- [ ] Ano anterior com SAMEPERIODLASTYEAR ou DATEADD(-1, YEAR)?
