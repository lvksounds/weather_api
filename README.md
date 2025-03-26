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
- [Streamlit](https://streamlit.io/)

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
│-- streamlit_app/
│   ├── app.py                # Interface para visualização do consumo da api
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
### 3️⃣ Instale as dependências:

Certifique-se de que você tem o Python 3.8+ instalado. Em seguida, instale os pacotes necessários:

```bash
pip install -r requirements.txt
```

### 4️⃣ Rodar a aplicação
```bash
uvicorn app.main:app --reload
```
A API estará disponível em **http://127.0.0.1:8000**

### 5️⃣ Acessar a documentação interativa
FastAPI fornece uma documentação interativa disponível em:
- **Swagger UI**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **Redoc**: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

### 6️⃣ Rodar a aplicação Streamlit 🎨

Para visualizar a interface do Streamlit, utilize o comando abaixo:

```bash
streamlit run streamlit_app/app.py
```

Isso abrirá a aplicação Streamlit em http://localhost:8501, onde você pode interagir com a API e visualizar as previsões do tempo.

# 🚦 Endpoints da API 

### 1. **POST /predictions/**
   - **Descrição**: Cria uma previsão do tempo para uma cidade e armazena no banco de dados.
   - **Parâmetros**:
     - `city` (string): Nome da cidade para a qual a previsão será buscada.
   - **Resposta**:
     - Status: 201 - Previsão criada com sucesso.
     - Mensagem: "Previsão criada com sucesso."

---

### 2. **GET /predictions/**
   - **Descrição**: Retorna uma lista de todas as previsões do tempo armazenadas no banco de dados.
   - **Resposta**:
     - Status: 200 - Lista de previsões.
     - Exemplo de retorno: `[{"id": 1, "city": "São Paulo", "date": "2025-03-25", "forecast": "ensolarado"}, ...]`

---

### 3. **GET /predictions/filter**
   - **Descrição**: Retorna uma previsão do tempo armazenada no banco de dados de acordo com a cidade e a data informadas.
   - **Parâmetros**:
     - `city` (string, opcional): Nome da cidade.
     - `date` (string, opcional): Data no formato "DD/MM/YYYY".
   - **Resposta**:
     - Status: 200 - Json com o objeto da previsão.
     - Status: 404 - Caso a cidade ou data não seja fornecida ou a previsão não seja encontrada.
     - Mensagem: "Cidade não informada" ou "Data não informada" ou "Previsão não encontrada."

---

### 4. **DELETE /predictions/delete/{id}**
   - **Descrição**: Deleta uma previsão do tempo armazenada no banco de dados de acordo com o ID fornecido.
   - **Parâmetros**:
     - `id` (inteiro): ID da previsão a ser deletada.
   - **Resposta**:
     - Status: 200 - Previsão deletada com sucesso.


## 🧪 Rodando os testes 

Para rodar os testes deste projeto, use o seguinte comando:
```bash
pytest tests.py
```

