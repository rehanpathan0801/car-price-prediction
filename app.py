import pandas as pd
import pickle as pk
import streamlit as st

# Load model with graceful error reporting
model = None
model_load_error = None
try:
    with open('model.pkl', 'rb') as f:
        model = pk.load(f)
except Exception as e:
    model_load_error = str(e)
    # In Streamlit, show a warning but allow the app to load so user sees the UI
    st.warning("Model file 'model.pkl' not found or failed to load. Prediction will be disabled.")

st.header('Car Price Prediction ML Model')

# Load dataset safely
try:
    cars_data = pd.read_csv('Cardetails.csv')
except Exception as e:
    st.error("Could not read 'Cardetails.csv'. Please ensure the file exists in the app folder.")
    st.stop()

def get_brand_name(car_name):
    if not isinstance(car_name, str):
        return car_name
    car_name = car_name.split(' ')[0]
    return car_name.strip()

cars_data['name'] = cars_data['name'].apply(get_brand_name)

name = st.selectbox('Select Car Brand', cars_data['name'].unique())
year = st.slider('Car Manufactured Year', 1994, 2024)
km_driven = st.slider('No of kms Driven', 11, 200000)
fuel = st.selectbox('Fuel type', cars_data['fuel'].unique())
seller_type = st.selectbox('Seller type', cars_data['seller_type'].unique())
transmission = st.selectbox('Transmission type', cars_data['transmission'].unique())
# Fixed label: owner should be 'Owner' (previously duplicated 'Seller  type')
owner = st.selectbox('Owner', cars_data['owner'].unique())
mileage = st.slider('Car Mileage', 10, 40)
engine = st.slider('Engine CC', 700, 5000)
max_power = st.slider('Max Power', 0, 200)
seats = st.slider('No of Seats', 5, 10)


if st.button("Predict"):
    if model is None:
        st.error("Model not loaded. Prediction unavailable until 'model.pkl' is present and valid.")
    else:
        input_data_model = pd.DataFrame(
            [[name, year, km_driven, fuel, seller_type, transmission, owner, mileage, engine, max_power, seats]],
            columns=['name', 'year', 'km_driven', 'fuel', 'seller_type', 'transmission', 'owner', 'mileage', 'engine', 'max_power', 'seats'])

        # Use mapping dicts to replace known categorical values to numeric codes
        owner_map = {
            'First Owner': 1,
            'Second Owner': 2,
            'Third Owner': 3,
            'Fourth & Above Owner': 4,
            'Test Drive Car': 5
        }
        fuel_map = {'Diesel': 1, 'Petrol': 2, 'LPG': 3, 'CNG': 4}
        seller_map = {'Individual': 1, 'Dealer': 2, 'Trustmark Dealer': 3}
        trans_map = {'Manual': 1, 'Automatic': 2}
        name_map = {
            'Maruti': 1, 'Skoda': 2, 'Honda': 3, 'Hyundai': 4, 'Toyota': 5, 'Ford': 6, 'Renault': 7,
            'Mahindra': 8, 'Tata': 9, 'Chevrolet': 10, 'Datsun': 11, 'Jeep': 12, 'Mercedes-Benz': 13,
            'Mitsubishi': 14, 'Audi': 15, 'Volkswagen': 16, 'BMW': 17, 'Nissan': 18, 'Lexus': 19,
            'Jaguar': 20, 'Land': 21, 'MG': 22, 'Volvo': 23, 'Daewoo': 24, 'Kia': 25, 'Fiat': 26, 'Force': 27,
            'Ambassador': 28, 'Ashok': 29, 'Isuzu': 30, 'Opel': 31
        }

        input_data_model['owner'].replace(owner_map, inplace=True)
        input_data_model['fuel'].replace(fuel_map, inplace=True)
        input_data_model['seller_type'].replace(seller_map, inplace=True)
        input_data_model['transmission'].replace(trans_map, inplace=True)
        input_data_model['name'].replace(name_map, inplace=True)

        # Coerce expected numeric columns to numeric types (safe fallback to 0 for unexpected values)
        numeric_cols = ['year', 'km_driven', 'mileage', 'engine', 'max_power', 'seats', 'owner', 'fuel', 'seller_type', 'transmission', 'name']
        for col in numeric_cols:
            input_data_model[col] = pd.to_numeric(input_data_model[col], errors='coerce').fillna(0)

        # Predict and display
        car_price = model.predict(input_data_model)
        predicted_price = int(round(car_price[0]))
        predicted_price = max(predicted_price, 0)
        st.markdown('Car Price is going to be : ₹' + f"{predicted_price:,}")