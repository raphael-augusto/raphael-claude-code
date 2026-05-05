# Power BI Model Review — Checklist

## Schema
- [ ] Star schema implementado (fatos + dimensoes)?
- [ ] Snowflake desnormalizado onde possivel?
- [ ] Tabela de fatos so tem metricas + chaves estrangeiras?
- [ ] Dimensoes com chave surrogate (nao chave natural composta)?
- [ ] Date Table dedicada, marcada como tabela de datas, sem lacunas?
- [ ] Date Table com chave inteira (YYYYMMDD) para relacionamento com fato?

## Relacionamentos
- [ ] Todos os relacionamentos com cardinalidade correta (1:N)?
- [ ] Sem relacionamentos M:N sem tabela de ponte?
- [ ] Direcao de filtro Single (nao bidirecional sem justificativa)?
- [ ] Sem caminho de filtro ambiguo entre tabelas?
- [ ] Relacionamentos inativos documentados e ativados via USERELATIONSHIP em DAX?

## Colunas
- [ ] Sem colunas nunca usadas no modelo?
- [ ] Tipos de dados corretos (Date nao DateTime quando hora nao usada)?
- [ ] Sem colunas calculadas para o que medidas resolvem?
- [ ] Alta cardinalidade em chaves → tipo inteiro (nao string)?
- [ ] Hierarquias nativas definidas para drill-down?

## Performance
- [ ] Tamanho do dataset adequado para modo Import?
- [ ] Colunas de texto de alta cardinalidade em fatos → movidas para dimensao?
- [ ] Aggregations configuradas para dataset > 1GB em DirectQuery?
- [ ] Refresh incremental configurado para tabelas de fatos grandes?

## Data Table
- [ ] Uma linha por dia sem lacunas?
- [ ] Range cobre todos os dados do fato (passado e futuro proximo)?
- [ ] Colunas: Ano, Trimestre, Mes, Semana, Dia da Semana, IsWeekend, IsFeriado?
- [ ] Marcada como Date Table no Power BI Desktop?
