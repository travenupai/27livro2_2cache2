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
