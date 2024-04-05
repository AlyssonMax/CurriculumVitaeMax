import streamlit as st
import pandas as pd

st.set_page_config(page_title="Quem é Alysson 'MAX' Bárbara")
st.write("---")

#cria um container de apresentação
with st.container():
    st.subheader("Curriculum Vitae")
    st.title("Quem é Alysson 'MAX' Bárbara")

#texto de apresentação
st.write("---")
st.write("Olá! Me chamo Alysson, um engenheiro de dados entusiasmado e dedicado. Como mineiro que sou, trago para o trabalho a mesma paixão que tenho pela vida familiar. Casado e pai orgulhoso de dois filhos. Desde setembro de 2021, venho me aplicando para não apenas crescer profissionalmente, mas também para contribuir com as equipes próximas a mim. Estou sempre em busca de crescimento na minha área e, atualmente, estou focado em aprimorar minhas habilidades em plataformas líderes de mercado como Databricks, Azure e AWS, além de aprofundar meu conhecimento na linguagem Python. Acredito que a constante evolução técnica e a troca de experiências são fundamentais para o sucesso, e é nisso que baseio minha jornada profissional.")

#cria uma função para carregar os dados fora do container
#armazena os dados em cache para que não seja necessário recarregar numa segunda execução
@st.cache_data
def carrega_dados1():
    tabela_skill = pd.read_csv("SKILLS.csv")
    return tabela_skill

@st.cache_data
def carrega_dados2():
    tabela_curso = pd.read_excel("Cursos.xlsx")
    return tabela_curso
st.write("---")

#tabela de cursos
st.write("CURSOS / CERTIFICADOS / GRADUAÇÕES")
st.write("---")
with st.container():
    df=carrega_dados2()
    st.dataframe(df)

st.write("---")

#cria um container para criar um gráfico para habilidades
st.write("HABILIDADES E PROFICIÊNCIA")
st.write("---")
with st.container():
    dados=carrega_dados1()
    st.bar_chart(dados, x="Nível", y="Habilidade",color="Nível")
    st.write("LEGENDA:")
    st.write("1-Iniciante")
    st.write("2-Apto")
    st.write("3-Intermediário")
    st.write("4-Competente")
    st.write("5-Experiente")
    st.write("6-Avançado")
    st.write("7-Diferenciado")
    st.write("8-Mestre")
st.write("---")
#lista de soft Skills
with st.container():
    st.write("SOFT SKILLS")
    st.write("---")
    st.write("Flexibilidade: Adaptabilidade a novos ambientes e desafios.")

    st.write("Resiliência Profissional: Habilidade de lidar com pressão e superar obstáculos.")

    st.write("Aprendizado Contínuo: Compromisso com o desenvolvimento pessoal e profissional.")

    st.write("Atuação junto de agentes multidisciplinares")

    st.write("Resolução de Problemas: Identificar problemas e implementar soluções eficazes1.")

    st.write("Ética de Trabalho: Demonstrar comprometimento, responsabilidade e dedicação ao trabalho")

st.write("---")
with st.container():
    st.write("LinkedIn pelo [LINK](https://www.linkedin.com/in/alyssonbarbara/)")

    st.write("Whatsapp pelo [LINK](https://wa.me/qr/QBC2WTSAJTDBN1)")
st.write("---")