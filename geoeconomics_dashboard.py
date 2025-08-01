
import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import numpy as np

# Настройки страницы
st.set_page_config(page_title="Geoeconomics Dashboard", layout="wide")
st.title("📊 Geoeconomics Dashboard — 2025 + Прогнозы до 2030")
st.markdown("Актуализация глобальных трендов, графики, прогнозы и карта точек роста.")

# Данные
data = [
    ["🌍 Geoeconomics (5C)", "IMF 2025: Индия — 3-я экономика мира; Африка +30 млн чел/год; Китай/Индия растут по KOF Globalisation Index", "📈", "2025-07"],
    ["⚔ Конфликты и безопасность", "GPI 2024: ухудшение в Украине, Йемене, Тайване; SIPRI: США 3% ВВП, Китай 2,2%; ACLED: рост конфликтов в Сахеле +15%", "📉", "2025-07"],
    ["🏙 Города и урбанизация", "Oxford Economics 2025: NY, London, Paris лидеры; Melbourne, Sydney в топ-10; GPCI: London, NY, Tokyo", "📈", "2025-07"],
    ["📖 Наративы и тренды", "Google Trends: рост запросов по AI, ESG; Edelman Trust: доверие к бизнесу > к правительству", "➡", "2025-07"],
    ["🧬 Антропоэкономика", "Gen Z: ценность — миссия > зарплата; Silver Economy: рост населения 65+; Pew: толерантность +7%", "📈", "2025-07"],
    ["♻ ESG и SDG", "SDG Tracker: РФ выполнила 13/17 целей; ESG фонды +20% в 2024; MSCI ESG Leaders обгоняют рынок", "📈", "2025-07"],
    ["🤖 Технологические сдвиги", "Stanford AI Index: США 40 AI моделей, Китай 15; WIPO: Китай 24% биопатентов, США 28%", "📈", "2025-07"],
    ["⚡ Критические ресурсы", "USGS: Китай и Чили лидеры по литий; FAO: Африка в дефиците воды; EIU: рост риска продбезопасности", "➡", "2025-07"],
    ["💰 Финансовые потоки", "GFCI 37 (2025): NY, London, HK лидеры; UNCTAD: FDI в развивающиеся страны +8%", "📈", "2025-07"],
    ["🌡 Климат и миграция", "Germanwatch: Пакистан, Бангладеш, Гаити — в топ риска; UNHCR: 34 млн климатических мигрантов к 2030", "📉", "2025-07"],
    ["🎭 Социально-культурные сдвиги", "WHR 2024: счастье коррелирует с доверием; Euromonitor: Gen Z — 40% за бренды с ценностями", "📈", "2025-07"],
    ["📰 Медийные тренды", "Freedom House: снижение свободы интернета; Statista: соцсети >50% медиапотребления", "➡", "2025-07"]
]

df = pd.DataFrame(data, columns=["Блок", "Описание", "Тренд", "Обновлено"])

# Выбор блока
selected_block = st.selectbox("Выберите блок для анализа:", df["Блок"])
block_data = df[df["Блок"] == selected_block].iloc[0]

st.subheader(f"{block_data['Тренд']} {block_data['Блок']}")
st.markdown(f"**Описание:** {block_data['Описание']}")
st.markdown(f"**Дата обновления:** {block_data['Обновлено']}")

# Показывать ли прогноз
show_forecast = st.checkbox("Показать прогноз до 2030 года", value=True)

# Пример графиков с прогнозами
if selected_block == "🤖 Технологические сдвиги":
    years = np.array(list(range(2018, 2026)))
    values = np.array([10, 15, 20, 35, 55, 75, 120, 150])
    
    fig, ax = plt.subplots()
    ax.plot(years, values, marker="o", label="Факт")
    
    if show_forecast:
        forecast_years = np.array(list(range(2025, 2031)))
        coef = np.polyfit(years[-4:], values[-4:], 1)
        forecast_values = np.polyval(coef, forecast_years)
        ax.plot(forecast_years, forecast_values, 'r--', label="Прогноз")
    
    ax.set_title("Глобальные инвестиции в AI (млрд $)")
    ax.legend()
    st.pyplot(fig)

elif selected_block == "🌡 Климат и миграция":
    years = np.array(list(range(2010, 2026)))
    values = np.array([5, 7, 8, 10, 12, 15, 18, 20, 25, 28, 30, 33, 34, 34, 35, 36])
    
    fig, ax = plt.subplots()
    ax.plot(years, values, marker="o", label="Факт")
    
    if show_forecast:
        forecast_years = np.array(list(range(2025, 2031)))
        coef = np.polyfit(years[-4:], values[-4:], 1)
        forecast_values = np.polyval(coef, forecast_years)
        ax.plot(forecast_years, forecast_values, 'r--', label="Прогноз")
    
    ax.set_title("Климатические мигранты (млн человек)")
    ax.legend()
    st.pyplot(fig)

elif selected_block == "🏙 Города и урбанизация":
    years = np.array(list(range(2000, 2026)))
    values = np.array([47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85])
    
    fig, ax = plt.subplots()
    ax.plot(years, values, marker="o", color="green", label="Факт")
    
    if show_forecast:
        forecast_years = np.array(list(range(2025, 2031)))
        coef = np.polyfit(years[-4:], values[-4:], 1)
        forecast_values = np.polyval(coef, forecast_years)
        ax.plot(forecast_years, forecast_values, 'r--', label="Прогноз")
    
    ax.set_title("Доля городского населения (%)")
    ax.legend()
    st.pyplot(fig)

# Карта
st.markdown("### 🌍 Карта точек роста")
city_data = pd.DataFrame({
    "Город": ["New York", "London", "Paris", "Singapore", "Dubai", "Shanghai"],
    "Широта": [40.7128, 51.5074, 48.8566, 1.3521, 25.276987, 31.2304],
    "Долгота": [-74.0060, -0.1278, 2.3522, 103.8198, 55.296249, 121.4737],
    "Рост (%)": [2.1, 1.5, 1.3, 3.2, 4.0, 2.8]
})
fig_map = px.scatter_mapbox(
    city_data, lat="Широта", lon="Долгота", hover_name="Город", hover_data=["Рост (%)"],
    color_discrete_sequence=["red"], zoom=1, height=500
)
fig_map.update_layout(mapbox_style="open-street-map")
st.plotly_chart(fig_map, use_container_width=True)
