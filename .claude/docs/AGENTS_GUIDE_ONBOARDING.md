# Onboarding — Claude Agents

Bem-vindo ao sistema de agentes Claude. Este guia te prepara para uso imediato.

---

## O que voce precisa saber

1. **Agentes** sao especialistas IA para tarefas especificas
2. **Commands** sao atalhos que escolhem o agente automaticamente
3. **MCP Server** consulta documentacoes oficiais

---

## Primeiros passos

### Passo 1: Testar o Super Agente

```
/agent ultimate-engineering-architect
Explique a arquitetura deste projeto.
```

### Passo 2: Usar um Command

```
/code-cleanup
[cole seu codigo aqui]
```

### Passo 3: Consultar documentacao

O MCP Server consulta docs de: GCP, Python, Spark, Beam, SQL, Databricks

---

## Agentes por area

### Voce trabalha com dados?

```
/agent data-engineer-expert
```
- ETL/ELT
- SQL Server, BigQuery
- Spark, Databricks
- Pipelines

### Voce trabalha com backend?

```
/agent backend-architect
```
- FastAPI, Node
- APIs REST
- Integracao

### Voce trabalha com frontend?

```
/agent frontend-architect
```
- Angular, React
- Componentes
- UI/UX

### Voce trabalha com seguranca?

```
/agent security-engineer
```
- Autenticacao
- RBAC
- Validacoes

---

## Commands do dia a dia

| Tarefa | Command |
|--------|---------|
| Planejar algo | `/new-task` |
| Limpar codigo | `/code-cleanup` |
| Otimizar SQL | `/sql-optimize` |
| Criar ETL | `/etl-new` |
| Criar API | `/api-new` |
| Documentar | `/docs-generate` |

---

## Dicas importantes

### 1. Nao sabe qual agente usar?

Use o Super Agente:
```
/agent ultimate-engineering-architect
```

### 2. Seja direto

Ruim:
> "Oi, eu gostaria de saber se voce poderia me ajudar a otimizar uma query..."

Bom:
> "/sql-optimize [query]"

### 3. Contexto e importante

Inclua:
- Stack usada
- Erro exato
- O que ja tentou

---

## Estrutura do projeto

```
.claude/
├── agents/       # Agentes personalizados
├── commands/     # Commands
├── mcp/          # Servidor de documentacao
└── docs/         # Este guia
```

---

## Proximos passos

1. Experimente cada agente da sua area
2. Memorize os commands mais usados
3. Consulte `AGENTS_GUIDE.md` para referencia completa

---

## Suporte

Duvidas? Use:
```
/agent learning-guide
Explique como funciona [X]
```

---

**Bom trabalho!**
