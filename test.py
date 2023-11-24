import streamlit as st
import requests

# List of APIs to test
api_endpoints = {
    "Binance API Ping": "https://api.binance.com/api/v3/ping",
    "Binance API Server Time": "https://api.binance.com/api/v3/time",
    "Binance API Exchange Info": "https://api.binance.com/api/v3/exchangeInfo",
    "HTTPBin Get": "https://httpbin.org/get",
    "JSON Placeholder Todos": "https://jsonplaceholder.typicode.com/todos/1"
}

def test_api(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return "Success", response.json()
        else:
            return f"Failed with status code {response.status_code}", None
    except Exception as e:
        return f"Error: {e}", None

def main():
    st.title("API Accessibility Test App")

    for name, url in api_endpoints.items():
        st.subheader(f"Testing: {name}")
        status, data = test_api(url)
        st.text(f"Response: {status}")
        if data:
            st.json(data)

if __name__ == "__main__":
    main()
