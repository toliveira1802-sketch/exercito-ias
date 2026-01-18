# 🚀 Deploy Rápido no Railway

## Guia Express - 10 Minutos

---

## ✅ Pré-requisitos

1. **Conta GitHub** (gratuita) - https://github.com
2. **Conta Railway** (gratuita) - https://railway.app
3. **Chave OpenAI** - https://platform.openai.com/api-keys

---

## 📝 Passo 1: Criar Repositório GitHub

### Via Interface Web (Mais Fácil)

1. Acesse https://github.com/new
2. Nome: `exercito-ias`
3. Visibilidade: **Private** ✅
4. Clique em **"Create repository"**
5. Na página do repositório, clique em **"uploading an existing file"**
6. Arraste TODOS os arquivos desta pasta
7. Commit message: `Initial deploy`
8. Clique em **"Commit changes"**

✅ **Repositório criado!**

---

## 🚂 Passo 2: Deploy no Railway

### 2.1 Criar Projeto

1. Acesse https://railway.app
2. Login com GitHub
3. Clique em **"New Project"**
4. Selecione **"Deploy from GitHub repo"**
5. Escolha `exercito-ias`

### 2.2 Adicionar PostgreSQL

1. No projeto, clique em **"+ New"**
2. Selecione **"Database"** → **"Add PostgreSQL"**
3. Aguarde criar (30 segundos)

### 2.3 Configurar Variáveis

1. Clique no serviço principal (Python)
2. Vá em **"Variables"**
3. Adicione:

```
OPENAI_API_KEY=sk-proj-sua-chave-aqui
ENVIRONMENT=production
DEBUG=false
```

**Nota:** `DATABASE_URL` é adicionada automaticamente pelo Railway

### 2.4 Gerar Domínio Público

1. Ainda no serviço Python
2. Vá em **"Settings"**
3. Em **"Networking"**, clique em **"Generate Domain"**
4. Copie a URL (exemplo: `exercito-ias-production.up.railway.app`)

---

## ✅ Passo 3: Testar

### Teste 1: Health Check

Abra no navegador:
```
https://SEU-DOMINIO.railway.app/health
```

Deve retornar:
```json
{
  "status": "healthy",
  "database": "connected"
}
```

### Teste 2: Listar IAs

```
https://SEU-DOMINIO.railway.app/
```

Deve mostrar 15 IAs disponíveis!

### Teste 3: Executar uma IA

Use Postman, Insomnia ou curl:

```bash
curl -X POST https://SEU-DOMINIO.railway.app/api/ia/bia/executar \
  -H "Content-Type: application/json" \
  -d '{"tarefa": "Analise o status do sistema"}'
```

---

## 🎉 Pronto!

Seu Exército de IAs está no ar!

**URL do seu sistema:** `https://SEU-DOMINIO.railway.app`

---

## 📊 Próximos Passos

### Opcional: Adicionar Segurança

Para proteger os endpoints, adicione nas variáveis do Railway:

```
API_KEY=sua-chave-secreta-aqui
```

Depois, nas requisições, adicione o header:
```
X-API-Key: sua-chave-secreta-aqui
```

### Monitorar Logs

1. No Railway, clique no serviço
2. Vá em **"Deployments"**
3. Clique no deployment ativo
4. Veja logs em tempo real

### Ver Custos

1. No Railway, menu lateral
2. Clique em **"Usage"**
3. Monitore consumo

---

## 🆘 Problemas Comuns

### Build falhou
- Verifique se todos os arquivos foram enviados ao GitHub
- Veja os logs de erro no Railway

### Database error
- Certifique-se que o PostgreSQL está rodando
- Verifique se `DATABASE_URL` está nas variáveis

### OpenAI error
- Confirme que `OPENAI_API_KEY` está correta
- Verifique se tem créditos na conta OpenAI

---

## 📞 Suporte

- Railway Docs: https://docs.railway.app
- OpenAI Docs: https://platform.openai.com/docs

---

**Desenvolvido por Doctor Prime 2026**
