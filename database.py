import os
import psycopg2
from psycopg2.extras import RealDictCursor

DATABASE_URL = os.getenv('DATABASE_URL')

def get_connection():
    """Retorna conexão com o banco"""
    return psycopg2.connect(DATABASE_URL, cursor_factory=RealDictCursor)

def criar_tabelas():
    """Cria todas as tabelas necessárias"""
    conn = get_connection()
    cur = conn.cursor()
    
    # Tabela de IAs
    cur.execute('''
        CREATE TABLE IF NOT EXISTS ias (
            id VARCHAR(50) PRIMARY KEY,
            nome VARCHAR(100) NOT NULL,
            funcao VARCHAR(200),
            emoji VARCHAR(10),
            ativa BOOLEAN DEFAULT false,
            bio TEXT,
            ultima_acao TIMESTAMP,
            prioridade VARCHAR(20),
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    # Tabela de logs das IAs
    cur.execute('''
        CREATE TABLE IF NOT EXISTS ia_logs (
            id SERIAL PRIMARY KEY,
            ia_id VARCHAR(50) REFERENCES ias(id),
            acao TEXT NOT NULL,
            resultado TEXT,
            sucesso BOOLEAN DEFAULT true,
            timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    # Tabela de atividades das IAs
    cur.execute('''
        CREATE TABLE IF NOT EXISTS ia_atividades (
            id SERIAL PRIMARY KEY,
            ia_id VARCHAR(50) REFERENCES ias(id),
            descricao TEXT NOT NULL,
            ordem INTEGER,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    # Tabela de permissões
    cur.execute('''
        CREATE TABLE IF NOT EXISTS ia_permissoes (
            ia_id VARCHAR(50) PRIMARY KEY REFERENCES ias(id),
            analisar BOOLEAN DEFAULT true,
            sugerir BOOLEAN DEFAULT true,
            executar BOOLEAN DEFAULT false,
            enviar BOOLEAN DEFAULT false,
            acessar BOOLEAN DEFAULT false
        )
    ''')
    
    # Tabela de fontes de sabedoria
    cur.execute('''
        CREATE TABLE IF NOT EXISTS ia_fontes (
            id SERIAL PRIMARY KEY,
            ia_id VARCHAR(50) REFERENCES ias(id),
            tipo VARCHAR(20),
            nome TEXT,
            url TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    # Tabela de conexões entre IAs
    cur.execute('''
        CREATE TABLE IF NOT EXISTS ia_conexoes (
            ia_origem VARCHAR(50) REFERENCES ias(id),
            ia_destino VARCHAR(50) REFERENCES ias(id),
            ativa BOOLEAN DEFAULT true,
            PRIMARY KEY (ia_origem, ia_destino)
        )
    ''')
    
    # Tabela de leads (integração Kommo)
    cur.execute('''
        CREATE TABLE IF NOT EXISTS leads (
            id INTEGER PRIMARY KEY,
            nome VARCHAR(200),
            telefone VARCHAR(50),
            email VARCHAR(200),
            status VARCHAR(50),
            ultima_interacao TIMESTAMP,
            dados JSONB,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    # Tabela de métricas
    cur.execute('''
        CREATE TABLE IF NOT EXISTS metricas (
            id SERIAL PRIMARY KEY,
            ia_id VARCHAR(50) REFERENCES ias(id),
            tipo VARCHAR(50),
            valor NUMERIC,
            data DATE DEFAULT CURRENT_DATE,
            timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    conn.commit()
    cur.close()
    conn.close()
    print("✅ Tabelas criadas com sucesso!")

def popular_ias_iniciais():
    """Popula IAs iniciais no banco"""
    conn = get_connection()
    cur = conn.cursor()
    
    ias = [
        ("bia", "BIA", "Líder Desenvolvedora", "👑", "maxima"),
        ("anna-laura", "ANNA LAURA", "Especialista em Vendas++", "💰", "maxima"),
        ("vigilante", "VIGILANTE", "Monitor de Leads", "🚨", "alta"),
        ("reativador", "REATIVADOR", "Especialista em Reativação", "🔄", "alta"),
        ("marketeiro", "MARKETEIRO", "Criador de Conteúdo", "📱", "alta"),
        ("competidor", "COMPETIDOR", "Analista de Concorrência", "🔍", "alta"),
        ("analista", "ANALISTA DE DADOS", "Análise de Leads", "📊", "alta"),
        ("qualificador", "QUALIFICADOR", "Classificação de Leads", "🎯", "alta"),
        ("fiscal", "FISCAL DO CRM", "Qualidade de Dados", "📝", "alta"),
        ("patio", "ORGANIZADOR DE PÁTIO", "Controle de Pátio", "🏗️", "alta"),
        ("iscas", "ESTRATEGISTA DE ISCAS", "Monitor de Conversão", "📈", "alta"),
        ("dedo-duro", "DEDO DURO", "Detector de Inconsistências", "🕵️", "media"),
        ("analista-preco", "ANALISTA DE PREÇO", "Monitor de Mercado", "💵", "media"),
        ("analista-tecnico", "ANALISTA TÉCNICO", "Especialista em Diagnóstico", "🔧", "media"),
        ("casanova", "CASANOVA", "Recompensa de Meta (Tinder)", "💘", "media")
    ]
    
    for ia in ias:
        cur.execute('''
            INSERT INTO ias (id, nome, funcao, emoji, prioridade)
            VALUES (%s, %s, %s, %s, %s)
            ON CONFLICT (id) DO NOTHING
        ''', ia)
    
    conn.commit()
    cur.close()
    conn.close()
    print("✅ IAs iniciais populadas!")

if __name__ == "__main__":
    print("🔧 Configurando banco de dados...")
    criar_tabelas()
    popular_ias_iniciais()
    print("✅ Banco configurado com sucesso!")
