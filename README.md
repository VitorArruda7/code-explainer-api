# 📝 Code Explainer API

Uma API para explicar trechos de código usando um modelo mockado (com estrutura preparada para integração com OpenAI). Desenvolvida com **FastAPI**, seguindo práticas de Clean Architecture, testes automatizados com **pytest**, e pronta para deploy com **Docker**.

---

## 🚀 **Features**

- ✅ Endpoint `POST /explain` para explicar trechos de código  
- ✅ Estrutura modular (services, routes, models)  
- ✅ Testes automatizados com Pytest  
- ✅ Mock de resposta para desenvolvimento local sem custos de API  
- ✅ Deploy containerizado com Docker

---

## 🛠 **Tecnologias**

- Python 3.11
- FastAPI
- Uvicorn
- Pydantic v1
- Pytest
- Docker + Docker Compose
- Dotenv

---

## 📁 **Estrutura de diretórios**

```bash
code-explainer-api/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── models/
│   │   └── code_models.py
│   ├── routes/
│   │   └── code_routes.py
│   └── services/
│       ├── __init__.py
│       └── code_service.py
├── tests/
│   ├── __init__.py
│   ├── test_code_service.py
│   └── test_routes.py
├── .env.example
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
```

---

## ⚙️ **Como rodar localmente**

1. **Clone o repositório**

```bash
git clone https://github.com/VitorArruda7/code-explainer-api.git
cd code-explainer-api 
```

2. **Crie e ative um ambiente virtual**

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/macOS
source venv/bin/activate
```

3. **Instale as dependências**

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

4. **Crie um arquivo .env**

- Copie o conteúdo do .env.example e ajuste se necessário.

5. **Inicie a API**
```bash
uvicorn app.main:app --reload
```

6. **Acesse a documentação interativa**
```bash
http://localhost:8000/docs
```
## 🐳 Como rodar com Docker

1. **Build e up**
```bash
docker compose up --build
```
2. **Acesse a API**
```bash
http://localhost:8000/docs
```
## ✅ Testes
- Para rodar os testes automatizados
```bash
pytest
```

## 📌 Endpoints disponíveis

- POST /explain
- Descrição: Explica o trecho de código enviado

- Body params:
```bash
{
  "code_snippet": "print('Hello World')",
  "language": "python"
}
```

- Response:
```bash
{
  "explanation": "Este trecho imprime 'Hello World' no console."
}
```
