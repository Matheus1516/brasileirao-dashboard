import pandas as pd
import streamlit as st
import plotly.express as px

# Configuração da página
st.set_page_config(page_title="Dashboard Brasileirão", layout="wide")

# Título
st.title("⚽ Dashboard de Desempenho — Brasileirão")
st.markdown("Análise histórica de aproveitamento dos times no Campeonato Brasileiro")

# Carregar dados
@st.cache_data
def carregar_dados():
    df = pd.read_csv("data/campeonato-brasileiro-full.csv")
    return df

df = carregar_dados()

# Calcular pontos (mesma lógica do notebook)
def calcular_pontos(row, lado):
    if row['vencedor'] == row[lado]:
        return 3
    elif row['vencedor'] == '-':
        return 1
    else:
        return 0

df['pontos_mandante'] = df.apply(lambda row: calcular_pontos(row, 'mandante'), axis=1)
df['pontos_visitante'] = df.apply(lambda row: calcular_pontos(row, 'visitante'), axis=1)

# Calcular ranking
mandante_stats = df.groupby('mandante').agg(
    jogos_mandante=('pontos_mandante', 'count'),
    pontos_mandante=('pontos_mandante', 'sum')
).reset_index().rename(columns={'mandante': 'time'})

visitante_stats = df.groupby('visitante').agg(
    jogos_visitante=('pontos_visitante', 'count'),
    pontos_visitante=('pontos_visitante', 'sum')
).reset_index().rename(columns={'visitante': 'time'})

ranking = mandante_stats.merge(visitante_stats, on='time', how='outer').fillna(0)
ranking['total_jogos'] = ranking['jogos_mandante'] + ranking['jogos_visitante']
ranking['total_pontos'] = ranking['pontos_mandante'] + ranking['pontos_visitante']
ranking['aproveitamento'] = (ranking['total_pontos'] / (ranking['total_jogos'] * 3) * 100).round(2)
ranking = ranking.sort_values('aproveitamento', ascending=False)

# Filtro interativo na barra lateral
st.sidebar.header("Filtros")
qtd_times = st.sidebar.slider("Quantos times mostrar?", min_value=5, max_value=30, value=10)

# Mostrar gráfico
top_times = ranking.head(qtd_times)

fig = px.bar(
    top_times,
    x='aproveitamento',
    y='time',
    orientation='h',
    title=f'Top {qtd_times} times por aproveitamento (%)',
    text='aproveitamento'
)
fig.update_layout(yaxis={'categoryorder': 'total ascending'})

st.plotly_chart(fig, width='stretch')

# Mostrar tabela com os dados
st.subheader("Tabela completa")
st.dataframe(ranking[['time', 'total_jogos', 'total_pontos', 'aproveitamento']], width='stretch')

# Análise: vantagem de jogar em casa
st.subheader("🏠 Vantagem de jogar em casa?")

def classificar_resultado(row):
    if row['vencedor'] == row['mandante']:
        return 'Vitória do mandante (casa)'
    elif row['vencedor'] == '-':
        return 'Empate'
    else:
        return 'Vitória do visitante (fora)'

df['resultado'] = df.apply(classificar_resultado, axis=1)
contagem_resultado = df['resultado'].value_counts().reset_index()
contagem_resultado.columns = ['resultado', 'quantidade']

fig_resultado = px.pie(
    contagem_resultado,
    names='resultado',
    values='quantidade',
    title='Distribuição de resultados em todas as partidas do Brasileirão'
)
st.plotly_chart(fig_resultado, width='stretch')