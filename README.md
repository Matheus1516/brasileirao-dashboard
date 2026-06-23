# ⚽ Dashboard de Desempenho — Brasileirão

Dashboard interativo que analisa mais de 20 anos de partidas do Campeonato Brasileiro de Futebol, revelando padrões de desempenho dos times e o impacto real de jogar em casa.

🔗 **[Acesse o dashboard ao vivo aqui](https://dashboard-brasileirao.streamlit.app/)**

> 💡 **Nota:** Este app está hospedado no plano gratuito do Streamlit Cloud, 
> que "adormece" após período de inatividade. Se o link demorar para abrir 
> na primeira vez, basta aguardar 30 segundos que o servidor irá reativar.

## 🎯 Principais insights

- **Vantagem de jogar em casa é real e expressiva**: 49,6% das partidas terminam em vitória do time da casa, contra apenas 23,9% de vitórias do visitante.
- **Palmeiras e São Paulo** lideram o ranking histórico de aproveitamento de pontos desde 2003.

## 🛠️ Tecnologias utilizadas

- **Python** — linguagem principal
- **Pandas** — limpeza, transformação e agregação dos dados
- **Streamlit** — construção da interface web interativa
- **Plotly** — visualizações de dados (gráficos de barras e pizza)

## 📊 Sobre os dados

Dataset público com o histórico completo de partidas do Campeonato Brasileiro (2003–presente), incluindo placares, times, datas e estatísticas das partidas.
Fonte: [Brasileirao Dataset (GitHub)](https://github.com/adaoduque/Brasileirao_Dataset)

## 🚀 Como executar localmente

```bash
# Clone o repositório
git clone <link-do-seu-repositorio>
cd brasileirao-dashboard

# Crie e ative o ambiente virtual
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # Mac/Linux

# Instale as dependências
pip install -r requirements.txt

# Execute o dashboard
streamlit run src/app.py
```

## 📈 Funcionalidades

- Ranking de aproveitamento de pontos por time, com filtro interativo de quantidade
- Análise comparativa de resultados (vitória em casa vs. fora vs. empate)
- Tabela completa navegável com estatísticas de todos os times

## 💡 Possíveis melhorias futuras

- Análise por estado/região
- Comparação direta entre dois times escolhidos pelo usuário
- Inclusão de dados de temporadas mais recentes

## 👤 Autor

**Matheus Castro** — [LinkedIn](https://www.linkedin.com/in/matheus-castro-7678ba202/) — [GitHub](https://github.com/Matheus1516)