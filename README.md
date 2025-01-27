# offline-deepseek-ai
An offline AI assistant powered by DeepSeek, designed for secure and efficient local use without internet dependency.
--- 
 

## Overview
The **DeepSeek R1 Offline Chat** is an interactive AI chat interface using the DeepSeek R1 model. It leverages **Streamlit** for the web interface, **LangChain** for conversation management, and **Ollama** to run the DeepSeek R1 model locally. This application provides a seamless offline chat experience with an AI model while maintaining context using conversation memory.

---

## Features
- **Offline AI Interaction**: Runs locally using the DeepSeek R1 model.
- **Streamlit Interface**: A user-friendly and visually appealing web interface.
- **LangChain Integration**: Maintains conversational context with `ConversationBufferMemory`.
- **Lightweight and Efficient**: Fully operational without relying on external servers.

---

## Prerequisites
### 1. Install Ollama
Before running this project, you need to install **Ollama** and set up the DeepSeek R1 model locally.

#### Steps to Install Ollama:
1. Visit the official [Ollama website](https://ollama.ai) to download the installer for your operating system.
2. Follow the installation instructions provided for your platform.

#### Add DeepSeek R1 Model:
Once Ollama is installed, download the **DeepSeek R1** model by running:
```bash
ollama pull deepseek-r1:7b
```

### 2. Install Python and Dependencies
Make sure Python (>= 3.8) is installed on your system. Then, install the required Python dependencies using `pip`.

---

## Installation and Setup
1. Clone this repository:
   ```bash
   git clone https://github.com/your-repository/deepseek-r1-offline-chat.git
   cd deepseek-r1-offline-chat
   ```

2. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Verify that **Ollama** is running:
   ```bash
   ollama serve
   ```

---

## Running the Application
1. Start the Streamlit app:
   ```bash
   streamlit run app.py
   ```

2. Open the app in your browser:
   - The app will automatically launch or provide a local URL (e.g., `http://localhost:8501`).

3. Start interacting with the **DeepSeek R1** model through the chat interface!

---

## How It Works
### Components:
1. **DeepSeek R1 Model**:
   - Powered by **Ollama** to run locally without relying on external APIs.
2. **Streamlit Interface**:
   - Provides an intuitive web UI for chatting with the AI model.
3. **LangChain**:
   - Handles the conversation memory and enables smooth back-and-forth exchanges.

### Workflow:
- The **DeepSeek R1** model is loaded through Ollama.
- **LangChain's ConversationBufferMemory** maintains chat context.
- User inputs are processed, and the AI model's responses are displayed in real-time.

---

## Example Usage
1. Launch the app.
2. Enter any question or topic in the chat input.
3. The AI will respond while maintaining context from the ongoing conversation.

---

## Troubleshooting
- **Ollama Not Running**:
  Ensure that the `ollama serve` command is running in a separate terminal.
- **DeepSeek R1 Model Not Found**:
  Double-check that you've pulled the model using `ollama pull deepseek-r1:7b`.
- **Dependency Issues**:
  Run `pip install -r requirements.txt` again to ensure all dependencies are installed.

---

## License
This project is licensed under the MIT License. Feel free to modify and distribute as per the license terms.

---

Happy chatting! 🎉