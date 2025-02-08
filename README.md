# 🚀 AI-Based Phishing URL Classifier

This project is an **AI-driven phishing URL classifier** that analyzes URLs and their website content to determine if they are **legitimate or phishing sites**. It leverages **OpenAI's GPT-4** to analyze webpage content and **Streamlit** for an interactive user interface.

---

## 📌 Features

✅ **URL Analysis:** Extracts and analyzes URL features such as HTTPS usage, domain structure, and suspicious keywords.

✅ **Content Scraping:** Fetches website text and analyzes it for phishing indicators.

✅ **AI-Powered Classification:** Uses GPT-4 to evaluate URL legitimacy based on content and structure.

✅ **Streamlit UI:** Provides an interactive web-based interface for easy URL testing.

✅ **Real-Time Insights:** Displays extracted features and AI-generated insights in real-time.

---

## 🛠️ Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/GargiChakraborty105/AI-based-phishing-URL-classifier.git
```

### 2️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 3️⃣ Set Up OpenAI API Key
Create a `.env` file and add your OpenAI API key:
```bash
echo "OPENAI_API_KEY=your-openai-api-key" > .env
```

Or set it as an environment variable:
```bash
export OPENAI_API_KEY='your-openai-api-key'
```

### 4️⃣ Run the Application
```bash
streamlit run main.py
```

---

## 🖥️ Usage
1. **Enter a URL** in the input field.
2. Click on **"Analyze URL"**.
3. The app will:
   - Extract URL features
   - Fetch website content
   - Analyze it using GPT-4
   - Display the results as **Legitimate, Phishing, or Uncertain**

---

## 🔍 How It Works

### 🔹 Step 1: Extract URL Features
- Checks for special characters, long domain names, and suspicious keywords.
- Identifies whether the site uses **HTTPS**.

### 🔹 Step 2: Scrape Website Content
- Fetches the **HTML content** from the given URL.
- Extracts readable text using **BeautifulSoup**.

### 🔹 Step 3: AI-Based Classification
- Sends extracted content and URL features to **GPT-4**.
- GPT-4 analyzes phishing indicators (urgent messages, credential requests, poor grammar, etc.).
- Returns a final classification as **"Legitimate"**, **"Phishing"**, or **"Uncertain"**.

### 🔹 Step 4: Display Results
- If GPT-4 detects **phishing**, the app shows **🚨 Phishing Alert**.
- If the site is **safe**, it shows **✅ Legitimate Site**.
- If unsure, it warns **⚠️ Proceed with Caution**.

---

## 📜 Example Results
| **Website**                 | **Expected Classification** |
|-----------------------------|-----------------------------|
| `https://www.google.com`   | ✅ Legitimate |
| `http://paypal-verification.com` | 🚨 Phishing |
| `https://secure-banking-login.com` | ⚠️ Uncertain |
| `http://fake-amazon-payment.com` | 🚨 Phishing |
| `https://microsoft.com`  | ✅ Legitimate |

---

## 🛠️ Technologies Used
- **Python 3.x**
- **Streamlit** (for UI)
- **OpenAI GPT-4 API** (for text-based analysis)
- **BeautifulSoup** (for web scraping)
- **Requests** (to fetch website content)
- **dotenv** (to manage environment variables)

---

## ⚠️ Disclaimer
This tool provides **AI-based phishing detection** but is **not 100% foolproof**. Always verify the legitimacy of websites manually before entering sensitive information.

---

## 🤝 Contributing
Feel free to submit **issues** or **pull requests** to improve the project. 🚀

---

## 📜 License
This project is licensed under the **MIT License**.


