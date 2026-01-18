# 🤖 Exército de IAs - Doctor Prime 2026

Sistema de automação inteligente para oficinas premium com 15 IAs especializadas.

---

## 🎯 O que é?

O Exército de IAs é um sistema completo de automação que utiliza inteligência artificial para gerenciar e otimizar operações de oficinas automotivas premium. Com 15 agentes especializados, o sistema cobre desde monitoramento de leads até análise de mercado e gestão de pátio.

---

## 👥 As 15 IAs

### Prioridade Máxima
- 👑 **BIA** - Líder Desenvolvedora (coordena todo o exército)
- 💰 **Anna Laura** - Especialista em Vendas++ (análise de preços e estratégias)

### Prioridade Alta
- 🚨 **Vigilante** - Monitor de Leads (detecta leads sem resposta)
- 🔄 **Reativador** - Especialista em Reativação (recupera leads inativos)
- 📱 **Marketeiro** - Criador de Conteúdo (gera posts e vídeos)
- 🔍 **Competidor** - Analista de Concorrência (monitora mercado)
- 📊 **Analista de Dados** - Análise de Leads (161 leads do Kommo)
- 🎯 **Qualificador** - Classificação de Leads (A/B/C)
- 📝 **Fiscal do CRM** - Qualidade de Dados (garante dados limpos)
- 🏗️ **Organizador de Pátio** - Controle de Pátio (máx 30% iscas)
- 📈 **Estrategista de Iscas** - Monitor de Conversão (mín 60%)

### Prioridade Média
- 🕵️ **Dedo Duro** - Detector de Inconsistências (falhas no processo)
- 💵 **Analista de Preço** - Monitor de Mercado (preços concorrência)
- 🔧 **Analista Técnico** - Especialista em Diagnóstico (fluxo técnico)
- 💘 **Casanova** - Recompensa de Meta (arma secreta)

---

## 🚀 Como Funciona

```
Kommo CRM → IAs Analisam → GPT-4 Processa → IAs Executam → WhatsApp/Email
```

1. **Coleta de Dados:** IAs buscam informações do Kommo, WhatsApp, etc
2. **Análise Inteligente:** GPT-4 processa e sugere ações
3. **Execução:** IAs executam tarefas automaticamente
4. **Registro:** Tudo é logado no banco de dados
5. **Relatórios:** Dashboard mostra resultados em tempo real

---

## 💻 Tecnologias

- **Backend:** Python 3.11 + Flask
- **IA:** OpenAI GPT-4
- **Banco de Dados:** PostgreSQL
- **Deploy:** Railway
- **Integrações:** Kommo CRM, WhatsApp Business API

---

## 📦 Estrutura do Projeto

```
exercito-railway/
├── main.py              # Servidor Flask + IAs
├── database.py          # Configuração do banco
├── requirements.txt     # Dependências Python
├── railway.json         # Config Railway
├── Procfile            # Comando de start
├── .env.example        # Exemplo de variáveis
├── GUIA_DEPLOY_RAILWAY.md  # Guia completo de deploy
└── README.md           # Este arquivo
```

---

## 🔧 Instalação Local (Desenvolvimento)

```bash
# 1. Clone o repositório
git clone https://github.com/seu-usuario/exercito-ias.git
cd exercito-ias

# 2. Crie ambiente virtual
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate  # Windows

# 3. Instale dependências
pip install -r requirements.txt

# 4. Configure variáveis de ambiente
cp .env.example .env
# Edite .env com suas chaves

# 5. Configure banco de dados
python database.py

# 6. Rode o servidor
python main.py
```

Acesse: http://localhost:5000

---

## 🚂 Deploy no Railway

Siga o guia completo em: [GUIA_DEPLOY_RAILWAY.md](./GUIA_DEPLOY_RAILWAY.md)

**Resumo:**
1. Criar repositório GitHub
2. Fazer upload do código
3. Criar projeto no Railway
4. Adicionar PostgreSQL
5. Configurar variáveis de ambiente
6. Deploy automático

**Custo:** ~$20/mês (após $5 de crédito inicial)

---

## 🔑 Variáveis de Ambiente

```env
# OpenAI
OPENAI_API_KEY=sk-proj-...

# Database (Railway fornece)
DATABASE_URL=postgresql://...

# Kommo CRM
KOMMO_API_KEY=...
KOMMO_DOMAIN=...

# WhatsApp
WHATSAPP_TOKEN=...
WHATSAPP_PHONE_ID=...

# Config
ENVIRONMENT=production
DEBUG=false
```

---

## 📡 API Endpoints

### Status
```
GET /
GET /health
```

### Executar IA
```
POST /api/ia/{nome}/executar
Body: {"tarefa": "sua tarefa aqui"}
```

### Logs
```
GET /api/logs
```

---

## 📊 Banco de Dados

### Tabelas Principais

- `ias` - Configuração das IAs
- `ia_logs` - Histórico de ações
- `ia_atividades` - Tarefas de cada IA
- `ia_permissoes` - Permissões configuráveis
- `ia_fontes` - Fontes de conhecimento
- `ia_conexoes` - Conexões entre IAs
- `leads` - Leads do Kommo
- `metricas` - Métricas de performance

---

## 🔒 Segurança

- ✅ Variáveis de ambiente para chaves sensíveis
- ✅ Repositório privado recomendado
- ✅ Autenticação em endpoints críticos
- ✅ Logs de todas as ações
- ✅ 2FA no GitHub e Railway

---

## 📈 Roadmap

### Fase 1 (Atual)
- [x] Sistema base com 15 IAs
- [x] Integração OpenAI GPT-4
- [x] Banco de dados PostgreSQL
- [x] Deploy Railway

### Fase 2 (Próxima)
- [ ] Integração Kommo CRM
- [ ] WhatsApp Business API
- [ ] Dashboard frontend
- [ ] Sistema de alertas

### Fase 3 (Futuro)
- [ ] Análise preditiva
- [ ] Automação completa
- [ ] Multi-oficina
- [ ] App mobile

---

## 🆘 Suporte

**Problemas?**
- Veja [GUIA_DEPLOY_RAILWAY.md](./GUIA_DEPLOY_RAILWAY.md)
- Fale com a BIA no dashboard
- Abra uma issue no GitHub

**Dúvidas sobre APIs:**
- Railway: https://docs.railway.app
- OpenAI: https://platform.openai.com/docs
- Kommo: https://www.kommo.com/developers

---

## 📄 Licença

Propriedade de Doctor Prime 2026. Todos os direitos reservados.

---

## 👨‍💻 Desenvolvido por

**Doctor Prime** - Oficinas Premium
**Minato Namithales** - Arquitetura e Desenvolvimento

---

**Versão:** 1.0.0  
**Última atualização:** Janeiro 2026
