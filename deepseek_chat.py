"""
DeepSeek R1 Offline Chat 
This script creates an interactive chat interface using the DeepSeek R1 language model,
running locally through Ollama. It demonstrates the use of Streamlit for creating
web applications and LangChain for managing conversations with AI models.
"""

import streamlit as st
from langchain.llms import Ollama
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory

# Streamlit page configuration
st.set_page_config(page_title="Offline DeepSeek R1", page_icon="🤖", layout="wide")

def initialize_model():
    """Initialize and return the Ollama model."""
    return Ollama(model="deepseek-r1:7b")

def create_conversation_chain(model, memory):
    """Create and return a ConversationChain object."""
    return ConversationChain(
        llm=model,
        memory=memory,
        verbose=True
    )

def display_chat_history(messages):
    """Display the chat history."""
    for message in messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

def main():
    st.title("DeepSeek R1 Offline Chat...")

    # Sidebar with educational information
    st.sidebar.title("About This App")
    st.sidebar.info(
        "This app demonstrates how to create an AI chat interface using:\n"
        "- Streamlit for the web interface\n"
        "- LangChain for managing the conversation\n"
        "- Ollama for running the DeepSeek R1 model locally"
    )
    st.sidebar.title("How It Works")
    st.sidebar.info(
        "1. The app initializes the DeepSeek R1 model via Ollama.\n"
        "2. It uses ConversationBufferMemory to maintain context.\n"
        "3. User input is processed through a ConversationChain.\n"
        "4. The model's response is displayed in the chat interface."
    )

    # Initialize model
    model = initialize_model()

    # Initialize or retrieve conversation memory
    if "memory" not in st.session_state:
        st.session_state.memory = ConversationBufferMemory()

    # Create conversation chain
    chain = create_conversation_chain(model, st.session_state.memory)

    # Initialize or retrieve chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display chat history
    display_chat_history(st.session_state.messages)

    # Chat input
    if prompt := st.chat_input("What would you like to know?"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            response = chain.run(prompt)
            st.markdown(response)
        st.session_state.messages.append({"role": "assistant", "content": response})

    # Display current conversation memory
    st.sidebar.title("Current Conversation Memory")
    st.sidebar.code(st.session_state.memory.buffer)

if __name__ == "__main__":
    main()
