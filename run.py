import streamlit as st
import numpy as np

def monte_carlo_simulacja(wiek_start, srednia_spotkan, srednia_zycia, zdrowie, uzywki, styl_zycia, liczba_symulacji):
    zdrowie_modyfikator = {'dobry': 1.1, 'średni': 1.0, 'zły': 0.9}
    uzywki_modyfikator = {'tak': 0.9, 'nie': 1.0}
    styl_zycia_modyfikator = {'aktywny': 1.05, 'umiarkowany': 1.0, 'siedzący': 0.95}

    modyfikowana_srednia_zycia = srednia_zycia * zdrowie_modyfikator[zdrowie] * uzywki_modyfikator[uzywki] * styl_zycia_modyfikator[styl_zycia]
    wyniki = []
    for _ in range(liczba_symulacji):
        lata_spotkan = max(0, int(modyfikowana_srednia_zycia - wiek_start))
        totalne_spotkania = srednia_spotkan * lata_spotkan
        wyniki.append(totalne_spotkania)
    return wyniki

# Ustawienie Streamlit
st.set_page_config(page_title='Symulacja Spotkań Rodzinnych', layout='wide')
st.title('Symulacja przyszłych spotkań z rodzicami')
st.image('path_to_image.jpg', caption='Rodzinne chwile')  # Zmień 'path_to_image.jpg' na ścieżkę do Twojego obrazu

st.header("Czy wiesz, że liczba spotkań z Twoimi rodzicami jest policzalna?")
st.write("""
Zastanawiałeś się kiedyś, ile razy jeszcze będziesz mógł spotkać się ze swoimi rodzicami? Nasza symulacja pomoże Ci oszacować tę liczbę na podstawie kilku kluczowych czynników.
Przejdźmy do szczegółów i zobaczmy, jak możesz wykorzystać te informacje do lepszego planowania czasu z rodziną!
""")

rodzic = st.selectbox('Wybierz rodzica:', ['Mama', 'Tata'])
wiek_start = st.slider('Wiek rodzica:', 18, 100, 50)
srednia_spotkan = st.slider('Średnia liczba spotkań na rok:', 1, 52, 10)
srednia_zycia = 81 if rodzic == 'Mama' else 74
zdrowie = st.selectbox('Stan zdrowia:', ['dobry', 'średni', 'zły'])
uzywki = st.selectbox('Stosowanie używek:', ['nie', 'tak'])
styl_zycia = st.selectbox('Styl życia:', ['aktywny', 'umiarkowany', 'siedzący'])
liczba_symulacji = st.slider('Liczba symulacji:', 1000, 10000, 5000)

if st.button('Uruchom symulację'):
    wyniki = monte_carlo_simulacja(wiek_start, srednia_spotkan, srednia_zycia, zdrowie, uzywki, styl_zycia, liczba_symulacji)
    st.subheader('Wyniki symulacji')
    srednia_spotkan = np.mean(wyniki)
    mediana_spotkan = np.median(wyniki)
    st.write(f'Średnia liczba przewidywanych spotkań: {srednia_spotkan:.2f}')
    st.write(f'Mediana liczby przewidywanych spotkań: {mediana_spotkan:.2f}')

    # Podsumowanie i rekomendacje
    if srednia_spotkan < 20:
        st.subheader("Do przemyślenia:")
        st.write("🌱 Liczba przewidywanych spotkań wydaje się być dość niska. Może warto zastanowić się nad sposobami na częstsze spotkania?")
    elif srednia_spotkan < 100:
        st.subheader("Do przemyślenia:")
        st.write("💞 Umiarkowana liczba spotkań to wspaniała okazja, aby pielęgnować relacje.")
    else:
        st.subheader("Do przemyślenia:")
        st.write("🎉 Wygląda na to, że liczba przewidywanych spotkań jest wysoka, co jest fantastyczne!")

    st.write('Detalizacja wszystkich symulowanych wyników:')
    st.dataframe(wyniki)

    st.subheader("Pamiętaj, że to tylko symulacja")
    st.write("""
    Wyniki prezentowane powyżej są wynikiem symulacji metodą Monte Carlo, która polega na wielokrotnym losowaniu próbek z określonych rozkładów prawdopodobieństwa, aby oszacować niepewne wyniki. Każda symulacja jest uproszczeniem i nie może dokładnie przewidzieć przyszłości, dlatego ważne jest, aby traktować te wyniki jako orientacyjne i używać ich do inspiracji do tworzenia wartościowych relacji rodzinnych.
    """)
