import streamlit as st
from save_model_manager import SaveModelManager
from maps import sexo_map, fumante_map, regiao_map
import constants as Constants
import pandas as pd

model_saved = SaveModelManager.load_model("./model/my_model.pkl")
df_final = pd.read_csv('./data/final.csv')

st.title("Previsão de custo de plano de saúde")

sexo_map_inverso = {v: k for k, v in sexo_map.items()} 
fumante_map_inverso = {v: k for k, v in fumante_map.items()} 
regiao_map_inverso = {v: k for k, v in regiao_map.items()}

with st.form(key='predict_form'):
    idade = st.number_input('Idade', min_value=Constants.MIN_AGE, max_value=Constants.MAX_AGE, value=25)
    sexo = st.selectbox('Sexo', options=sexo_map.values(), format_func=lambda x: f'{sexo_map_inverso.get(x).capitalize()}')
    imc = st.number_input('IMC', min_value=Constants.MIN_IMC, max_value=Constants.MAX_IMC, value=25.0)
    criancas = st.number_input('Número de crianças', min_value=Constants.MIN_CHILDREN, max_value=Constants.MAX_CHILDREN, value=0)
    fumante = st.selectbox('Fumante', options=fumante_map.values(), format_func=lambda x: f'{fumante_map_inverso.get(x).capitalize()}')
    regiao = st.selectbox('Região', options=regiao_map.values(), format_func=lambda x: f'{regiao_map_inverso.get(x).capitalize()}')

    submit_button = st.form_submit_button(label='Prever custo')

    if submit_button:
        data = pd.DataFrame({
            'idade': [idade],
            'imc': [imc],
            'criancas': [criancas],
            'sexo_1': [bool(sexo)],
            'fumante_1': [bool(fumante)],
            'regiao_1': [regiao == 1],
            'regiao_2': [regiao == 2],
            'regiao_3': [regiao == 3],
            'regiao_4': [regiao == 4]
        })

        previsao = model_saved.predict(data)

        st.write(f'Valor estimado: R$ {previsao[0]:.2f}') 

st.subheader("Version 0.1.0 | created by Deyvid Jaguaribe")
st.subheader("* Dados simulados, veja mais sobre o projeto em: https://github.com/DeyvidJLira/fiap-iadev-project-fase1/tree/main")