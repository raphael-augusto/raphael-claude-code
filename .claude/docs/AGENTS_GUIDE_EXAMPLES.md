# Claude Agents — Exemplos de Codigo por Agente

---

## 1. ultimate-engineering-architect

### Exemplo: Arquitetura de microservico

```
/agent ultimate-engineering-architect
Desenhe arquitetura para sistema de pedidos com:
- API Gateway
- Servico de pedidos
- Servico de pagamentos
- Mensageria
```

**Resposta tipica:**

```
┌──────────────┐     ┌──────────────┐     ┌──────────────┐
│   Cliente    │────▶│  API Gateway │────▶│   Pedidos    │
└──────────────┘     └──────────────┘     └──────┬───────┘
                                                  │
                           ┌──────────────────────┘
                           ▼
                     ┌──────────────┐     ┌──────────────┐
                     │   RabbitMQ   │────▶│  Pagamentos  │
                     └──────────────┘     └──────────────┘
```

---

## 2. data-engineer-expert

### Exemplo: Pipeline ETL com PySpark

```
/agent data-engineer-expert
Crie ETL que le CSV do S3, transforma e grava em Delta Lake
```

**Resposta tipica:**

```python
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, when, current_timestamp

spark = SparkSession.builder.appName("etl_s3_delta").getOrCreate()

# Bronze
df_raw = spark.read.csv("s3://bucket/raw/dados.csv", header=True)

# Silver
df_clean = (
    df_raw
    .filter(col("id").isNotNull())
    .withColumn("valor", col("valor").cast("decimal(18,2)"))
    .withColumn("processed_at", current_timestamp())
)

# Gold
df_clean.write.format("delta").mode("overwrite").save("s3://bucket/gold/dados")
```

---

### Exemplo: Otimizacao SQL

```
/sql-optimize

SELECT * FROM vendas v
LEFT JOIN clientes c ON v.cliente_id = c.id
LEFT JOIN produtos p ON v.produto_id = p.id
WHERE v.data BETWEEN '2024-01-01' AND '2024-12-31'
```

**Resposta tipica:**

```sql
SELECT
    v.id,
    v.data,
    v.valor,
    c.nome AS cliente_nome,
    p.nome AS produto_nome
FROM vendas v
INNER JOIN clientes c ON v.cliente_id = c.id
INNER JOIN produtos p ON v.produto_id = p.id
WHERE v.data >= '2024-01-01'
  AND v.data < '2025-01-01'
OPTION (RECOMPILE);

-- Indices recomendados:
-- CREATE INDEX IX_vendas_data ON vendas(data) INCLUDE (cliente_id, produto_id, valor);
```

---

## 3. backend-architect

### Exemplo: API FastAPI

```
/agent backend-architect
Crie endpoint de criacao de usuario com validacao
```

**Resposta tipica:**

```python
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, EmailStr, Field
from passlib.context import CryptContext

app = FastAPI()
pwd_context = CryptContext(schemes=["bcrypt"])

class UserCreate(BaseModel):
    email: EmailStr
    password: str = Field(min_length=8)
    name: str = Field(min_length=2, max_length=100)

class UserResponse(BaseModel):
    id: int
    email: str
    name: str

@app.post("/users", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
async def create_user(user: UserCreate):
    hashed = pwd_context.hash(user.password)
    # db.insert(...)
    return UserResponse(id=1, email=user.email, name=user.name)
```

---

## 4. security-engineer

### Exemplo: Middleware de autenticacao

```
/agent security-engineer
Crie middleware JWT para FastAPI
```

**Resposta tipica:**

```python
from fastapi import Request, HTTPException, status
from fastapi.security import HTTPBearer
from jose import jwt, JWTError
from datetime import datetime

SECRET_KEY = "your-secret-key"
ALGORITHM = "HS256"

class JWTBearer(HTTPBearer):
    async def __call__(self, request: Request):
        credentials = await super().__call__(request)
        if not credentials:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN)

        try:
            payload = jwt.decode(credentials.credentials, SECRET_KEY, algorithms=[ALGORITHM])
            if payload.get("exp") < datetime.utcnow().timestamp():
                raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token expirado")
            return payload
        except JWTError:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token invalido")

auth = JWTBearer()
```

---

## 5. performance-engineer

### Exemplo: Analise de query lenta

```
/agent performance-engineer
Query demora 30s, como otimizar?

SELECT COUNT(*) FROM logs WHERE created_at > DATEADD(day, -30, GETDATE())
```

**Resposta tipica:**

