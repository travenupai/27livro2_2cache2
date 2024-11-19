import sys
import os

# Adiciona o diretório `src` ao caminho de importação
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../src')))

# Agora as importações devem funcionar
from cache.tools.search_tool import funcao_cache
from cache.crew import Cache


# Verifica se a classe Cache foi importada corretamente
print(Cache)

# Simulação de argumentos para teste
args1 = {"search_query": "Como usar cache no SerperDevTools"}

# Primeira execução: deve gerar [CACHE MISS]
print("Primeira execução: Deve gerar [CACHE MISS]")
funcao_cache(args1, None)  

# Segunda execução: deve gerar [CACHE HIT]
print("Segunda execução: Deve gerar [CACHE HIT]")
funcao_cache(args1, None)  








# antigo search_tool.py
"""
from crewai_tools import SerperDevTool
from datetime import datetime, timedelta

# Instância da ferramenta de busca SerperDevTool
ferramenta_busca = SerperDevTool()

# Dicionário para rastrear as últimas consultas de cada termo
ultima_consulta_busca = {}

# Função de cache personalizada
def funcao_cache(args, resultado):
    print(f"[DEBUG] Argumentos recebidos: {args}")
    termo = args.get("search_query", None)
    if not termo:
        print("[ERRO] Termo não encontrado nos argumentos!")
        raise ValueError("Chave 'search_query' não encontrada nos argumentos!")

    agora = datetime.now()
    print(f"[DEBUG] Termo consultado: {termo}, Hora atual: {agora}")

    if termo in ultima_consulta_busca:
        ultima_hora_consulta = ultima_consulta_busca[termo]
        print(f"[DEBUG] Última consulta para '{termo}': {ultima_hora_consulta}")

        if agora - ultima_hora_consulta < timedelta(hours=1):
            print(f"[CACHE HIT] Reutilizando cache para o termo '{termo}'")
            return True

    print(f"[CACHE MISS] Atualizando cache para o termo '{termo}'")
    ultima_consulta_busca[termo] = agora
    return False


# Associa a função de cache à ferramenta SerperDevTool
ferramenta_busca.cache_function = funcao_cache
"""