import streamlit as st
import requests

# URL da API
BASE_URL = "http://127.0.0.1:8000"

# Função para exibir os detalhes de cada previsão
def display_prediction(prediction):
    st.write(f"### {prediction['city'].capitalize()}")
    st.write(f"**ID**: {prediction['id']}")
    st.write(f"**Data da consulta**: {prediction['date'].split('T')[0]}")
    st.write(f"**Detalhes**: {prediction['description']}")
    st.write(f"**Temperatura**: {prediction['temperature']}°C")
    st.write(f"**Umidade**: {prediction['humidity']}%")
    st.write("---")

# Função para criar previsão
def create_prediction():
    st.title("📌 Criar Previsão")
    city = st.text_input("Digite o nome da cidade:")
    if st.button("Criar Previsão"):
        if city:
            response = requests.post(f"{BASE_URL}/predictions/", params={"city": city})
            if response.status_code == 201:
                st.success("Previsão criada com sucesso!")
            else:
                st.error(f"Erro: {response.json().get('detail')}")
        else:
            st.error("Por favor, insira o nome da cidade.")

# Função para consultar todas as previsões
def get_all_predictions():
    st.title("📌 Consultar Todas as Previsões")
    if st.button("Consultar"):
        response = requests.get(f"{BASE_URL}/predictions/")
        if response.status_code == 200:
            predictions = response.json()
            predictions.reverse()
            if predictions:
                for prediction in predictions:
                    display_prediction(prediction)
            else:
                st.info("Nenhuma previsão encontrada.")
        else:
            st.error("Erro ao consultar previsões.")

# Função para filtrar previsões por cidade e data
def filter_predictions():
    st.title("📌 Filtrar Previsões")
    city = st.text_input("Digite o nome da cidade:")
    date = st.text_input("Digite a data (DD/MM/YYYY):")
    if st.button("Filtrar Previsões"):
        params = {}
        if city:
            params["city"] = city
        if date:
            params["date"] = date
        
        response = requests.get(f"{BASE_URL}/predictions/filter", params=params)
        if response.status_code == 200:
            prediction = response.json()
            if prediction:
                display_prediction(prediction)
            else:
                st.info("Nenhuma previsão encontrada para os critérios informados.")
        else:
            st.error(f"Erro: {response.json().get('detail')}")

# Função para deletar previsão
def delete_prediction():
    st.title("📌 Deletar Previsão")
    prediction_id = st.number_input("Digite o ID da previsão a ser deletada:", min_value=1)
    if st.button("Deletar Previsão"):
        if prediction_id:
            response = requests.delete(f"{BASE_URL}/predictions/delete/{prediction_id}")
            if response.status_code == 200:
                st.success("Previsão deletada com sucesso!")
            else:
                st.error(f"Erro: {response.json().get('detail')}")
        else:
            st.error("Por favor, insira um ID válido.")

# Função principal que exibe todas as seções
def main():
    st.sidebar.title("Navegação")
    selection = st.sidebar.radio("Escolha uma ação", ["Criar Previsão", "Consultar Todas as Previsões", "Filtrar Previsões", "Deletar Previsão"])

    if selection == "Criar Previsão":
        create_prediction()
    elif selection == "Consultar Todas as Previsões":
        get_all_predictions()
    elif selection == "Filtrar Previsões":
        filter_predictions()
    elif selection == "Deletar Previsão":
        delete_prediction()

if __name__ == "__main__":
    main()
