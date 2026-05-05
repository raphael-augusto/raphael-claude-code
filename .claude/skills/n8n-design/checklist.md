# n8n Workflow — Checklist

## Design
- [ ] Trigger correto para o caso (Webhook / Schedule / App trigger)?
- [ ] Nodes nativos usados antes de HTTP Request ou Code node?
- [ ] Sem lógica duplicada entre branches?
- [ ] Nomes dos nodes descritivos (não "HTTP Request 3")?
- [ ] Workflow com nota/descrição para manutenção futura?

## Error Handling
- [ ] `Error Trigger` node configurado para notificar em falha?
- [ ] `Continue on Error` ativo em nodes não-críticos?
- [ ] Retry configurado em HTTP Request para erros 5xx?
- [ ] Validação de dados antes de nodes que assumem campos específicos (IF node)?
- [ ] Branch de fallback para dados inesperados?

## Credenciais e Segurança
- [ ] Credenciais via Credential Manager (nunca hardcoded)?
- [ ] Scopes mínimos necessários para cada credencial OAuth?
- [ ] Webhook com autenticação (Header Auth ou Basic Auth) se dados sensíveis?
- [ ] Sem dados sensíveis em logs de execução (mascarar se necessário)?

## Performance
- [ ] `Split in Batches` para arrays > 50 items?
- [ ] `Wait` node para respeitar rate limits de APIs?
- [ ] Webhook com resposta imediata para operações longas (async)?
- [ ] Sem loops aninhados desnecessários?

## Self-hosted (quando aplicável)
- [ ] PostgreSQL como banco (não SQLite em prod)?
- [ ] `N8N_ENCRYPTION_KEY` configurado e persistente?
- [ ] `N8N_WEBHOOK_URL` apontando para URL pública correta?
- [ ] Redis configurado para execuções paralelas em escala?
- [ ] Backup de workflows agendado (CLI export ou API)?
- [ ] Versão n8n pinned no docker-compose (não `latest`)?
- [ ] HTTPS configurado (não HTTP em prod)?

## Integrações
- [ ] Rate limits da API destino considerados?
- [ ] Paginação implementada para APIs com limite de registros?
- [ ] Timeout adequado no HTTP Request node?
- [ ] Headers de autenticação corretos (Bearer / API Key / OAuth)?
