import streamlit as st
import requests

# Title and Intro
st.title("🔮 The Future of Cryptocurrency")
st.write("Welcome to an interactive journey into the future of digital currencies.")
st.image(
    "https://upload.wikimedia.org/wikipedia/commons/thumb/0/09/Cryptocurrency_logos.png/640px-Cryptocurrency_logos.png",
    caption="Popular Cryptocurrency Logos",
    use_container_width=True
)
# Sidebar
st.sidebar.title("🧭 Navigation")
st.sidebar.info("Use the dropdown on the main page to explore different topics.")
st.sidebar.markdown("---")
st.sidebar.success("Built with ❤️ using Streamlit")



# Dropdown Menu (Selectbox)
st.subheader("📈 What do you want to explore?")
option = st.selectbox("Choose a topic:", [
    "Overview",
    "Trends",
    "Predictions",
    "Risks",
    "Opportunities"
])

# Show content based on selection
if option == "Overview":
    st.write("Cryptocurrency is a digital or virtual currency that uses cryptography for security. It operates independently of a central bank.")
elif option == "Trends":
    st.write("Current trends include DeFi, NFTs, CBDCs, Bitcoin ETFs, and increasing government interest.")

    st.subheader("📊 Market Cap Prediction (Sample Data)")
    
    import pandas as pd

    data = pd.DataFrame({
        'Year': [2021, 2022, 2023, 2024, 2025],
        'Market Cap (in Billion $)': [800, 1500, 1100, 1800, 2500]
    })

    st.line_chart(data.set_index('Year'))
elif option == "Predictions":
    st.write("Experts predict that cryptocurrencies will see mass adoption, new regulations, and more stablecoin usage by 2030.")
elif option == "Risks":
    st.write("Risks include market volatility, lack of regulation, security issues, and environmental concerns.")
elif option == "Opportunities":
    st.write("Cryptocurrencies offer opportunities for financial inclusion, fast cross-border payments, and Web3 innovation.")
# 💬 User Opinion Section

st.subheader("🤔 What do *you* think?")
user_opinion = st.text_input("Where do you see cryptocurrency in 5 years?")

if user_opinion:
    st.success(f"📢 Your prediction: {user_opinion}")



st.subheader("📡 Live Bitcoin Price")

if st.button("Check Current Price"):
    try:
        url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"
        response = requests.get(url)
        data = response.json()
        price = data["bitcoin"]["usd"]
        st.success(f"💰 Current Bitcoin Price: ${price}")
    except Exception as e:
        st.error("⚠️ Could not fetch data. Please check your internet connection.")





