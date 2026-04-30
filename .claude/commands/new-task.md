---
description: Analisa complexidade da tarefa e cria plano de implementacao acionavel
model: claude-sonnet-4-6
---

Analise a tarefa a seguir e crie um plano de implementação claro e acionável.

## Tarefa

$ARGUMENTS

## Framework de Análise

### 1. Decomposição
- Entender requisitos
- Identificar dependências
- Listar arquivos/componentes afetados
- Estimar complexidade (Pequena/Média/Grande)

### 2. Estimativa de Tempo
- **Pequena**: 1-2 horas (bug simples, ajuste menor)
- **Média**: Meio dia a 1 dia (novo componente, endpoint)
- **Grande**: 2-5 dias (feature complexa, múltiplas integrações)
- **Muito Grande**: 1+ semana (refactor maior, novo subsistema)

### 3. Avaliação de Riscos
Identificar bloqueadores potenciais:
- Dependências desconhecidas
- Limitações de API
- Necessidade de migração de dados
- Breaking changes
- Problemas com serviços externos

### 4. Passos de Implementação

Criar etapas sequenciais e lógicas:
1. Setup/preparação
2. Mudanças de pipeline / modelo de dados
3. Lógica SQL / transformação
4. Testes (unitário + integração)
5. Deploy / config CI-CD

### 5. Critérios de Sucesso

Definir "pronto":
- Feature funciona conforme especificado
- Testes passam
- Sem regressões
- Code review feito
- Documentado

## Formato de Saída

### Análise da Tarefa
- **Tipo**: [Bug Fix / Feature / Refactor / Infraestrutura]
- **Complexidade**: [Pequena / Média / Grande / Muito Grande]
- **Tempo Estimado**: X horas/dias
- **Prioridade**: [Alta / Média / Baixa]

### Plano de Implementação

**Fase 1: [Nome]** (Estimativa de tempo)
- [ ] Passo 1
- [ ] Passo 2

**Fase 2: [Nome]** (Estimativa de tempo)
- [ ] Passo 3
- [ ] Passo 4

### Estratégia de Testes
- Testes unitários para X
- Testes de integração para Y
- Passos de teste manual

### Problemas Potenciais
- Problema 1 e mitigação
- Problema 2 e mitigação

### Próximos Passos
1. Começar com Fase 1, Passo 1
2. Testar incrementalmente
3. Commitar frequentemente
