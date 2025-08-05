#!/usr/bin/env python3
"""
Setup script for Basketball Analysis Chatbot
This script helps users set up their environment and initialize the chatbot.
"""

import os
import json
import subprocess
import sys
from pathlib import Path

def check_python_version():
    """Check if Python version is compatible."""
    if sys.version_info < (3, 8):
        print("❌ Python 3.8 or higher is required.")
        print(f"Current version: {sys.version}")
        return False
    print(f"✅ Python version: {sys.version}")
    return True

def install_dependencies():
    """Install required dependencies."""
    print("\n📦 Installing dependencies...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("✅ Dependencies installed successfully!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Error installing dependencies: {e}")
        return False

def create_env_file():
    """Create .env file with user input."""
    print("\n🔧 Setting up environment variables...")
    
    env_content = []
    
    # Hugging Face API Token
    print("\n1. Hugging Face API Token:")
    print("   - Go to https://huggingface.co/settings/tokens")
    print("   - Create a new token")
    hf_token = input("   Enter your Hugging Face API token (or press Enter to skip): ").strip()
    if hf_token:
        env_content.append(f"HUGGINGFACE_API_TOKEN={hf_token}")
    
    # Pinecone API Key
    print("\n2. Pinecone API Key:")
    print("   - Go to https://app.pinecone.io/")
    print("   - Create an account and get your API key")
    pinecone_key = input("   Enter your Pinecone API key (or press Enter to skip): ").strip()
    if pinecone_key:
        env_content.append(f"PINECONE_API_KEY={pinecone_key}")
    
    # Pinecone Environment
    if pinecone_key:
        print("\n3. Pinecone Environment:")
        print("   - Check your Pinecone dashboard for the environment")
        print("   - Common values: us-east-1-aws, us-west1-gcp, eu-west1-aws")
        pinecone_env = input("   Enter your Pinecone environment: ").strip()
        if pinecone_env:
            env_content.append(f"PINECONE_ENVIRONMENT={pinecone_env}")
    
    # Model Configuration
    print("\n4. Model Configuration:")
    print("   - Using default model: microsoft/DialoGPT-medium")
    env_content.append("MODEL_NAME=microsoft/DialoGPT-medium")
    env_content.append("EMBEDDING_MODEL=sentence-transformers/all-MiniLM-L6-v2")
    
    # Pinecone Index Name
    env_content.append("PINECONE_INDEX_NAME=basketball-analysis")
    
    # Write .env file
    if env_content:
        with open(".env", "w") as f:
            f.write("\n".join(env_content))
        print("✅ .env file created successfully!")
        return True
    else:
        print("⚠️ No environment variables were set. The chatbot will work with limited functionality.")
        return False

def test_setup():
    """Test the setup by importing modules."""
    print("\n🧪 Testing setup...")
    
    try:
        # Test basic imports
        import streamlit
        print("✅ Streamlit imported successfully")
        
        import transformers
        print("✅ Transformers imported successfully")
        
        import langchain
        print("✅ LangChain imported successfully")
        
        # Test our modules
        from config import Config
        print("✅ Config module imported successfully")
        
        from basketball_knowledge import BasketballKnowledgeBase
        print("✅ Basketball knowledge module imported successfully")
        
        print("✅ All modules imported successfully!")
        return True
        
    except ImportError as e:
        print(f"❌ Import error: {e}")
        return False

def create_sample_data():
    """Create sample basketball knowledge data."""
    print("\n📚 Creating sample basketball knowledge...")
    
    try:
        from basketball_knowledge import BasketballKnowledgeBase
        
        kb = BasketballKnowledgeBase()
        kb.save_knowledge_to_file("basketball_knowledge.json")
        print("✅ Sample basketball knowledge created!")
        return True
        
    except Exception as e:
        print(f"❌ Error creating sample data: {e}")
        return False

def main():
    """Main setup function."""
    print("🏀 Basketball Analysis Chatbot Setup")
    print("=" * 50)
    
    # Check Python version
    if not check_python_version():
        return
    
    # Install dependencies
    if not install_dependencies():
        return
    
    # Create environment file
    create_env_file()
    
    # Test setup
    if not test_setup():
        print("❌ Setup test failed. Please check the error messages above.")
        return
    
    # Create sample data
    create_sample_data()
    
    print("\n🎉 Setup completed successfully!")
    print("\n📋 Next steps:")
    print("1. Make sure you have set up your API keys in the .env file")
    print("2. Run the application with: streamlit run app.py")
    print("3. Open your browser and go to the URL shown in the terminal")
    print("\n💡 Tips:")
    print("- If you don't have Pinecone API keys, the chatbot will still work with basic responses")
    print("- You can always update your .env file later with additional API keys")
    print("- Check the README.md file for more detailed instructions")

if __name__ == "__main__":
    main() 