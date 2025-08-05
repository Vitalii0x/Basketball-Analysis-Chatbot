import streamlit as st
import time
from basketball_chatbot import BasketballChatbot
from config import Config
import os

# Page configuration
st.set_page_config(
    page_title="🏀 Basketball Analysis Chatbot",
    page_icon="🏀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        font-weight: bold;
        text-align: center;
        color: #1f77b4;
        margin-bottom: 2rem;
    }
    .chat-message {
        padding: 1rem;
        border-radius: 0.5rem;
        margin-bottom: 1rem;
        border-left: 4px solid;
    }
    .user-message {
        background-color: #e3f2fd;
        border-left-color: #2196f3;
    }
    .bot-message {
        background-color: #f3e5f5;
        border-left-color: #9c27b0;
    }
    .sidebar-header {
        font-size: 1.5rem;
        font-weight: bold;
        color: #1f77b4;
        margin-bottom: 1rem;
    }
    .info-box {
        background-color: #e8f5e8;
        padding: 1rem;
        border-radius: 0.5rem;
        border-left: 4px solid #4caf50;
        margin-bottom: 1rem;
    }
</style>
""", unsafe_allow_html=True)

def initialize_chatbot():
    """Initialize the basketball chatbot."""
    try:
        config = Config()
        
        # Check if required environment variables are set
        if not config.PINECONE_API_KEY or not config.PINECONE_ENVIRONMENT:
            st.error("⚠️ Pinecone API key and environment not configured. Please set them in your environment variables.")
            st.info("You can still use the chatbot with basic responses, but vector search will be disabled.")
            return None
        
        chatbot = BasketballChatbot()
        return chatbot
    except Exception as e:
        st.error(f"Error initializing chatbot: {e}")
        return None

def main():
    """Main application function."""
    
    # Header
    st.markdown('<h1 class="main-header">🏀 Basketball Analysis Chatbot</h1>', unsafe_allow_html=True)
    
    # Sidebar
    with st.sidebar:
        st.markdown('<div class="sidebar-header">⚙️ Settings</div>', unsafe_allow_html=True)
        
        # Model selection
        model_option = st.selectbox(
            "Choose Model:",
            ["DialoGPT (Default)", "Custom Model"],
            help="Select the language model to use for responses"
        )
        
        # Knowledge base status
        st.markdown('<div class="sidebar-header">📚 Knowledge Base</div>', unsafe_allow_html=True)
        
        if st.button("🔄 Refresh Knowledge Base"):
            with st.spinner("Refreshing knowledge base..."):
                try:
                    chatbot = initialize_chatbot()
                    if chatbot:
                        chatbot.setup_knowledge_base()
                        st.success("Knowledge base refreshed successfully!")
                    else:
                        st.error("Could not initialize chatbot")
                except Exception as e:
                    st.error(f"Error refreshing knowledge base: {e}")
        
        # Quick actions
        st.markdown('<div class="sidebar-header">🚀 Quick Actions</div>', unsafe_allow_html=True)
        
        if st.button("📋 Basketball Rules"):
            st.session_state.quick_question = "What are the basic rules of basketball?"
        
        if st.button("👥 Player Positions"):
            st.session_state.quick_question = "What are the different player positions in basketball?"
        
        if st.button("📊 Statistics"):
            st.session_state.quick_question = "What are the most important basketball statistics?"
        
        # Information
        st.markdown('<div class="sidebar-header">ℹ️ About</div>', unsafe_allow_html=True)
        st.markdown("""
        This chatbot uses:
        - **LangChain** for conversation management
        - **Hugging Face** models for text generation
        - **Pinecone** for vector search
        - **Streamlit** for the web interface
        """)
    
    # Main chat area
    col1, col2 = st.columns([3, 1])
    
    with col1:
        # Chat container
        chat_container = st.container()
        
        # Initialize session state
        if "messages" not in st.session_state:
            st.session_state.messages = []
        
        if "chatbot" not in st.session_state:
            st.session_state.chatbot = initialize_chatbot()
        
        # Display chat messages
        with chat_container:
            for message in st.session_state.messages:
                if message["role"] == "user":
                    st.markdown(f"""
                    <div class="chat-message user-message">
                        <strong>You:</strong> {message["content"]}
                    </div>
                    """, unsafe_allow_html=True)
                else:
                    st.markdown(f"""
                    <div class="chat-message bot-message">
                        <strong>🏀 Basketball Bot:</strong> {message["content"]}
                    </div>
                    """, unsafe_allow_html=True)
        
        # Chat input
        with st.container():
            # Check for quick question
            if "quick_question" in st.session_state:
                user_input = st.text_input(
                    "Ask me about basketball:",
                    value=st.session_state.quick_question,
                    key="user_input"
                )
                del st.session_state.quick_question
            else:
                user_input = st.text_input(
                    "Ask me about basketball:",
                    placeholder="e.g., What are the rules of basketball?",
                    key="user_input"
                )
            
            col1, col2 = st.columns([4, 1])
            with col1:
                send_button = st.button("Send", type="primary")
            with col2:
                clear_button = st.button("Clear Chat")
            
            if clear_button:
                st.session_state.messages = []
                st.rerun()
            
            if send_button and user_input:
                # Add user message
                st.session_state.messages.append({"role": "user", "content": user_input})
                
                # Generate response
                with st.spinner("🏀 Analyzing your question..."):
                    try:
                        if st.session_state.chatbot:
                            response = st.session_state.chatbot.generate_response(user_input)
                        else:
                            response = "I'm sorry, but I'm currently unable to process your request. Please check your configuration and try again."
                        
                        # Add bot response
                        st.session_state.messages.append({"role": "assistant", "content": response})
                        
                        # Rerun to display new messages
                        st.rerun()
                        
                    except Exception as e:
                        st.error(f"Error generating response: {e}")
    
    with col2:
        # Quick tips and information
        st.markdown('<div class="sidebar-header">💡 Quick Tips</div>', unsafe_allow_html=True)
        
        st.markdown("""
        <div class="info-box">
            <strong>Ask about:</strong>
            <ul>
                <li>Basketball rules</li>
                <li>Player positions</li>
                <li>Game strategies</li>
                <li>Statistics</li>
                <li>Team tactics</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
        # Example questions
        st.markdown('<div class="sidebar-header">❓ Example Questions</div>', unsafe_allow_html=True)
        
        example_questions = [
            "What is a pick and roll?",
            "How do you calculate field goal percentage?",
            "What are the responsibilities of a point guard?",
            "What is zone defense?",
            "How many points is a three-pointer worth?"
        ]
        
        for question in example_questions:
            if st.button(question, key=f"example_{question}"):
                st.session_state.quick_question = question
                st.rerun()

if __name__ == "__main__":
    main() 