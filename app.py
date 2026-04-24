import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score

# =========================
# CONFIG
# =========================
st.set_page_config(page_title="Logistics ML Analysis", layout="centered")

st.title("📦 Logistics ML Analysis")
st.write("Predict Packing → Ready Supply Time and analyze bottleneck")

data = {
    'process_1': [1.5, 2.0, 1.2, 3.0, 2.5, 1.8, 2.2, 3.5, 1.0, 2.8],
    'process_2': [1.0, 1.5, 0.8, 2.0, 1.8, 1.2, 1.4, 2.5, 0.7, 2.0],
    'process_3': [2.0, 3.0, 1.5, 4.0, 3.5, 2.5, 2.8, 4.5, 1.2, 3.8],
}

df = pd.DataFrame(data)

X = df[['process_1', 'process_2']]
y = df['process_3']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = LinearRegression()
model.fit(X_train, y_train)

# evaluasi
y_pred = model.predict(X_test)
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

# Model
st.subheader("📊 Model Evaluation")
col1, col2 = st.columns(2)
col1.metric("MAE", f"{mae:.2f}")
col2.metric("R² Score", f"{r2:.2f}")

st.markdown("---")

st.subheader("🧾 Input Process Time")

p1 = st.number_input("Order → Warehouse (minutes)", value=15.0)
p2 = st.number_input("Warehouse → Packing (minutes)", value=16.0)

# Prediction
if st.button("Run Prediction"):

    input_data = pd.DataFrame({
        'process_1': [p1],
        'process_2': [p2]
    })

    predicted_p3 = model.predict(input_data)[0]
    total = p1 + p2 + predicted_p3

    # Output
    st.subheader("📈 Prediction Result")

    st.success(f"Estimated Packing → Ready: {predicted_p3:.2f} minutes")
    st.info(f"Estimated Total Lead Time: {total:.2f} minutes")

    # Bottleneck
    processes = {
        "Order → Warehouse": p1,
        "Warehouse → Packing": p2,
        "Packing → Ready": predicted_p3
    }

    bottleneck = max(processes, key=processes.get)

    st.warning(f"🚨 Bottleneck: {bottleneck}")

    # Insight
    st.subheader("🧠 AI Insight")
    st.write(f"""
    The system identifies **{bottleneck}** as the most dominant stage in the workflow.  
    Reducing delay in this stage could significantly improve overall lead time.
    """)

    #Recomend
    st.subheader("🚀 AI Recommendation")

    if bottleneck == "Order → Warehouse":
        st.write("""
        Improve coordination and speed up item retrieval from warehouse systems.
        """)

    elif bottleneck == "Warehouse → Packing":
        st.write("""
        Optimize warehouse flow and improve material handling efficiency.
        """)

    else:
        st.write("""
        Increase manpower or improve packing efficiency to reduce processing time.
        """)