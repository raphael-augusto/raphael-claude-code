# Checklist - Airflow Investigator

## Contexto do incidente
- DAG ID
- Task ID
- Run ID
- Execution date
- Ambiente
- Última alteração no código
- Última alteração em variável/conexão
- Frequência do problema

## Código
- Imports quebrados
- Operador correto
- Hook correto
- Dependências entre tasks
- Parâmetros do DAG
- Schedule e timezone
- Uso de XCom
- Uso de templates/Jinja

## Ambiente
- Providers instalados
- Requirements
- Permissões
- Secrets
- Buckets e paths
- APIs externas
- Limites de memória/CPU
- Timeouts

## Operação
- Impacto em downstream
- Risco de duplicidade
- Risco de perda de dados
- Possibilidade de reprocessamento seguro