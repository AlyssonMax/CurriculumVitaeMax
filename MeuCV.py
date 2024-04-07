import streamlit as st
import pandas as pd

st.set_page_config(page_title="Quem é Alysson 'MAX' Bárbara")
# Usando st.markdown com HTML para criar um divisor colorido
st.write("---")
#cria um container de apresentação
with st.container():
    st.subheader("Curriculum Vitae", divider='rainbow')
    st.title("Quem é _Alysson :blue['MAX'] Bárbara_")

#texto de apresentação
st.write("---")
st.write("Olá! Me chamo Alysson, um engenheiro de dados entusiasmado e dedicado. Como mineiro que sou, trago para o trabalho a mesma paixão que tenho pela vida familiar. Casado e pai orgulhoso de dois filhos. Desde setembro de 2021, venho me aplicando para não apenas crescer profissionalmente, mas também para contribuir com as equipes próximas a mim. Estou sempre em busca de crescimento na minha área e, atualmente, estou focado em aprimorar minhas habilidades em plataformas líderes de mercado como Databricks, Azure e AWS, além de aprofundar meu conhecimento na linguagem Python. Acredito que a constante evolução técnica e a troca de experiências são fundamentais para o sucesso, e é nisso que baseio minha jornada profissional.")

#cria uma função para carregar os dados fora do container
#armazena os dados em cache para que não seja necessário recarregar numa segunda execução
#@st.cache_data
def carrega_dados1():
    tabela_skill = pd.read_csv("SKILLS.csv")
    return tabela_skill

#@st.cache_data
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
    st.write("---")
    # textos da legenda
    legenda = 	"LEGENDA:", "1-Iniciante", "2-Apto", "3-Intermediário", "4-Competente", "5-Experiente", "6-Avançado", "7-Diferenciado", "8-Mestre"
    # imprime legenda
    for linha in legenda:
        st.write(linha)

st.write("---")
#lista de soft Skills
with st.container():
    st.write("SOFT SKILLS :handshake:")
    # Usando st.markdown com HTML para criar um divisor colorido
    st.markdown('<hr style="border:2px solid rainbow">', unsafe_allow_html=True)
    # lista das soft skills
    soft_skills = "Flexibilidade: Adaptabilidade a novos ambientes e desafios.";"Resiliência Profissional: Habilidade de lidar com pressão e superar obstáculos.";"Aprendizado Contínuo: Compromisso com o desenvolvimento pessoal e profissional.";"Atuação junto de agentes multidisciplinares";"Resolução de Problemas: Identificar problemas e implementar soluções eficazes1.";"Ética de Trabalho: Demonstrar comprometimento, responsabilidade e dedicação ao trabalho"
    # divide em linhas
    linhas = soft_skills.split(';')
    # imprime as linhas de soft skills
    for linha in linhas:
        st.write(linha)

st.write("---")
with st.container():
    st.write(":blue[LinkedIn] pelo [LINK](https://www.linkedin.com/in/alyssonbarbara/)")
    st.write("---")
    st.write(":green[Whatsapp] pelo [LINK](https://wa.me/qr/QBC2WTSAJTDBN1)")
st.write("---")