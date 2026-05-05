# Terraform Review — Checklist

## Segurança
- [ ] Sem credenciais hardcoded em `.tf` ou `.tfvars`
- [ ] IAM sem `*` em actions ou resources sem justificativa
- [ ] Storage buckets/blobs sem acesso público desnecessário
- [ ] Encryption at rest habilitada em DB, storage, discos
- [ ] VMs/containers sem portas abertas ao 0.0.0.0/0 sem firewall
- [ ] Secrets via Secret Manager / Key Vault / Secrets Manager (nunca variável literal)

## Estado
- [ ] Backend remoto configurado (GCS / S3 / Azure Blob)
- [ ] State lock habilitado
- [ ] `terraform.tfstate` fora do repositório (.gitignore)
- [ ] Workspaces separados por ambiente (dev/staging/prod)

## Modularidade
- [ ] Root module < 200 linhas (caso contrário, extrair módulos)
- [ ] Módulos com `variables.tf`, `outputs.tf`, `main.tf` separados
- [ ] Sem lógica duplicada entre módulos
- [ ] Todas as variáveis com `description` e `type`

## Custo
- [ ] SKU/tier justificado para o ambiente
- [ ] Auto-scaling ou auto-suspend configurado onde aplicável
- [ ] Storage com lifecycle policy para dados frios
- [ ] Recursos de dev sem `prevent_destroy = true`

## Naming e Tags
- [ ] snake_case consistente em resource names
- [ ] Tags obrigatórias: `environment`, `owner`, `project`
- [ ] Outputs nomeados de forma clara e documentados

## CI/CD
- [ ] `plan` em PRs, `apply` apenas em merge com aprovação
- [ ] Secrets de provider via variáveis de ambiente ou OIDC (nunca hardcoded no workflow)
- [ ] `terraform fmt` e `terraform validate` no pipeline
