import streamlit as st
import numpy as np

def monte_carlo_simulacja(srednia_spotkan, odchylenie_std, wiek_start, srednia_zycia, zdrowie, uzywki, liczba_symulacji):
    modyfikator_zdrowia = 1.0 + (0.1 if zdrowie == 'dobry' else -0.1 if zdrowie == 'zły' else 0)
    modyfikator_uzywki = 1.0 - (0.1 if uzywki else 0)
    modyfikowana_srednia_zycia = srednia_zycia * modyfikator_zdrowia * modyfikator_uzywki

    wyniki = []
    for _ in range(liczba_symulacji):
        max_lata = np.random.normal(modyfikowana_srednia_zycia, 5)
        lata_spotkan = max(0, int(max_lata - wiek_start))
        spotkania_rocznie = np.random.normal(srednia_spotkan, odchylenie_std, lata_spotkan)
        totalne_spotkania = np.sum(spotkania_rocznie)
        wyniki.append(totalne_spotkania)
    return wyniki

# Ustawienie Streamlit
st.set_page_config(page_title='Symulacja Spotkań Rodzinnych', layout='wide')
st.title('Symulacja przyszłych spotkań z rodzicami')

role = st.radio("Wybierz swoją rolę:", ('Dziecko', 'Rodzic'))

if role == 'Dziecko':
    st.sidebar.header('Parametry symulacji dla Dziecka')
    wiek_start = st.sidebar.slider('Wiek twojego rodzica:', min_value=18, max_value=100, value=50)
elif role == 'Rodzic':
    st.sidebar.header('Parametry symulacji dla Rodzica')
    wiek_start = st.sidebar.slider('Twój wiek:', min_value=18, max_value=100, value=50)

srednia_spotkan = st.sidebar.slider('Średnia liczba spotkań na rok:', min_value=1, max_value=52, value=10)
odchylenie_std = st.sidebar.slider('Odchylenie standardowe spotkań:', min_value=0, max_value=10, value=2)
srednia_zycia = st.sidebar.slider('Średnia długość życia:', min_value=60, max_value=100, value=74)
zdrowie = st.sidebar.selectbox('Stan zdrowia:', ['dobry', 'neutralny', 'zły'])
uzywki = st.sidebar.checkbox('Czy regularnie stosowane są używki?')
liczba_symulacji = st.sidebar.slider('Liczba symulacji:', min_value=1000, max_value=10000, value=5000)

if st.button('Uruchom symulację'):
    wyniki = monte_carlo_simulacja(srednia_spotkan, odchylenie_std, wiek_start, srednia_zycia, zdrowie, uzywki, liczba_symulacji)
    st.subheader('Wyniki symulacji')
    st.write(f'Średnia liczba przewidywanych spotkań: {np.mean(wyniki):.2f}')
    st.write(f'Mediana liczby przewidywanych spotkań: {np.median(wyniki):.2f}')
    st.write('Detalizacja wszystkich symulowanych wyników:')
    st.dataframe(wyniki)
