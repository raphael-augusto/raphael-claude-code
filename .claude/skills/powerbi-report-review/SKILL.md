---
name: powerbi-report-review
description: Revisa relatórios Power BI — design de visuais, UX, performance de renderização, Row-Level Security e boas práticas de publicação.
tools: Read, Grep, Glob
---

# Power BI Report Review

Especialista em design e performance de relatorios Power BI. Foco em UX, performance de renderizacao e seguranca (RLS).

## Quando usar esta skill

Use quando o usuario:
- tiver relatorio lento para abrir ou interagir
- quiser revisar design de visuais e UX
- quiser configurar ou debugar Row-Level Security (RLS)
- quiser publicar relatorio no Power BI Service corretamente
- quiser configurar workspace, app ou deployment pipeline
- tiver visual com dados incorretos (problema de filtro de visual, nao de DAX)
- quiser otimizar numero de visuais ou interacoes em pagina

## Objetivo

Identificar problemas de performance, UX ou seguranca no relatorio, propor menor melhoria possivel.

## Como agir

1. **Entender contexto**
   - Lentidao: ao abrir, ao filtrar, ao navegar entre paginas?
   - Numero de visuais por pagina?
   - Modo de conexao: Import / DirectQuery / Composite?
   - RLS configurado? Testado?
   - Publicado no Service? Workspace / App / Embedded?

2. **Diagnosticar performance de relatorio**

   **Causas comuns de lentidao**
   - Muitos visuais em uma pagina (> 8-10) → dividir em abas
   - Visuais com medidas DAX lentas → usar `Performance Analyzer` para identificar
   - Slicer com muitos valores distintos → `Dropdown` preferido a `List`
   - Visuais customizados (AppSource) geralmente mais lentos que nativos
   - DirectQuery com muitos visuais → cada visual = query na fonte
   - `Sync slicers` em multiplas paginas → aumenta queries

   **Performance Analyzer (ferramenta nativa)**
   - View → Performance Analyzer → Start recording → atualizar pagina
   - Checar: `DAX query` (tempo de medida) vs `Visual display` (renderizacao)
   - DAX alto → otimizar medida (skill `powerbi-dax-optimizer`)
   - Visual display alto → simplificar visual ou reduzir dados exibidos

3. **Revisar design de visuais**

   **Escolha de visual correta**
   - Comparacao de categorias → Grafico de barras/colunas
   - Tendencia ao longo do tempo → Grafico de linha
   - Parte do todo → Grafico de rosca (evitar pizza)
   - Relacao entre variaveis → Dispersao (scatter)
   - Detalhe tabulado → Tabela ou Matriz
   - KPI unico → Cartao ou KPI visual
   - Evitar: graficos de pizza com > 5 categorias, gauges sem contexto

   **UX e layout**
   - Hierarquia visual clara: KPIs no topo, detalhes abaixo
   - Paleta de cores consistente (nao mais de 3-4 cores principais)
   - Rotulos de dados somente quando agregam informacao
   - Titulo descritivo em cada visual (nao generico)
   - Tooltip customizado para contexto adicional sem poluir visual
   - Paginas com nome descritivo (nao "Page 1", "Page 2")

4. **Revisar Row-Level Security**

   **RLS Estatico**
   - Criar Role no Desktop: Modeling → Manage Roles
   - Filtro DAX na tabela de dimensao (ex: `[Regiao] = "Sul"`)
   - Testar: Modeling → View as Role antes de publicar
   - Publicar → Service → Semantic Model → Security → atribuir usuarios/grupos a role

   **RLS Dinamico**
   ```dax
   -- Filtro na tabela de usuarios
   [Email] = USERPRINCIPALNAME()
   ```
   - Tabela de mapeamento: usuario → regiao/departamento/filtro
   - Relacionamento da tabela de mapeamento com tabela de fatos
   - Testar com usuario real (nao apenas "View as Role" — testar no Service tambem)

   **Erros comuns de RLS**
   - RLS aplicado na tabela errada (deve ser na dimensao, nao no fato)
   - Direcao de filtro incorreta no relacionamento → RLS nao propaga
   - Usuario nao atribuido a nenhuma role → ve todos os dados (sem role = sem restricao)
   - `USERNAME()` vs `USERPRINCIPALNAME()` → usar UPN para Azure AD

5. **Revisar publicacao e workspace**
   - Workspace de desenvolvimento separado de producao
   - Deployment Pipeline para promoção dev → homolog → prod
   - App publicada para usuarios finais (nao compartilhar workspace diretamente)
   - Dataset e relatorio em workspace Premium para RLS por row (nao apenas por relatorio)
   - Refresh agendado configurado no Service (nao apenas no Desktop)
   - Gateway configurado para fontes on-premises

## Formato da resposta

### Problema identificado
### Causa raiz
### Correcao recomendada
### Impacto esperado (performance / UX / seguranca)

## Regras

- Performance Analyzer sempre antes de otimizar visualmente
- RLS testar no Service com usuario real — nao apenas no Desktop
- Nao recomendar visual customizado sem necessidade clara
- Nao dividir pagina sem avaliar impacto em navegacao do usuario
- Deployment Pipeline para qualquer relatorio de producao

## Arquivo de apoio

Consulte sempre:
- `checklist.md`
