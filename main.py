import os
import json
from datetime import datetime
from flask import Flask, jsonify, request
from dotenv import load_dotenv
import psycopg2
from psycopg2 import pool
from openai import OpenAI
from functools import wraps

load_dotenv()

app = Flask(__name__)
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

# Configuração do banco
DATABASE_URL = os.getenv('DATABASE_URL')

# Pool de conexões para melhor performance
connection_pool = None

def init_connection_pool():
    """Inicializa pool de conexões"""
    global connection_pool
    try:
        connection_pool = pool.SimpleConnectionPool(1, 10, DATABASE_URL)
        print("✅ Pool de conexões criado com sucesso")
    except Exception as e:
        print(f"❌ Erro ao criar pool: {e}")

def get_db_connection():
    """Obtém conexão do pool"""
    if connection_pool:
        return connection_pool.getconn()
    return psycopg2.connect(DATABASE_URL)

def return_db_connection(conn):
    """Retorna conexão ao pool"""
    if connection_pool:
        connection_pool.putconn(conn)

def init_db():
    """Inicializa tabelas do banco"""
    conn = get_db_connection()
    cur = conn.cursor()
    
    try:
        # Tabela de logs das IAs
        cur.execute('''
            CREATE TABLE IF NOT EXISTS ia_logs (
                id SERIAL PRIMARY KEY,
                ia_nome VARCHAR(100),
                acao TEXT,
                resultado TEXT,
                timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        
        # Tabela de configurações das IAs
        cur.execute('''
            CREATE TABLE IF NOT EXISTS ia_config (
                id VARCHAR(50) PRIMARY KEY,
                nome VARCHAR(100),
                ativa BOOLEAN DEFAULT true,
                bio TEXT,
                atividades JSONB,
                permissoes JSONB,
                fontes JSONB,
                conexoes JSONB
            )
        ''')
        
        # Criar índices para melhor performance
        cur.execute('''
            CREATE INDEX IF NOT EXISTS idx_ia_logs_timestamp 
            ON ia_logs(timestamp DESC)
        ''')
        
        cur.execute('''
            CREATE INDEX IF NOT EXISTS idx_ia_logs_ia_nome 
            ON ia_logs(ia_nome)
        ''')
        
        conn.commit()
        print("✅ Banco de dados inicializado com sucesso")
    except Exception as e:
        print(f"❌ Erro ao inicializar banco: {e}")
        conn.rollback()
    finally:
        cur.close()
        return_db_connection(conn)

# Decorator para autenticação (opcional - ativar em produção)
def require_api_key(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        # Se API_KEY não estiver configurada, permite acesso (para facilitar testes)
        api_key_env = os.getenv('API_KEY')
        if api_key_env:
            api_key = request.headers.get('X-API-Key')
            if api_key != api_key_env:
                return jsonify({"erro": "Não autorizado"}), 401
        return f(*args, **kwargs)
    return decorated_function

class IA:
    """Classe base para todas as IAs"""
    
    def __init__(self, nome, funcao, prioridade="media"):
        self.nome = nome
        self.funcao = funcao
        self.prioridade = prioridade
    
    def executar(self, tarefa):
        """Executa tarefa usando GPT-4 Turbo"""
        try:
            # Validação de entrada
            if not tarefa or len(tarefa.strip()) < 5:
                return {"erro": "Tarefa muito curta ou vazia"}
            
            # Usar gpt-4-turbo para melhor custo-benefício
            response = client.chat.completions.create(
                model="gpt-4-turbo",
                messages=[
                    {"role": "system", "content": f"Você é {self.nome}, {self.funcao}. Seja objetivo e eficiente nas respostas."},
                    {"role": "user", "content": tarefa}
                ],
                max_tokens=500,  # Limitar tokens para controlar custos
                temperature=0.7
            )
            
            resultado = response.choices[0].message.content
            self.registrar_log(tarefa, resultado, "sucesso")
            return resultado
            
        except Exception as e:
            erro_msg = f"Erro: {str(e)}"
            self.registrar_log(tarefa, erro_msg, "erro")
            return erro_msg
    
    def registrar_log(self, acao, resultado, status="sucesso"):
        """Registra ação no banco"""
        try:
            conn = get_db_connection()
            cur = conn.cursor()
            cur.execute(
                "INSERT INTO ia_logs (ia_nome, acao, resultado) VALUES (%s, %s, %s)",
                (self.nome, f"[{status.upper()}] {acao[:200]}", resultado[:1000])
            )
            conn.commit()
            cur.close()
            return_db_connection(conn)
        except Exception as e:
            print(f"❌ Erro ao registrar log: {e}")

# Instanciar todas as 15 IAs
ias = {
    # Prioridade Máxima
    "bia": IA("BIA", "Líder Desenvolvedora que coordena todo o exército de IAs", "maxima"),
    "anna-laura": IA("Anna Laura", "Especialista em Vendas++ que analisa preços e estratégias de vendas", "maxima"),
    
    # Prioridade Alta
    "vigilante": IA("Vigilante", "Monitor de Leads que detecta leads sem resposta", "alta"),
    "reativador": IA("Reativador", "Especialista em Reativação que recupera leads inativos", "alta"),
    "marketeiro": IA("Marketeiro", "Criador de Conteúdo que gera posts e vídeos", "alta"),
    "competidor": IA("Competidor", "Analista de Concorrência que monitora o mercado", "alta"),
    "analista-dados": IA("Analista de Dados", "Análise de Leads e métricas do Kommo", "alta"),
    "qualificador": IA("Qualificador", "Classificação de Leads em A/B/C", "alta"),
    "fiscal-crm": IA("Fiscal do CRM", "Garantia de Qualidade de Dados no CRM", "alta"),
    "organizador-patio": IA("Organizador de Pátio", "Controle de Pátio com máximo 30% de iscas", "alta"),
    "estrategista-iscas": IA("Estrategista de Iscas", "Monitor de Conversão com mínimo 60%", "alta"),
    
    # Prioridade Média
    "dedo-duro": IA("Dedo Duro", "Detector de Inconsistências e falhas no processo", "media"),
    "analista-preco": IA("Analista de Preço", "Monitor de Mercado e preços da concorrência", "media"),
    "analista-tecnico": IA("Analista Técnico", "Especialista em Diagnóstico e fluxo técnico", "media"),
    "casanova": IA("Casanova", "Recompensa de Meta - arma secreta motivacional", "media"),
}

@app.route('/')
def home():
    return jsonify({
        "status": "online",
        "exercito": "Exército de IAs - Doctor Prime 2026",
        "versao": "1.1.0",
        "ias_disponiveis": list(ias.keys()),
        "total_ias": len(ias),
        "endpoints": {
            "executar_ia": "POST /api/ia/{nome}/executar",
            "listar_ias": "GET /api/ias",
            "logs": "GET /api/logs",
            "health": "GET /health"
        }
    })

@app.route('/api/ias', methods=['GET'])
def listar_ias():
    """Lista todas as IAs disponíveis"""
    return jsonify({
        "total": len(ias),
        "ias": [
            {
                "id": key,
                "nome": ia.nome,
                "funcao": ia.funcao,
                "prioridade": ia.prioridade
            }
            for key, ia in ias.items()
        ]
    })

@app.route('/api/ia/<nome>/executar', methods=['POST'])
@require_api_key
def executar_ia(nome):
    """Endpoint para executar uma IA"""
    try:
        data = request.json
        
        # Validação de entrada
        if not data or 'tarefa' not in data:
            return jsonify({"erro": "Campo 'tarefa' é obrigatório"}), 400
        
        tarefa = data.get('tarefa', '').strip()
        
        if not tarefa or len(tarefa) < 5:
            return jsonify({"erro": "Tarefa muito curta (mínimo 5 caracteres)"}), 400
        
        if len(tarefa) > 2000:
            return jsonify({"erro": "Tarefa muito longa (máximo 2000 caracteres)"}), 400
        
        # Buscar IA
        ia = ias.get(nome.lower())
        if not ia:
            return jsonify({
                "erro": "IA não encontrada",
                "ias_disponiveis": list(ias.keys())
            }), 404
        
        # Executar tarefa
        resultado = ia.executar(tarefa)
        
        return jsonify({
            "ia": ia.nome,
            "tarefa": tarefa,
            "resultado": resultado,
            "timestamp": datetime.now().isoformat()
        })
        
    except Exception as e:
        return jsonify({"erro": f"Erro interno: {str(e)}"}), 500

@app.route('/api/logs', methods=['GET'])
def get_logs():
    """Retorna logs das IAs"""
    try:
        limit = request.args.get('limit', 50, type=int)
        limit = min(limit, 200)  # Máximo 200 logs
        
        ia_nome = request.args.get('ia_nome', None)
        
        conn = get_db_connection()
        cur = conn.cursor()
        
        if ia_nome:
            cur.execute(
                "SELECT * FROM ia_logs WHERE ia_nome = %s ORDER BY timestamp DESC LIMIT %s",
                (ia_nome, limit)
            )
        else:
            cur.execute(
                "SELECT * FROM ia_logs ORDER BY timestamp DESC LIMIT %s",
                (limit,)
            )
        
        logs = cur.fetchall()
        cur.close()
        return_db_connection(conn)
        
        return jsonify({
            "total": len(logs),
            "logs": [
                {
                    "id": log[0],
                    "ia_nome": log[1],
                    "acao": log[2],
                    "resultado": log[3],
                    "timestamp": log[4].isoformat()
                }
                for log in logs
            ]
        })
        
    except Exception as e:
        return jsonify({"erro": f"Erro ao buscar logs: {str(e)}"}), 500

@app.route('/health')
def health():
    """Health check"""
    try:
        # Testar conexão com banco
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("SELECT 1")
        cur.close()
        return_db_connection(conn)
        
        return jsonify({
            "status": "healthy",
            "database": "connected",
            "timestamp": datetime.now().isoformat()
        })
    except Exception as e:
        return jsonify({
            "status": "unhealthy",
            "database": "disconnected",
            "erro": str(e)
        }), 503

if __name__ == '__main__':
    # Inicializa pool de conexões
    init_connection_pool()
    
    # Inicializa banco na primeira execução
    init_db()
    
    # Roda servidor
    port = int(os.getenv('PORT', 5000))
    debug = os.getenv('DEBUG', 'false').lower() == 'true'
    
    print(f"🚀 Servidor iniciando na porta {port}")
    print(f"🤖 {len(ias)} IAs carregadas")
    
    app.run(host='0.0.0.0', port=port, debug=debug)
