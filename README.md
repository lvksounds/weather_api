# Weather API

![Python](https://img.shields.io/badge/Python-3.10-blue.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-0.100.0-green.svg)

API para previsão do tempo, desenvolvida com **FastAPI** e banco de dados **SQLite**.

## 📌 Funcionalidades

- Criar previsões do tempo com base em uma cidade.
- Consultar todas as previsões cadastradas.
- Filtrar previsões por cidade e data.
- Remover previsões do banco de dados.

## 🚀 Tecnologias utilizadas

- [Python](https://www.python.org/)
- [FastAPI](https://fastapi.tiangolo.com/)
- [SQLite](https://www.sqlite.org/index.html)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [HTTPX](https://www.python-httpx.org/)

## 📂 Estrutura do projeto

```
weather_api/
│-- app/
│   ├── infra/                # Configuração do banco de dados
│   ├── models/               # Modelos do SQLAlchemy
│   ├── routers/              # Rotas da API
│   ├── schemas/              # Schemas do Pydantic
│   ├── services/             # Serviços para comunicação externa (ex: consumo de API de clima)
│   ├── helpers/              # Funções auxiliares
│   ├── main.py               # Ponto de entrada da aplicação
│-- tests/                    # Testes automatizados
│-- README.md                 # Documentação do projeto
│-- requirements.txt          # Dependências do projeto
```

## ⚡ Como executar o projeto

### 1️⃣ Clonar o repositório
```bash
git clone https://github.com/seu-usuario/weather_api.git
cd weather_api
```

### 2️⃣ Criar um ambiente virtual e instalar dependências
```bash
python -m venv venv
source venv/bin/activate  # Para Linux/macOS
venv\Scripts\activate     # Para Windows
pip install -r requirements.txt
```

### 3️⃣ Rodar a aplicação
```bash
uvicorn app.main:app --reload
```
A API estará disponível em **http://127.0.0.1:8000**

### 4️⃣ Acessar a documentação interativa
FastAPI fornece uma documentação interativa disponível em:
- **Swagger UI**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **Redoc**: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

## 🧪 Como rodar os testes

### 1️⃣ Executar os testes com `pytest`
```bash
pytest tests/
```

## 📜 Licença
Este projeto é licenciado sob a licença MIT - veja o arquivo [LICENSE](LICENSE) para mais detalhes.

