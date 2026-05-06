---
name: Erros a Evitar
description: Comportamentos e abordagens que causaram problemas ou foram corrigidos — nao repetir
type: feedback
last_updated: 2026-05-05
---

## Como usar

Consultar antes de responder. Se cometer erro novo → sugerir adicao aqui com causa raiz.

## Formato de entrada

```
### [CATEGORIA] — [nome curto]
- Anti-pattern: [o que nao fazer]
- Causa: [por que e problema]
- Correto: [o que fazer em vez disso]
```

---

## Estilo de Resposta

### Resposta — Sem emoji
- Anti-pattern: Usar emojis em qualquer resposta
- Causa: Usuario rejeitou explicitamente
- Correto: Texto puro, sem decoracao

### Resposta — Sem introducao
- Anti-pattern: Iniciar com "Claro!", "Certamente!", explicacao teorica ou contexto nao solicitado
- Causa: Ruido — usuario quer codigo ou resposta direta
- Correto: Codigo primeiro, resumo de 1 linha depois

### Resposta — Sem resumo pos-entrega
- Anti-pattern: Resumir o que foi feito apos entregar codigo ("Em resumo, o que fiz foi...")
- Causa: Usuario le o diff — repetir e desperdicio de tokens
- Correto: Encerrar na ultima linha relevante

---

## Codigo

### Codigo — Sem helpers de uso unico
- Anti-pattern: Criar funcoes auxiliares que so sao chamadas em um lugar
- Causa: Complexidade desnecessaria — inline e mais simples
- Correto: Inline quando usado uma vez; extrair apenas se reutilizado

### Codigo — Sem error handling especulativo
- Anti-pattern: Adicionar try/except para cenarios que nao podem ocorrer
- Causa: Codigo morto — mascara bugs reais e aumenta complexidade
- Correto: Validar apenas em boundaries reais (input usuario, API externa)

### Codigo — Sem features nao solicitadas
- Anti-pattern: Adicionar feature extra durante implementacao de outra
- Causa: Escopo creep — o usuario nao pediu, nao quer
- Correto: Escopo exato do pedido — nada mais

### Codigo — Sem refatoracao nao solicitada
- Anti-pattern: Refatorar codigo adjacente ao corrigir um bug
- Causa: Risco de regressao — mudanca nao revisada
- Correto: Fix minimo e cirurgico no escopo do bug

---

## Dados / SQL

### SQL — SELECT * em producao
- Anti-pattern: `SELECT *` em qualquer query de producao
- Causa: Performance (full scan), schema instavel, custo BigQuery
- Correto: Listar colunas explicitamente

### SQL — Subqueries aninhadas
- Anti-pattern: Mais de 1 nivel de subquery correlacionada
- Causa: Ilegivel, otimizador nao consegue planejar bem
- Correto: CTE para cada nivel de transformacao

### Pipeline — INSERT sem idempotencia
- Anti-pattern: INSERT simples sem verificar existencia
- Causa: Duplicatas em reprocessamento
- Correto: MERGE com chave de negocio unica

---

## Testes

### Testes — Mock de banco em integracao
- Anti-pattern: Mockar banco em testes de integracao
- Causa: Mock nao reflete schema real — testes passam, prod falha
- Correto: Banco real ou container (testcontainers)

---

## Agentes / Orquestracao

### Agente — Invocar skill de dominio diretamente
- Anti-pattern: Orchestrator invocar `airflow-debug` ou `pyspark-optimizer` diretamente
- Causa: Bypassar o agent especialista quebra o fluxo de contexto
- Correto: Delegar ao `data-engineer-expert` que invoca a skill adequada

### Agente — Propagar saida reprovada
- Anti-pattern: Repassar resultado de agente com `status=erro` ou `confianca < 0.7`
- Causa: Output invalido chega ao usuario
- Correto: Fallback ou refinamento (max 2x) antes de consolidar
