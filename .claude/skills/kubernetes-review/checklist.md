# Kubernetes Review — Checklist

## Resources
- [ ] `requests.cpu` e `requests.memory` definidos em todos os containers?
- [ ] `limits.memory` definido (sem limit → OOMKill do node)?
- [ ] `limits.cpu` avaliado (throttling pode ser pior que sem limit)?
- [ ] QoS class adequada: Guaranteed (req=limit) para apps críticas?

## Disponibilidade
- [ ] `minReplicas >= 2` em produção?
- [ ] `PodDisruptionBudget` definido?
- [ ] `readinessProbe` e `livenessProbe` configurados?
- [ ] `terminationGracePeriodSeconds` adequado para o app?
- [ ] Anti-affinity para distribuir pods entre nodes/zonas?

## Segurança
- [ ] `runAsNonRoot: true` em SecurityContext?
- [ ] `readOnlyRootFilesystem: true` onde possível?
- [ ] `allowPrivilegeEscalation: false`?
- [ ] ServiceAccount dedicado (não `default`)?
- [ ] `automountServiceAccountToken: false` quando não necessário?
- [ ] Imagens com digest ou tag imutável (não `:latest`)?
- [ ] Secrets fora do Git (External Secrets / Sealed Secrets / Vault)?

## RBAC
- [ ] Role/ClusterRole com least privilege?
- [ ] Sem `cluster-admin` para aplicações?
- [ ] Namespace isolado por time/ambiente?

## Networking
- [ ] NetworkPolicy com `default-deny` + allow explícito?
- [ ] Service type correto (ClusterIP interno, LoadBalancer externo)?
- [ ] Ingress com TLS configurado?
- [ ] Annotations corretas para o Ingress controller usado?

## Scaling
- [ ] HPA configurado para apps stateless com carga variável?
- [ ] Metrics corretas para HPA (CPU, custom, external)?
- [ ] Node autoscaling habilitado no cluster?

## ConfigMap e Secrets
- [ ] Sem dados sensíveis em ConfigMap?
- [ ] Secrets não versionados no Git?
- [ ] Volume mount usado para configs grandes (não env explosion)?

## Helm (quando aplicável)
- [ ] `values.yaml` sem secrets hardcoded?
- [ ] `helm diff` executado antes de upgrade em prod?
- [ ] `--atomic` em pipelines de deploy automatizados?
- [ ] Chart version pinned (não `*` ou `latest`)?

## Observabilidade
- [ ] Logs estruturados (stdout/stderr, não arquivo)?
- [ ] Métricas expostas via `/metrics` (Prometheus)?
- [ ] Resource limits configurados para evitar `noisy neighbor`?
