import pandas as pd
import random
import streamlit as st

# Load fortunes
fortunes = pd.read_csv("Fortune_cookies.csv")

# Add layout and title
st.set_page_config(page_title="Fortune Cookie & Lucky Number Generator",
                     page_icon="🍪",
                     layout="wide")

st.title("🍪 Fortune Cookie & Lucky Number Generator")
st.subheader("Open your fortune cookie and find out your lucky number!")

# Generate a random fortune
if st.button("Open your fortune cookie"):
    with st.spinner("Opening..."):

        fortune = random.choice(fortunes['Fortune'])

        lucky_number = random.randint(1, 100)

        st.balloons()
        st.text("🎉 Congratulations! 🎉")
        st.text("Your fortune cookie has been opened!")
        st.success(f"## ✨ {fortune} ✨")
        st.text("Your lucky number is:")
        st.info(f"## 🍀 {lucky_number} 🍀")
