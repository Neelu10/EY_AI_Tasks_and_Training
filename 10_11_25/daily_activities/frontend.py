import streamlit as st
import requests

st.set_page_config(page_title="Smart Query Assistant", layout="centered")
st.title("🤖 Smart Query Assistant")

query = st.text_input("Enter your query (e.g., 'Add 45 and 35', 'Reverse Name', 'Tell me today's date')")

if st.button("Submit"):
    if not query.strip():
        st.warning("Please enter a query first.")
    else:
        try:
            res = requests.post("http://127.0.0.1:8000/ask", json={"query": query})
            if res.status_code == 200:
                data = res.json()
                st.success(f"✅ **Answer:** {data['answer']}")
            else:
                st.error(f"❌ Error: {res.text}")
        except Exception as e:
            st.error(f"🚨 Unable to reach backend: {e}")
