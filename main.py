import streamlit as st
import requests
import tldextract
import openai
from bs4 import BeautifulSoup
from urllib.parse import urlparse

# OpenAI API Key (Replace with your actual key)
OPENAI_API_KEY = "api-key"

# Function to extract URL-based features
def extract_url_features(url):
    parsed_url = urlparse(url)
    domain = parsed_url.netloc
    path = parsed_url.path

    # Feature 1: URL Length
    url_length = len(url)

    # Feature 2: Special Characters Count
    special_chars_count = sum(1 for char in url if char in ['@', '?', '-', '=', '.', '_', '&', '~', '%', '/'])

    # Feature 3: Count of dots in the domain
    dot_count = domain.count(".")

    # Feature 4: Check HTTPS usage
    https_flag = 1 if parsed_url.scheme == "https" else 0

    return {
        "URL Length": url_length,
        "Special Characters Count": special_chars_count,
        "Dot Count in Domain": dot_count,
        "Uses HTTPS": "Yes" if https_flag else "No"
    }

# Function to scrape website content
def extract_website_content(url):
    try:
        response = requests.get(url, timeout=5)
        soup = BeautifulSoup(response.text, "html.parser")
        text = " ".join([p.get_text() for p in soup.find_all("p")])[:5000]  # Limit text size for GPT
        return text if text else "No readable content found."
    except:
        return "Error fetching content"

# Function to analyze URL and content with GPT-4
def analyze_with_gpt(url, content):
    openai.api_key = OPENAI_API_KEY

    prompt = f"""
      You are a cybersecurity expert analyzing whether a given website is legitimate or a phishing attempt. 
    Consider the following aspects:
    1. URL Structure:
       - Look for excessive special characters, long URLs, and multiple dots in the domain.
       - Check if it contains misleading words (e.g., "secure", "login", "verify") but doesn't belong to an official organization.
       - If HTTPS is missing, note it.
    2. Website Content:
       - Does it contain urgent requests (e.g., "Your account will be locked", "Verify now")?
       - Does it ask for personal details (passwords, banking info) directly?
       - Check for spelling or grammatical errors.
    3. Determine if the website is legitimate or phishing based on your analysis.

    URL: {url}

    Website Content:
    {content[:3000]}  # Limit to avoid exceeding token limits

    Provide a conclusion in the format:
    - "Legitimate" if there are no signs of phishing.
    - "Phishing" if the indicators suggest a phishing attempt.
    - "Uncertain" if more verification is needed.
    Explain your reasoning briefly.
    """

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}]
        )
        gpt_response = response["choices"][0]["message"]["content"]
        return gpt_response
    except Exception as e:
        return f"Error in OpenAI API: {str(e)}"

# Streamlit UI
def main():
    st.title("🔍 AI-Based Phishing URL Classifier")
    url = st.text_input("Enter a URL to analyze:")

    if st.button("Analyze URL"):
        if url:
            # Extract URL features
            st.subheader("🔍 Extracting URL Features...")
            features = extract_url_features(url)
            for key, value in features.items():
                st.write(f"**{key}:** {value}")

            # Scrape website content
            st.subheader("🌐 Extracting Website Content...")
            content = extract_website_content(url)
            if content == "Error fetching content":
                st.error("Failed to extract website content.")
                return
            else:
                st.success("Website content extracted successfully.")

            # AI Analysis
            st.subheader("🤖 AI Analysis with GPT-4...")
            gpt_result = analyze_with_gpt(url, content)
            st.write(gpt_result)

            # Determine final classification
            if "phishing" in gpt_result.lower():
                st.error("🚨 This website is classified as **Phishing**.")
            elif "legitimate" in gpt_result.lower():
                st.success("✅ This website is classified as **Legitimate**.")
            else:
                st.warning("⚠️ Unable to confidently classify the website. Proceed with caution.")

if __name__ == "__main__":
    main()
