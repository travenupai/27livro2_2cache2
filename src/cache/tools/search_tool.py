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

           