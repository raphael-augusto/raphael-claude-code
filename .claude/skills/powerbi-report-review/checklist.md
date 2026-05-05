# Power BI Report Review — Checklist

## Performance
- [ ] Performance Analyzer executado para identificar visuais lentos?
- [ ] Menos de 8-10 visuais por pagina?
- [ ] Slicers em modo Dropdown (nao List) para alta cardinalidade?
- [ ] Sem visuais customizados desnecessarios (preferir nativos)?
- [ ] DirectQuery: numero de visuais minimizado por pagina?
- [ ] Sync slicers apenas onde necessario (cada sync = query extra)?

## Design de Visuais
- [ ] Visual correto para o tipo de dado (barra para comparacao, linha para tendencia)?
- [ ] Sem grafico de pizza com > 5 categorias?
- [ ] Paleta de cores consistente (max 3-4 cores)?
- [ ] Titulos descritivos em todos os visuais?
- [ ] Rotulos de dados somente quando agregam informacao?
- [ ] KPIs no topo da pagina (hierarquia visual)?
- [ ] Paginas com nomes descritivos?

## RLS
- [ ] Roles criadas e testadas no Desktop ("View as Role")?
- [ ] Testado no Service com usuario real?
- [ ] Filtro RLS aplicado na tabela de dimensao (nao no fato)?
- [ ] Direcao de filtro do relacionamento propaga RLS corretamente?
- [ ] Usuario sem role atribuida ve o que deveria ver (geralmente nada)?
- [ ] RLS dinamico usa `USERPRINCIPALNAME()` (nao `USERNAME()`)?
- [ ] Tabela de mapeamento usuario→filtro com relacionamento correto?

## Publicacao e Workspace
- [ ] Workspace dev/prod separados?
- [ ] Deployment Pipeline configurado para promocao dev→prod?
- [ ] App publicada para usuarios finais (nao acesso direto ao workspace)?
- [ ] Refresh agendado configurado no Service?
- [ ] Gateway configurado para fontes on-premises?
- [ ] Licenca adequada para features usadas (Pro / Premium / Fabric)?
