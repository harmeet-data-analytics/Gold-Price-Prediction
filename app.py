import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Streamlit page configuration
st.set_page_config(page_title="Gold Price Predictor", layout="wide")
st.title("🪙 Gold Price Predictor (CSV Dataset)")

# Load and preprocess data
@st.cache_data
def load_data():
    df = pd.read_csv(
        r"C:\Users\jagta\OneDrive\Desktop\gold_price_prediction\gold_price_predictor\FINAL_USO.csv",
        parse_dates=["Date"]
    )
    df.columns = df.columns.str.strip()  # Remove any extra whitespace
    df = df.sort_values("Date")
    df.set_index("Date", inplace=True)
    return df

df = load_data()

# Show actual columns for debugging
st.subheader("📁 Raw Data Info")
st.write("Columns found in dataset:", df.columns.tolist())
st.write(df.head())

# Handle alternative column names (you can adjust more if needed)
possible_price_columns = ["Price", "price", "Close", "Adj Close", "Gold Price"]
found_price_col = None
for col in df.columns:
    if col.strip() in possible_price_columns:
        found_price_col = col
        break

if found_price_col:
    df.rename(columns={found_price_col: "Price"}, inplace=True)
else:
    st.error("❌ Could not find a valid 'Price' column in your dataset.")
    st.stop()

# Check if dataframe is still usable
if df.empty or 'Price' not in df.columns:
    st.error("❌ The dataset is empty or missing a 'Price' column.")
    st.stop()

# Display last 10 rows
st.subheader("📊 Gold Price Data (Last 10 Rows)")
st.dataframe(df.tail(10))

# Feature engineering
df['Target'] = df['Price'].shift(-1)
df.dropna(inplace=True)

# Define features and labels
X = df[['Price']]
y = df['Target']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, shuffle=False, test_size=0.2)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Predictions and evaluation
predictions = model.predict(X_test)
mse = mean_squared_error(y_test, predictions)

# Display evaluation
st.subheader("📉 Model Evaluation")
st.write(f"**Mean Squared Error (MSE):** {mse:.2f}")

# Plot actual vs predicted
fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(y_test.index, y_test.values, label="Actual Price", color='blue')
ax.plot(y_test.index, predictions, label="Predicted Price", linestyle="--", color='orange')
ax.set_title("Actual vs Predicted Gold Prices")
ax.set_xlabel("Date")
ax.set_ylabel("Price (USD)")
ax.legend()
st.pyplot(fig)

# Predict next day's price
latest_price = df['Price'].iloc[-1]
predicted_next = model.predict(np.array([[latest_price]]))[0]

st.subheader("🔮 Next Day Prediction")
st.write(f"Last known price: **${latest_price:.2f}**")
st.write(f"Predicted next price: **${predicted_next:.2f}**")
