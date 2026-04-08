#!/usr/bin/env python3
"""MCP Server para consulta de documentacoes tecnicas."""

import json
import sys
import urllib.request
import urllib.error
from html.parser import HTMLParser

DOCS = {
    "gcp": {
        "bigquery": "https://cloud.google.com/bigquery/docs",
        "storage": "https://cloud.google.com/storage/docs",
        "dataflow": "https://cloud.google.com/dataflow/docs",
        "pubsub": "https://cloud.google.com/pubsub/docs",
        "cloudrun": "https://cloud.google.com/run/docs",
        "cloudfunctions": "https://cloud.google.com/functions/docs",
    },
    "python": {
        "official": "https://docs.python.org/3/",
        "pandas": "https://pandas.pydata.org/docs/",
        "numpy": "https://numpy.org/doc/stable/",
    },
    "spark": {
        "official": "https://spark.apache.org/docs/latest/",
        "pyspark": "https://spark.apache.org/docs/latest/api/python/",
        "sql": "https://spark.apache.org/docs/latest/sql-programming-guide.html",
    },
    "beam": {
        "official": "https://beam.apache.org/documentation/",
        "python_sdk": "https://beam.apache.org/documentation/sdks/python/",
        "transforms": "https://beam.apache.org/documentation/transforms/python/overview/",
    },
    "sql": {
        "tsql": "https://learn.microsoft.com/en-us/sql/t-sql/language-reference",
        "functions": "https://learn.microsoft.com/en-us/sql/t-sql/functions/functions",
        "procedures": "https://learn.microsoft.com/en-us/sql/relational-databases/stored-procedures/stored-procedures-database-engine",
    },
    "databricks": {
        "official": "https://docs.databricks.com/",
        "unity_catalog": "https://docs.databricks.com/en/data-governance/unity-catalog/index.html",
        "delta": "https://docs.databricks.com/en/delta/index.html",
        "sql": "https://docs.databricks.com/en/sql/index.html",
    },
}


class HTMLTextExtractor(HTMLParser):
    def __init__(self):
        super().__init__()
        self.text = []
        self.skip = False

    def handle_starttag(self, tag, attrs):
        if tag in ("script", "style", "nav", "footer", "header"):
            self.skip = True

    def handle_endtag(self, tag):
        if tag in ("script", "style", "nav", "footer", "header"):
            self.skip = False

    def handle_data(self, data):
        if not self.skip:
            text = data.strip()
            if text:
                self.text.append(text)

    def get_text(self):
        return " ".join(self.text)


def fetch_url(url: str, max_chars: int = 8000) -> str:
    """Busca conteudo de URL e extrai texto."""
    try:
        req = urllib.request.Request(
            url,
            headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/120.0.0.0"}
        )
        with urllib.request.urlopen(req, timeout=10) as response:
            html = response.read().decode("utf-8", errors="ignore")
            parser = HTMLTextExtractor()
            parser.feed(html)
            text = parser.get_text()
            return text[:max_chars] if len(text) > max_chars else text
    except urllib.error.URLError as e:
        return f"Erro ao acessar URL: {e}"
    except Exception as e:
        return f"Erro: {e}"


def list_docs() -> dict:
    """Lista todas as documentacoes disponiveis."""
    return {"docs": DOCS}


def get_doc(tech: str, topic: str = None) -> dict:
    """Busca documentacao de uma tecnologia."""
    tech = tech.lower()
    if tech not in DOCS:
        return {"error": f"Tecnologia '{tech}' nao encontrada. Disponiveis: {list(DOCS.keys())}"}

    if topic:
        topic = topic.lower()
        if topic not in DOCS[tech]:
            return {"error": f"Topico '{topic}' nao encontrado. Disponiveis: {list(DOCS[tech].keys())}"}
        url = DOCS[tech][topic]
        content = fetch_url(url)
        return {"tech": tech, "topic": topic, "url": url, "content": content}

    return {"tech": tech, "topics": DOCS[tech]}


def search_docs(query: str, tech: str = None) -> dict:
    """Busca por termo nas documentacoes."""
    results = []
    search_in = {tech: DOCS[tech]} if tech and tech in DOCS else DOCS

    for t, topics in search_in.items():
        for topic, url in topics.items():
            content = fetch_url(url, max_chars=15000)
            if query.lower() in content.lower():
                idx = content.lower().find(query.lower())
                snippet = content[max(0, idx-100):idx+300]
                results.append({
                    "tech": t,
                    "topic": topic,
                    "url": url,
                    "snippet": f"...{snippet}..."
                })

    return {"query": query, "results": results[:5]}


def handle_request(request: dict) -> dict:
    """Processa requisicao MCP."""
    method = request.get("method", "")
    params = request.get("params", {})

    if method == "initialize":
        return {
            "protocolVersion": "2024-11-05",
            "capabilities": {"tools": {}},
            "serverInfo": {"name": "docs-server", "version": "1.0.0"}
        }

    if method == "tools/list":
        return {
            "tools": [
                {
                    "name": "list_docs",
                    "description": "Lista todas as documentacoes disponiveis",
                    "inputSchema": {"type": "object", "properties": {}}
                },
                {
                    "name": "get_doc",
                    "description": "Busca documentacao de uma tecnologia (gcp, python, spark, beam, sql, databricks)",
                    "inputSchema": {
                        "type": "object",
                        "properties": {
                            "tech": {"type": "string", "description": "Tecnologia (gcp, python, spark, beam, sql, databricks)"},
                            "topic": {"type": "string", "description": "Topico especifico (opcional)"}
                        },
                        "required": ["tech"]
                    }
                },
                {
                    "name": "search_docs",
                    "description": "Busca por termo nas documentacoes",
                    "inputSchema": {
                        "type": "object",
                        "properties": {
                            "query": {"type": "string", "description": "Termo de busca"},
                            "tech": {"type": "string", "description": "Filtrar por tecnologia (opcional)"}
                        },
                        "required": ["query"]
                    }
                }
            ]
        }

    if method == "tools/call":
        tool_name = params.get("name", "")
        args = params.get("arguments", {})

        if tool_name == "list_docs":
            result = list_docs()
        elif tool_name == "get_doc":
            result = get_doc(args.get("tech", ""), args.get("topic"))
        elif tool_name == "search_docs":
            result = search_docs(args.get("query", ""), args.get("tech"))
        else:
            result = {"error": f"Tool '{tool_name}' nao encontrada"}

        return {"content": [{"type": "text", "text": json.dumps(result, ensure_ascii=False, indent=2)}]}

    return {"error": f"Metodo '{method}' nao suportado"}


def main():
    """Loop principal do servidor MCP."""
    while True:
        try:
            line = sys.stdin.readline()
            if not line:
                break

            request = json.loads(line)
            response = {
                "jsonrpc": "2.0",
                "id": request.get("id"),
                "result": handle_request(request)
            }

            sys.stdout.write(json.dumps(response) + "\n")
            sys.stdout.flush()
        except json.JSONDecodeError:
            continue
        except Exception as e:
            error_response = {
                "jsonrpc": "2.0",
                "id": None,
                "error": {"code": -32603, "message": str(e)}
            }
            sys.stdout.write(json.dumps(error_response) + "\n")
            sys.stdout.flush()


if __name__ == "__main__":
    main()
