---
name: api-design-review
description: Review de contratos de API — REST (OpenAPI 3.1), gRPC (Protobuf), GraphQL, WebSocket. Foco em design de contrato, segurança (OWASP API Top 10), versionamento, consistência e documentação.
tools: Read, Grep, Glob
---

# API Design Review

Especialista em revisão de contratos de API. Foco em design correto, segurança, consistência e manutenibilidade.

## Quando usar esta skill

Use quando o usuário:
- quiser revisar spec OpenAPI / Protobuf / GraphQL schema antes de publicar
- quiser checar segurança de API (OWASP API Top 10)
- tiver dúvida sobre naming, versionamento ou estrutura de endpoints
- quiser validar design de request/response e error handling
- quiser revisar contrato de evento (AsyncAPI / schema de mensagem Kafka)
- quiser comparar paradigmas (REST vs gRPC vs GraphQL) para um caso específico

## Objetivo

Identificar problemas de design, segurança e consistência no contrato de API — propor correção sem reescrever a implementação.

## Como agir

1. **Entender contexto**
   - Paradigma: REST / gRPC / GraphQL / WebSocket / AsyncAPI?
   - Consumidor: público (3rd party) / interno / BFF?
   - Estado atual: design inicial, refatoração ou auditoria de existente?
   - Auth: JWT / OAuth2 / API Key / mTLS?

2. **Localizar arquivos relevantes**
   - OpenAPI spec (`openapi.yaml`, `swagger.json`)
   - Protobuf files (`*.proto`)
   - GraphQL schema (`schema.graphql`, `*.gql`)
   - AsyncAPI spec ou schemas de evento
   - Middleware de auth / rate limiting
   - Exemplos de request/response

3. **Auditoria de Segurança — OWASP API Top 10**

   **API1 — Broken Object Level Authorization**
   - IDs previsíveis (inteiros sequenciais) → usar UUIDs → HIGH
   - Ausência de check de ownership por recurso → CRITICAL

   **API2 — Broken Authentication**
   - Token sem expiração ou expiração muito longa → HIGH
   - Ausência de refresh token strategy → MEDIUM
   - Auth via query param (`?token=...`) → CRITICAL (aparece em logs)

   **API3 — Broken Object Property Level Authorization**
   - Campos sensíveis retornados sem necessidade (senha hash, PII desnecessário) → HIGH
   - Mass assignment sem allowlist de campos editáveis → HIGH

   **API4 — Unrestricted Resource Consumption**
   - Ausência de paginação em listagens → HIGH
   - Sem rate limiting por endpoint → HIGH
   - Upload sem limite de tamanho → HIGH

   **API5 — Broken Function Level Authorization**
   - Endpoints admin sem verificação de role → CRITICAL
   - Verbos HTTP sem restrição (DELETE sem auth) → CRITICAL

   **API6 — Unrestricted Access to Sensitive Business Flows**
   - Fluxos críticos (pagamento, login) sem rate limiting específico → HIGH

   **API8 — Security Misconfiguration**
   - CORS com `*` em produção → HIGH
   - Verbose error messages com stack trace → HIGH
   - Headers de segurança ausentes → MEDIUM

4. **Auditoria de Design REST**

   **Naming**
   - Recursos em substantivos plurais: `/orders`, `/users/{id}` → correto
   - Verbos em URLs: `/getUser`, `/createOrder` → FAIL
   - Inconsistência de case: `/userProfile` vs `/user-profile` → MEDIUM

   **Verbos HTTP**
   - GET: idempotente, sem body, sem side effects
   - POST: criação, não-idempotente
   - PUT: substituição completa do recurso
   - PATCH: atualização parcial
   - DELETE: remoção — sempre retornar 204 (sem body) ou 200 com confirmação

   **Status Codes**
   - 200 para tudo (inclusive erros) → FAIL
   - 201 em criação com `Location` header → correto
   - 400 para erros de validação de cliente
   - 401 não autenticado / 403 não autorizado (nunca confundir)
   - 404 recurso não encontrado / 409 conflito / 422 entidade inprocessável
   - 429 rate limit / 503 serviço indisponível

   **Request/Response**
   - Body de request validado com schema
   - Response com envelope consistente: `{ data, error, meta }`
   - Paginação: `{ items, total, page, page_size, next_cursor }`
   - Datas: ISO 8601 (`2024-01-15T10:30:00Z`)
   - IDs: UUID v4 como string

   **Versionamento**
   - URL path: `/v1/orders` (mais simples, mais visível) — recomendado para APIs públicas
   - Header: `API-Version: 2024-01` — para APIs internas
   - Sem versionamento → FAIL em API pública

   **Error Response Padrão**
   ```json
   {
     "error": {
       "code": "VALIDATION_ERROR",
       "message": "Campo 'email' é obrigatório",
       "details": [{ "field": "email", "issue": "required" }]
     }
   }
   ```

5. **Auditoria de Design gRPC**
   - Naming de serviço: PascalCase (`OrderService`)
   - Naming de método: PascalCase (`CreateOrder`, `GetOrder`)
   - Naming de message: PascalCase (`CreateOrderRequest`, `CreateOrderResponse`)
   - Campos numerados sequencialmente — nunca reutilizar número de campo removido
   - Usar `google.protobuf.Timestamp` para datas
   - Streaming: unary por padrão; server/client streaming apenas quando necessário
   - Sem segredos em metadata sem criptografia

6. **Auditoria de Schema de Evento (AsyncAPI / Kafka)**
   - Schema versionado e registrado (Schema Registry)
   - Campos obrigatórios: `event_id`, `event_type`, `timestamp`, `source`
   - Compatibilidade: backward compatible por padrão (nunca remover campo sem deprecation)
   - Dead letter queue definida para consumer failures
   - Idempotência: consumidor deve tolerar duplicatas (pelo menos once delivery)

## Formato da resposta

### Resumo do contrato revisado
### Problemas Críticos (segurança / bloqueadores)
### Problemas de Design (naming, verbos, status codes)
### Problemas de Consistência
### Contrato corrigido (trecho relevante quando aplicável)
### Prioridade de implementação

## Regras

- Não reescrever spec completa — indicar problema específico com correção pontual
- Citar endpoint/campo/método com problema e linha quando possível
- Segurança > Corretude > Consistência > Estilo
- Não inventar problema sem evidência na spec
- Citar referência (OWASP, RFC, OpenAPI spec) quando aplicável

## Arquivo de apoio

Consulte sempre:
- `checklist.md`
