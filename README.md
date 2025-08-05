# 🏀 Basketball Analysis Chatbot

A sophisticated basketball analysis chatbot built with **LangChain**, **Hugging Face Llama models**, and **Pinecone** vector database. This application provides intelligent responses to basketball-related questions using advanced AI and vector search capabilities.

## ✨ Features

- **🤖 AI-Powered Responses**: Uses Hugging Face language models for natural conversation
- **🔍 Vector Search**: Pinecone integration for semantic search of basketball knowledge
- **📚 Comprehensive Knowledge Base**: Built-in basketball rules, positions, strategies, and statistics
- **🌐 Modern Web Interface**: Beautiful Streamlit-based UI with real-time chat
- **⚡ Quick Actions**: Pre-built buttons for common basketball questions
- **🔄 Real-time Updates**: Dynamic knowledge base refresh capabilities

## 🛠️ Technology Stack

- **LangChain**: Conversation management and AI orchestration
- **Hugging Face**: Language models and transformers
- **Pinecone**: Vector database for semantic search
- **Streamlit**: Web application framework
- **Sentence Transformers**: Text embeddings
- **Python**: Core programming language

## 📋 Prerequisites

- Python 3.8 or higher
- Hugging Face account and API token
- Pinecone account and API key (optional but recommended)
- Git (for cloning the repository)

## 🚀 Quick Start

### 1. Clone the Repository

```bash
git clone <repository-url>
cd basketball-chatbot
```

### 2. Run the Setup Script

```bash
python setup.py
```

The setup script will:
- Check Python version compatibility
- Install all required dependencies
- Guide you through API key configuration
- Test the installation
- Create sample basketball knowledge

### 3. Manual Setup (Alternative)

If you prefer manual setup:

#### Install Dependencies

```bash
pip install -r requirements.txt
```

#### Configure Environment Variables

Create a `.env` file in the project root:

```env
# Hugging Face API Token
HUGGINGFACE_API_TOKEN=your_huggingface_token_here

# Pinecone API Key (optional)
PINECONE_API_KEY=your_pinecone_api_key_here
PINECONE_ENVIRONMENT=your_pinecone_environment_here
PINECONE_INDEX_NAME=basketball-analysis

# Model Configuration
MODEL_NAME=microsoft/DialoGPT-medium
EMBEDDING_MODEL=sentence-transformers/all-MiniLM-L6-v2
```

### 4. Run the Application

```bash
streamlit run app.py
```

The application will open in your default browser at `http://localhost:8501`.

## 🔑 API Keys Setup

### Hugging Face API Token

1. Go to [Hugging Face Settings](https://huggingface.co/settings/tokens)
2. Create a new token
3. Copy the token and add it to your `.env` file

### Pinecone API Key (Optional)

1. Go to [Pinecone Console](https://app.pinecone.io/)
2. Create an account and get your API key
3. Note your environment (e.g., `us-east-1-aws`)
4. Add both to your `.env` file

**Note**: The chatbot will work without Pinecone, but vector search capabilities will be limited.

## 🏀 Basketball Knowledge Base

The chatbot includes comprehensive basketball knowledge covering:

### 📋 Rules and Regulations
- Basic basketball rules
- Scoring system
- Game duration and timing
- Fouls and violations

### 👥 Player Positions
- Point Guard (PG)
- Shooting Guard (SG)
- Small Forward (SF)
- Power Forward (PF)
- Center (C)

### 🎯 Strategies and Tactics
- Pick and roll
- Zone defense
- Man-to-man defense
- Fast break
- Half-court offense

### 📊 Statistics and Analytics
- Points per game (PPG)
- Rebounds per game (RPG)
- Assists per game (APG)
- Field goal percentage (FG%)
- Three-point percentage (3P%)
- Player efficiency rating (PER)

## 💬 Usage Examples

### Basic Questions
- "What are the rules of basketball?"
- "How many points is a three-pointer worth?"
- "What is a pick and roll?"

### Player Analysis
- "What are the responsibilities of a point guard?"
- "How do you calculate field goal percentage?"
- "What makes a good shooting guard?"

### Strategy Questions
- "What is zone defense?"
- "How does a fast break work?"
- "What are the different offensive strategies?"

## 🏗️ Project Structure

```
basketball-chatbot/
├── app.py                 # Main Streamlit application
├── basketball_chatbot.py  # Core chatbot logic
├── basketball_knowledge.py # Basketball knowledge base
├── vector_store.py        # Pinecone vector database operations
├── config.py             # Configuration management
├── setup.py              # Setup script
├── requirements.txt      # Python dependencies
├── env_example.txt       # Environment variables template
├── README.md            # This file
└── .env                 # Environment variables (created during setup)
```

## 🔧 Configuration Options

### Model Configuration

You can customize the language model in `config.py`:

```python
MODEL_NAME = "meta-llama/Llama-2-7b-chat-hf"  # For Llama-2 (requires access)
MODEL_NAME = "microsoft/DialoGPT-medium"      # Default (no access required)
```

### Vector Database Settings

```python
VECTOR_DIMENSION = 384    # Embedding dimension
METRIC = "cosine"        # Similarity metric
CHUNK_SIZE = 1000        # Text chunk size
CHUNK_OVERLAP = 200      # Chunk overlap
```

## 🚀 Advanced Features

### Custom Knowledge Addition

You can extend the basketball knowledge base by modifying `basketball_knowledge.py`:

```python
def get_custom_knowledge(self):
    return [
        {
            "title": "Your Custom Topic",
            "content": "Your custom basketball knowledge here."
        }
    ]
```

### Model Customization

To use different models, update the configuration:

```python
# For Llama-2 (requires Hugging Face access)
MODEL_NAME = "meta-llama/Llama-2-7b-chat-hf"

# For other models
MODEL_NAME = "gpt2"  # Smaller model
MODEL_NAME = "EleutherAI/gpt-neo-125M"  # Alternative
```

## 🐛 Troubleshooting

### Common Issues

1. **Import Errors**: Make sure all dependencies are installed
   ```bash
   pip install -r requirements.txt
   ```

2. **API Key Errors**: Verify your API keys are correctly set in `.env`
   ```bash
   cat .env  # Check your environment variables
   ```

3. **Model Loading Issues**: Try using the default DialoGPT model
   ```python
   MODEL_NAME = "microsoft/DialoGPT-medium"
   ```

4. **Pinecone Connection Issues**: Check your environment and API key
   ```python
   PINECONE_ENVIRONMENT = "us-east-1-aws"  # Verify your environment
   ```

### Performance Optimization

- Use smaller models for faster responses
- Reduce `MAX_LENGTH` for quicker generation
- Adjust `TEMPERATURE` for more focused responses

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- **LangChain** for conversation management
- **Hugging Face** for language models
- **Pinecone** for vector database
- **Streamlit** for the web interface
- **Basketball community** for knowledge and insights

## 📞 Support

If you encounter any issues or have questions:

1. Check the troubleshooting section
2. Review the configuration options
3. Open an issue on GitHub
4. Check the documentation

---

**Happy Basketball Analysis! 🏀** 