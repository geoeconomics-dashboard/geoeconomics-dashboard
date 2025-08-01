
import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt

st.set_page_config(page_title="Geoeconomics Dashboard", layout="wide")
st.title("📊 Geoeconomics Dashboard — 2025")

data = [
    ["🌍 Geoeconomics (5C)", "IMF 2025: Индия — 3-я экономика мира; Африка +30 млн чел/год; Китай/Индия растут по KOF Globalisation Index", "📈", "2025-07"],
    ["🤖 Технологические сдвиги", "Stanford AI Index: США 40 AI моделей, Китай 15", "📈", "2025-07"],
]

df = pd.DataFrame(data, columns=["Блок", "Описание", "Тренд", "Обновлено"])

selected_block = st.selectbox("Выберите блок для анализа:", df["Блок"])
block_data = df[df["Блок"] == selected_block].iloc[0]

st.subheader(f"{block_data['Тренд']} {block_data['Блок']}")
st.markdown(f"**Описание:** {block_data['Описание']}")
st.markdown(f"**Дата обновления:** {block_data['Обновлено']}")

if selected_block == "🤖 Технологические сдвиги":
    years = list(range(2018, 2026))
    investments = [10, 15, 20, 35, 55, 75, 120, 150]
    fig, ax = plt.subplots()
    ax.plot(years, investments, marker="o")
    ax.set_title("Глобальные инвестиции в AI (млрд $)")
    st.pyplot(fig)
