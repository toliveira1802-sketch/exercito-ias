# 🚂 Guia Completo de Deploy no Railway

## Exército de IAs - Doctor Prime 2026

---

## 📋 Pré-requisitos

Antes de começar, você precisa ter:

- Conta no GitHub (gratuita)
- Conta no Railway (gratuita - $5 de crédito inicial)
- Chave API da OpenAI (para as IAs funcionarem)

---

## 🎯 Passo 1: Criar Repositório no GitHub

### 1.1 Acessar GitHub
- Vá para https://github.com
- Faça login na sua conta

### 1.2 Criar Novo Repositório
- Clique em **"New repository"**
- Nome: `exercito-ias`
- Descrição: `Exército de IAs - Doctor Prime 2026`
- Visibilidade: **Private** (recomendado)
- Clique em **"Create repository"**

### 1.3 Fazer Upload dos Arquivos
Você tem 2 opções:

**OPÇÃO A: Via Interface Web (Mais Fácil)**
1. Na página do repositório, clique em **"uploading an existing file"**
2. Arraste todos os arquivos da pasta `exercito-railway`
3. Escreva mensagem: "Initial commit"
4. Clique em **"Commit changes"**

**OPÇÃO B: Via Git (Linha de Comando)**
```bash
cd /caminho/para/exercito-railway
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/SEU-USUARIO/exercito-ias.git
git push -u origin main
```

---

## 🚂 Passo 2: Deploy no Railway

### 2.1 Criar Conta no Railway
- Acesse https://railway.app
- Clique em **"Login"**
- Faça login com sua conta GitHub
- Autorize o Railway a acessar seus repositórios

### 2.2 Criar Novo Projeto
1. No dashboard do Railway, clique em **"New Project"**
2. Selecione **"Deploy from GitHub repo"**
3. Escolha o repositório `exercito-ias`
4. Railway detectará automaticamente que é um projeto Python

### 2.3 Adicionar Banco de Dados PostgreSQL
1. No seu projeto, clique em **"+ New"**
2. Selecione **"Database"**
3. Escolha **"PostgreSQL"**
4. Railway criará o banco automaticamente

### 2.4 Conectar Banco ao Código
1. Clique no serviço **PostgreSQL**
2. Vá na aba **"Variables"**
3. Copie a variável `DATABASE_URL`
4. Volte para o serviço principal (Python)
5. Vá em **"Variables"** → **"+ New Variable"**
6. Cole: `DATABASE_URL` = (valor copiado)

---

## 🔑 Passo 3: Configurar Variáveis de Ambiente

No serviço principal do Railway, adicione as seguintes variáveis:

### 3.1 OpenAI API
```
OPENAI_API_KEY = sk-proj-...
```
**Como obter:**
- Acesse https://platform.openai.com/api-keys
- Clique em **"Create new secret key"**
- Copie a chave (começa com `sk-proj-`)

### 3.2 Kommo CRM (Opcional - para depois)
```
KOMMO_API_KEY = sua-chave-kommo
KOMMO_DOMAIN = seudominio.kommo.com
```

### 3.3 WhatsApp Business API (Opcional - para depois)
```
WHATSAPP_TOKEN = seu-token
WHATSAPP_PHONE_ID = seu-phone-id
```

### 3.4 Configurações Gerais
```
ENVIRONMENT = production
DEBUG = false
PORT = 5000
```

---

## 🚀 Passo 4: Fazer Deploy

1. Após adicionar todas as variáveis, clique em **"Deploy"**
2. Railway começará o build automaticamente
3. Aguarde 2-5 minutos
4. Quando aparecer **"Success"**, está no ar! 🎉

---

## ✅ Passo 5: Testar o Sistema

### 5.1 Acessar URL do Projeto
1. No Railway, clique no seu serviço
2. Vá na aba **"Settings"**
3. Em **"Domains"**, clique em **"Generate Domain"**
4. Copie a URL (exemplo: `exercito-ias-production.up.railway.app`)

### 5.2 Testar Endpoints

**Teste 1: Health Check**
```
GET https://seu-dominio.railway.app/health
```
Resposta esperada:
```json
{"status": "healthy"}
```

