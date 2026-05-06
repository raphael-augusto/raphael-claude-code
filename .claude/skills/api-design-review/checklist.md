# API Design Review — Checklist

## Segurança (OWASP API Top 10)
- [ ] IDs de recursos como UUID (não inteiro sequencial)?
- [ ] Check de ownership por recurso (object-level authorization)?
- [ ] Token com expiração definida e strategy de refresh?
- [ ] Auth via header (não query param)?
- [ ] Campos sensíveis removidos do response (senha, PII desnecessário)?
- [ ] Mass assignment bloqueado (allowlist de campos editáveis)?
- [ ] Paginação obrigatória em listagens?
- [ ] Rate limiting por endpoint (especialmente auth e fluxos críticos)?
- [ ] Upload com limite de tamanho?
- [ ] Endpoints admin com verificação de role?
- [ ] CORS sem `*` em produção?
- [ ] Sem stack trace em error responses?
- [ ] Headers de segurança configurados (HSTS, X-Content-Type-Options)?

## Design REST
- [ ] Recursos em substantivos plurais (`/orders`, não `/getOrders`)?
- [ ] Sem verbos em URLs?
- [ ] Naming consistente (snake_case ou kebab-case — definir e seguir)?
- [ ] Verbos HTTP corretos (GET idempotente, POST criação, PUT substituição, PATCH parcial)?
- [ ] Status codes corretos (201 criação, 204 delete, 401 vs 403, 422 vs 400)?
- [ ] Response com envelope consistente (`{ data, error, meta }`)?
- [ ] Paginação com `total`, `page`, `page_size` ou cursor?
- [ ] Datas em ISO 8601?
- [ ] API versionada (`/v1/` ou header)?
- [ ] Error response com `code`, `message` e `details`?
- [ ] `Location` header em criação (201)?

## Design gRPC
- [ ] Serviço e métodos em PascalCase?
- [ ] Messages em PascalCase com sufixo Request/Response?
- [ ] Numeração de campos sequencial sem reutilização de números removidos?
- [ ] `google.protobuf.Timestamp` para datas?
- [ ] Streaming justificado (não por padrão)?

## Eventos / AsyncAPI
- [ ] Schema versionado e registrado em Schema Registry?
- [ ] Campos obrigatórios: `event_id`, `event_type`, `timestamp`, `source`?
- [ ] Mudanças backward compatible?
- [ ] Dead letter queue definida?
- [ ] Consumer tolera duplicatas (idempotência)?

## Documentação
- [ ] Todos endpoints documentados com descrição, request e response example?
- [ ] Erros possíveis documentados por endpoint?
- [ ] Auth scheme documentado (OAuth2 flows, JWT claims esperados)?
- [ ] Breaking changes sinalizados e versionados?
