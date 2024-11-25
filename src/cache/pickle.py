"""

import os
import pickle  # Importando pickle para serialização binária
from datetime import datetime, timedelta
from crewai_tools import SerperDevTool

# Caminho do arquivo de cache
CACHE_FILE = "cache_data.pkl"  # Alterado para .pkl para indicar formato pickle

# Instância da ferramenta de busca SerperDevTool
ferramenta_busca = SerperDevTool()

# Função para carregar o cache do arquivo
def carregar_cache():
    """
    Carrega os dados de cache do arquivo pickle, se existir.
    """
    if os.path.exists(CACHE_FILE):
        with open(CACHE_FILE, "rb") as file:  # Abrindo no modo binário para leitura
            return pickle.load(file)  # Carrega os dados do arquivo pickle
    return {}

# Função para salvar o cache no arquivo
def salvar_cache(cache_data):
    """
    Salva os dados de cache no arquivo pickle.
    """
    with open(CACHE_FILE, "wb") as file:  # Abrindo no modo binário para escrita
        pickle.dump(cache_data, file)  # Salva os dados no arquivo pickle

# Carrega o cache inicial
ultima_consulta_busca = carregar_cache()

# Função de cache personalizada
def funcao_cache(args, resultado):
    """
    Função que implementa o mecanismo de cache.
    """
    termo = args.get("search_query", None)
    if not termo:
        raise ValueError("Chave 'search_query' não encontrada nos argumentos!")

    agora = datetime.now()
    print(f"[DEBUG] Termo consultado: {termo}, Hora atual: {agora}")

    # Verifica se o termo está no cache e se o tempo é válido
    if termo in ultima_consulta_busca:
        ultima_hora_consulta = datetime.fromisoformat(ultima_consulta_busca[termo])
        print(f"[DEBUG] Última consulta para '{termo}': {ultima_hora_consulta}")

        if agora - ultima_hora_consulta < timedelta(hours=1):
            print(f"[CACHE HIT] Reutilizando cache para o termo '{termo}'")
            return True  # Usa cache

    # Atualiza o cache e salva no arquivo
    ultima_consulta_busca[termo] = agora.isoformat()
    salvar_cache(ultima_consulta_busca)
    print(f"[CACHE MISS] Atualizando cache para o termo '{termo}'")
    return False  # Não usa cache

# Associa a função de cache à ferramenta SerperDevTool
ferramenta_busca.cache_function = funcao_cache
"""