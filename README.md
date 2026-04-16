# 🤖 Gemini Pro Chatbot with Streamlit

A conversational AI chatbot built using Python, Streamlit, and Google Gemini Pro API. This application provides a clean, responsive user interface for interacting with the Gemini model, maintaining a full conversation history for context aware responses.

<h3 align="center"><a href="https://bdyksrxhmbrwkhwfenfthd.streamlit.app/"><strong>Live Demo on Streamlit Cloud</strong></a></h3>

## 📖 About The Project

This project is a simple yet robust implementation of a Large Language Model (LLM) chatbot. The goal was to create a functional and easy-to-understand chatbot application that developers can easily clone, modify, and learn from.

**Key Features:**

- **Conversational Memory:** The chatbot remembers previous messages in the session to provide contextually relevant answers.
- **Clean User Interface:** Built with Streamlit for a simple and intuitive chat experience.
- **Easy Setup:** Requires minimal setup with a `.env` file for your API key.
- **Model Checker:** Includes a utility script (`check_models.py`) to help you find the correct Gemini model name available for your specific API key, preventing common `404 Not Found` errors.

## 🛠️ Tech Stack

This project is built with the following technologies:

- **Python**
- **Streamlit:** For creating the interactive web UI.
- **Google Generative AI API:** For accessing the Gemini family of models.
- **python-dotenv:** For managing environment variables securely.

## 📂 Project Structure

Here is a brief overview of the project's file structure:

```
gemini-chatbot/
├── .env                  # Stores your secret API key
├── .gitignore            # Specifies files for Git to ignore (like venv)
├── check_models.py       # Utility to list available models for your API key
├── main.py               # The main Streamlit application script
└── requirements.txt      # Lists all the Python dependencies
```

## 🚀 Getting Started

Follow these steps to set up and run the project on your local machine.

### Prerequisites

- Python 3.8 or higher installed on your system.
- A Google Account to create a Gemini API key.

### Installation & Setup

1. **Clone the Repository**
   ```
   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name
   ```

2. **Create a Virtual Environment**
   
   It's a best practice to create a virtual environment to manage project dependencies.
   
   _# For Windows_
   ```
   python -m venv venv
   venv\Scripts\activate
   ```
   
   _# For macOS/Linux_
   ```
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install Dependencies**
   
   Install all the required packages from the `requirements.txt` file.
   ```
   pip install -r requirements.txt
   ```

4. **Get Your Google Gemini API Key**
   
   - Go to [Google AI Studio](https://aistudio.google.com/).
   - Sign in with your Google account.
   - Click on **"Get API key"** > **"Create API key in new project"**.
   - Copy the generated API key.

5. **Set Up Your Environment File**
   
   - Create a new file in the root of your project named `.env`.
   - Add your API key to this file as shown below:
   
   ```
   # .env file
   GOOGLE_API_KEY="PASTE_YOUR_API_KEY_HERE"
   ```

6. **(Optional but Recommended) Check Your Available Models**
   
   Google API keys can have access to different model names (e.g., `gemini-pro` vs. `gemini-pro-latest`). To avoid errors, run the included script to see which models your key can use.
   ```
   python check_models.py
   ```
   
   - The script will print a list of model names. Find the one you want to use (e.g., `gemini-pro-latest`) and make sure it's the one specified in `main.py`.

7. **Run the Streamlit App**
   
   You're all set! Run the following command in your terminal.
   ```
   streamlit run main.py
   ```
   
   - Your chatbot will now be running and accessible in your web browser.

## 🔗 Connect with Me

Feel free to reach out if you have any questions or just want to connect!

- **LinkedIn:** [https://www.linkedin.com/in/shhshubham/](https://www.linkedin.com/in/shhshubham/)
