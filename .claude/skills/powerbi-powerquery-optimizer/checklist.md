# Power BI Power Query — Checklist

## Query Folding
- [ ] Filtros (SelectRows) antes de transformacoes que quebram folding?
- [ ] Projecao de colunas (SelectColumns) logo apos a fonte?
- [ ] "View Native Query" disponivel no step final (indica folding ativo)?
- [ ] `Table.Buffer` usado apenas com justificativa clara?
- [ ] Joins feitos via Power Query (preserva folding) em vez de merge apos transformacao?

## Tipos de Dados
- [ ] Tipos definidos explicitamente (nao detectados automaticamente)?
- [ ] Datas como `type date` (nao `DateTime` quando hora nao usada)?
- [ ] IDs numericos como `Int64.Type` (nao `type text`)?
- [ ] Step de tipagem no final (apos filtros e projecao)?

## Erros e Nulos
- [ ] Colunas criticas sem erros (`Table.RemoveRowsWithErrors` ou `try...otherwise`)?
- [ ] Nulos tratados explicitamente (nao ignorados)?
- [ ] Nomes de colunas validados antes de transformacao (fonte pode mudar)?

## Performance
- [ ] Colunas desnecessarias removidas o mais cedo possivel?
- [ ] Refresh incremental configurado para tabelas > 1M linhas?
- [ ] Parametros `RangeStart` / `RangeEnd` usados corretamente no filtro?
- [ ] Sem steps intermediarios inuteis gerados automaticamente?

## Boas Praticas M
- [ ] Nomes de steps descritivos (nao "Added Custom", "Changed Type1")?
- [ ] Logica repetida extraida para funcao reutilizavel?
- [ ] Credenciais de fonte via parametros ou Privacy Level correto (nao hardcoded)?
- [ ] Privacy Level configurado corretamente para evitar bloqueio de folding cross-source?
