# Frontend Review — Checklist

## Segurança
- [ ] `dangerouslySetInnerHTML` / `innerHTML` com DOMPurify?
- [ ] Sem secrets em variáveis `NEXT_PUBLIC_*` ou equivalentes?
- [ ] Tokens em HTTP-only cookies (não localStorage)?
- [ ] Content-Security-Policy configurado via HTTP header?
- [ ] Sem `unsafe-inline` ou `unsafe-eval` no CSP?
- [ ] Sem `console.log` com dados sensíveis?
- [ ] Dependências ativas e sem CVE conhecida?
- [ ] Versões de deps críticas fixas (sem `^` loose em segurança)?

## Performance
- [ ] Code splitting por rota (`React.lazy`, `next/dynamic`, `defineAsyncComponent`)?
- [ ] Imports nomeados em libs grandes (sem `import _ from 'lodash'`)?
- [ ] Imagens otimizadas (`next/image` ou equivalente)?
- [ ] `useEffect` com dependências corretas?
- [ ] Fetch com abort controller em `useEffect`?
- [ ] Sem objetos/arrays inline em props sem `useMemo`?
- [ ] Bundle analisado antes do PR em features grandes?

## Acessibilidade (WCAG 2.2)
- [ ] Todas as imagens com `alt` descritivo?
- [ ] Botões e links com label acessível?
- [ ] Contraste de texto >= 4.5:1 (normal) / >= 3:1 (grande)?
- [ ] Focus visível em todos elementos interativos?
- [ ] Touch targets >= 44x44px?
- [ ] Inputs com `<label>` associado (não apenas placeholder)?
- [ ] Formulários navegáveis por teclado?
- [ ] `prefers-reduced-motion` respeitado em animações?

## Qualidade de Código
- [ ] Validação de input/output de API com Zod?
- [ ] Error boundaries em árvores críticas?
- [ ] Props tipadas com TypeScript?
- [ ] Lógica de negócio separada de componentes de apresentação?
- [ ] Loading, error e empty states implementados?
- [ ] Sem props drilling excessivo (mais de 3 níveis)?

## Integração com API
- [ ] Tokens de autenticação enviados via header (não query param)?
- [ ] Retry em chamadas críticas?
- [ ] Timeout configurado?
- [ ] Erros de API tratados e exibidos de forma amigável?
- [ ] Dados da API validados antes de renderizar?