```sql
-- Problema: Table scan em tabela grande

-- Solucao 1: Indice
CREATE INDEX IX_logs_created_at ON logs(created_at);

-- Solucao 2: Query otimizada
DECLARE @data_limite DATETIME = DATEADD(day, -30, GETDATE());

SELECT COUNT_BIG(*)
FROM logs WITH (NOLOCK)
WHERE created_at > @data_limite;

-- Solucao 3: Particionar tabela por mes (se > 100M registros)
```

---

## 6. refactoring-expert

### Exemplo: Simplificar codigo

```
/agent refactoring-expert
Refatore:

def process(data):
    result = []
    for item in data:
        if item is not None:
            if item['status'] == 'active':
                if item['value'] > 0:
                    result.append(item)
    return result
```

**Resposta tipica:**

```python
def process(data):
    return [
        item for item in data
        if item and item.get("status") == "active" and item.get("value", 0) > 0
    ]
```

---

## 7. technical-writer

### Exemplo: Documentar API

```
/docs-generate
Documente: POST /orders
```

**Resposta tipica:**

```markdown
## POST /orders

Cria um novo pedido.

### Request

**Headers:**
- `Authorization: Bearer {token}`
- `Content-Type: application/json`

**Body:**
```json
{
  "customer_id": 123,
  "items": [
    {"product_id": 1, "quantity": 2}
  ]
}
```

### Response

**201 Created:**
```json
{
  "id": 456,
  "status": "pending",
  "total": 99.90
}
```

**400 Bad Request:**
```json
{
  "error": "Invalid customer_id"
}
```
```

---

## 8. requirements-analyst

### Exemplo: Transformar ideia em requisitos

```
/agent requirements-analyst
Preciso de um sistema de notificacoes push
```

**Resposta tipica:**

```markdown
## Requisitos Funcionais

RF01: Sistema deve enviar notificacoes push para iOS e Android
RF02: Usuario pode ativar/desativar notificacoes por categoria
RF03: Admin pode agendar notificacoes
RF04: Sistema deve registrar taxa de abertura

## Requisitos Nao-Funcionais

RNF01: Latencia maxima de 5s para entrega
RNF02: Suportar 10k notificacoes/minuto
RNF03: Retry automatico em caso de falha

## User Stories

US01: Como usuario, quero receber notificacoes de promocoes
US02: Como admin, quero ver metricas de engajamento
```

---

## 9. deep-research-agent

### Exemplo: Comparacao tecnica

```
/agent deep-research-agent
Compare Apache Kafka vs RabbitMQ para sistema de 50k msg/s
```

**Resposta tipica:**

```markdown
## Kafka vs RabbitMQ para 50k msg/s

| Criterio | Kafka | RabbitMQ |
|----------|-------|----------|
| Throughput | 100k+ msg/s | 20-50k msg/s |
| Latencia | 2-10ms | <1ms |
| Ordenacao | Por particao | Por fila |
| Persistencia | Disco (log) | Memoria/Disco |
| Replay | Sim | Nao |

## Recomendacao

**Kafka** para:
- Alto volume
- Event sourcing
- Replay necessario

**RabbitMQ** para:
- Baixa latencia
- Roteamento complexo
- Menor curva de aprendizado

Para 50k msg/s: **Kafka**
```

---

## 10. learning-guide

### Exemplo: Explicar conceito

```
/agent learning-guide
Explique CQRS com exemplo pratico
```

**Resposta tipica:**

```markdown
## CQRS — Command Query Responsibility Segregation

Separa operacoes de leitura (Query) e escrita (Command).

### Sem CQRS
```
[API] ---> [Service] ---> [Database]
```

### Com CQRS
```
[Command API] ---> [Write DB]
                        |
                   [Sync/Event]
                        |
[Query API]  ---> [Read DB otimizado]
```

### Exemplo Pratico

```python
# Command (escrita)
class CreateOrderCommand:
    def execute(self, order_data):
        db.orders.insert(order_data)
        event_bus.publish("order_created", order_data)

# Query (leitura)
class OrderQueryService:
    def get_orders(self, filters):
        return read_db.orders.find(filters)  # DB otimizado para leitura
```

### Quando usar

- Leitura >> Escrita
- Precisar escalar leitura independente
- Modelos de leitura diferentes do de escrita
```

---

## MCP Server — Exemplos

### Listar documentacoes

```
list_docs
```

### Buscar documentacao especifica

```
get_doc tech=databricks topic=delta
```

### Pesquisar termo

```
search_docs query="broadcast join" tech=spark
```

---

**Fim dos Exemplos**
