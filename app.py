import streamlit as st
from src.predict import predict_spam

st.set_page_config(
    page_title="Spam Detector",
    page_icon="🚫",
    layout="centered"
)

# Title Section
st.title("📩 SMS Spam Detection App")
st.markdown("Type a message below to check if it's **Spam** or **Not Spam**.")

# Input box
user_input = st.text_area("✉️ Enter your message here:")

# Button to trigger prediction
if st.button("🔍 Predict"):
    if user_input.strip() == "":
        st.warning("⚠️ Please enter a message to analyze.")
    else:
        # Call your prediction function (returns label + probability)
        result, probability = predict_spam(user_input)

        # Show results
        if result == "Spam":
            st.error("🚨 This message is **SPAM**.")
        else:
            st.success("✅ This message is **NOT SPAM**.")

        # Show confidence
        st.info(f"🔢 Prediction Confidence: `{probability * 100:.2f}%`")

# Footer
st.markdown("---")
st.caption("📊 Model Accuracy: 96.14% | Built by Sandhya")