**Teste 2: Listar IAs**
```
GET https://seu-dominio.railway.app/
```
Resposta esperada:
```json
{
  "status": "online",
  "exercito": "Exército de IAs - Doctor Prime 2026",
  "ias_disponiveis": ["BIA", "Anna Laura", "Vigilante", ...]
}
```

**Teste 3: Executar uma IA**
```
POST https://seu-dominio.railway.app/api/ia/bia/executar
Content-Type: application/json

{
  "tarefa": "Analise o status do sistema"
}
```

---

## 🔧 Passo 6: Configurar Banco de Dados

### 6.1 Rodar Migração Inicial
1. No Railway, vá no serviço principal
2. Clique em **"Settings"** → **"Deploy Triggers"**
3. Adicione comando de inicialização:
```
python database.py && python main.py
```

Ou rode manualmente via Railway CLI:
```bash
railway run python database.py
```

---

## 📊 Passo 7: Monitorar o Sistema

### 7.1 Ver Logs em Tempo Real
1. No Railway, clique no serviço
2. Vá na aba **"Deployments"**
3. Clique no deployment ativo
4. Veja os logs em tempo real

### 7.2 Métricas
- **CPU Usage:** Veja quanto está usando
- **Memory:** Monitore memória
- **Network:** Tráfego de entrada/saída

---

## 💰 Custos

### Plano Gratuito
- **$5 de crédito inicial**
- Suficiente para ~1 mês de testes
- Inclui PostgreSQL

### Plano Pago (após créditos)
- **~$20/mês** para uso moderado
- Inclui:
  - Servidor Python rodando 24/7
  - PostgreSQL com 1GB
  - 100GB de tráfego

---

## 🔒 Segurança

### Recomendações:
1. ✅ Mantenha repositório **Private**
2. ✅ Nunca commite chaves API no código
3. ✅ Use variáveis de ambiente sempre
4. ✅ Ative 2FA no GitHub e Railway
5. ✅ Monitore logs regularmente

---

## 🆘 Troubleshooting

### Problema: Build falhou
**Solução:**
- Verifique se `requirements.txt` está correto
- Veja logs de erro no Railway
- Certifique-se que `main.py` não tem erros

### Problema: Banco não conecta
**Solução:**
- Verifique se `DATABASE_URL` está configurada
- Confirme que PostgreSQL está rodando
- Teste conexão com: `railway run python database.py`

### Problema: IA não responde
**Solução:**
- Verifique se `OPENAI_API_KEY` está correta
- Confirme que tem créditos na OpenAI
- Veja logs de erro

### Problema: Deploy muito lento
**Solução:**
- Normal na primeira vez (5-10min)
- Próximos deploys são mais rápidos (1-2min)

---

## 🎯 Próximos Passos

Após deploy bem-sucedido:

1. **Integrar com Kommo**
   - Adicionar chaves API
   - Testar conexão
   - Configurar webhooks

2. **Conectar WhatsApp**
   - Configurar WhatsApp Business API
   - Testar envio de mensagens

3. **Adicionar Frontend**
   - Deploy do dashboard no Vercel/Netlify
   - Conectar com backend Railway

4. **Configurar Monitoramento**
   - Adicionar alertas
   - Dashboard de métricas
   - Logs estruturados

---

## 📞 Suporte

**Dúvidas?**
- Railway Docs: https://docs.railway.app
- OpenAI Docs: https://platform.openai.com/docs

**Precisa de ajuda?**
- Fale com a BIA no dashboard
- Ou volte aqui comigo (Minato) 😄

---

## ✅ Checklist Final

Antes de considerar o deploy completo:

- [ ] Repositório GitHub criado
- [ ] Código enviado pro GitHub
- [ ] Projeto criado no Railway
- [ ] PostgreSQL adicionado
- [ ] Variáveis de ambiente configuradas
- [ ] Deploy realizado com sucesso
- [ ] URL pública funcionando
- [ ] Banco de dados inicializado
- [ ] IAs respondendo corretamente
- [ ] Logs sendo gerados

---

**Parabéns! Seu Exército de IAs está no ar! 🚀**

*Guia criado por Minato Namithales para Doctor Prime 2026*
