# Sustav za predviđanje potrošnje električne energije

# Opis projekta
Ovaj projekt razvijen je kao rješenje za predviđanje satne potrošnje električne energije koristeći strojno učenje. Sustav analizira povijesne podatke, identificira obrasce potrošnje i omogućuje interaktivnu prognozu putem web sučelja.

Tehnologije:
- Python 3.11
- XGBoost (Napredni gradijentni boosting za vremenske serije)
- Pandas i SciKit-learn (Obrada podataka i evaluacija)
- Streamlit (Interaktivni dashboard za vizualizaciju)
- Docker (Kontejnerizacija sustava)

# Rezultati i evaluacija modela
Model je treniran na AEP (American Electric Power) datasetu koji je dostupan na linku https://www.kaggle.com/datasets/robikscube/hourly-energy-consumption/data. Kroz proces feature engineeringa, uključeni su faktori poput doba dana, dana u tjednu, kvartala te poseban indikator za vikende.
- MAPE (Srednja apsolutna pogreška): 8.86%
- Točnost modela: 91.14%
- Glavni utjecajni faktori: Sat u danu (hour) i dan u tjednu (dayofweek) identificirani su kao ključni parametri za preciznu prognozu.

# Kako koristiti projekt?
1. Putem Dockera (Preporučeno)
Docker osigurava da aplikacija radi u izoliranom okruženju sa svim potrebnim zavisnostima. 

-Izgradnja imagea: 
    `docker build -t energy-app .`
-Pokretanje kontejnera: 
    `docker run -p 8501:8501 energy-app`

Nakon pokretanja, aplikacija je dostupna na: http://localhost:8501

2. Lokalno pokretanje (Virtualno okruženje)
- Instalacija biblioteka: 
    `pip install -r requirements.txt`
- Pokretanje Streamlit aplikacije: 
    `streamlit run main.py`

# Struktura direktorija 
- main.py - Glavna Streamlit aplikacija.
- model.json - Istrenirani XGBoost model spreman za predviđanje.
- Dockerfile - Konfiguracija za kontejnerizaciju. 
- requirements.txt - Popis svih potrebnih Python biblioteka.
- analiza.ipynb - Jupyter bilježnica s detaljnim procesom analize i treninga.