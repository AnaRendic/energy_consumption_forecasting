import streamlit as st
import pandas as pd
import xgboost as xgb
import datetime

st.set_page_config(
    page_title="Predviđanje potrošnje električne energije", layout="centered")
st.title("Sustav za predviđanje potrošnje")

# Učitavanje modela


@st.cache_resource  # Da se model ne učitava stalno iznova
def load_my_model():
    model = xgb.XGBRegressor()
    model.load_model('model.json')  # Ranije spremljen model
    return model


model = load_my_model()

# Korisnik unosi podatke
st.subheader("Parametri za predviđanje")
odabrani_datum = st.date_input("Odaberi datum", datetime.date.today())
odabrani_sat = st.slider("Odaberi sat", 0, 23, 12)

# Priprema podataka za model


def create_features(datum, sat):
    data = {
        'hour': [sat],
        'dayofweek': [datum.weekday()],
        'quarter': [(datum.month - 1) // 3 + 1],
        'month': [datum.month],
        'year': [datum.year],
        'dayofyear': [datum.timetuple().tm_yday],
        'is_weekend': [1 if datum.weekday() >= 5 else 0]
    }
    return pd.DataFrame(data)


def predict_full_day(datum):
    hours = list(range(24))
    day_data = []

    weekend_val = 1 if datum.weekday() >= 5 else 0

    for hour in hours:
        day_data.append({
            'hour': hour,
            'dayofweek': datum.weekday(),
            'quarter': (datum.month - 1) // 3 + 1,
            'month': datum.month,
            'year': datum.year,
            'dayofyear': datum.timetuple().tm_yday,
            'is_weekend': weekend_val
        })

    df_day = pd.DataFrame(day_data)
    preds = model.predict(df_day)
    return pd.DataFrame({'Sat': hours, 'Potrošnja (MW)': preds})


input_df = create_features(odabrani_datum, odabrani_sat)

# Predviđanje
if st.button('Izračunaj predviđenu potrošnju'):
    prognoza = model.predict(input_df)
    st.metric(label="Predviđena potrošnja (MW)", value=f"{prognoza[0]:.2f} MW")

# Grafički prikaz
st.divider()
# Generiranje podataka za cijeli dan
daily_forecast = predict_full_day(odabrani_datum)
st.line_chart(data=daily_forecast, x='Sat', y='Potrošnja (MW)')
# Opcija za dodatnu tablicu
if st.checkbox("Prikaži tablične podatke"):
    st.dataframe(daily_forecast)
