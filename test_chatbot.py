#!/usr/bin/env python3
"""
Test script for Basketball Analysis Chatbot
This script tests the basic functionality of the chatbot.
"""

import sys
import os

def test_imports():
    """Test if all required modules can be imported."""
    print("🧪 Testing imports...")
    
    try:
        from config import Config
        print("✅ Config imported successfully")
        
        from basketball_knowledge import BasketballKnowledgeBase
        print("✅ Basketball knowledge imported successfully")
        
        from basketball_chatbot import BasketballChatbot
        print("✅ Basketball chatbot imported successfully")
        
        return True
        
    except ImportError as e:
        print(f"❌ Import error: {e}")
        return False

def test_knowledge_base():
    """Test the basketball knowledge base."""
    print("\n📚 Testing knowledge base...")
    
    try:
        from basketball_knowledge import BasketballKnowledgeBase
        
        kb = BasketballKnowledgeBase()
        
        # Test getting rules
        rules = kb.get_basketball_rules()
        print(f"✅ Basketball rules: {len(rules)} items")
        
        # Test getting positions
        positions = kb.get_player_positions()
        print(f"✅ Player positions: {len(positions)} items")
        
        # Test getting all knowledge
        all_knowledge = kb.get_all_basketball_knowledge()
        print(f"✅ Total knowledge items: {len(all_knowledge)}")
        
        return True
        
    except Exception as e:
        print(f"❌ Knowledge base error: {e}")
        return False

def test_config():
    """Test the configuration."""
    print("\n⚙️ Testing configuration...")
    
    try:
        from config import Config
        
        config = Config()
        
        print(f"✅ Model name: {config.MODEL_NAME}")
        print(f"✅ Embedding model: {config.EMBEDDING_MODEL}")
        print(f"✅ Vector dimension: {config.VECTOR_DIMENSION}")
        
        return True
        
    except Exception as e:
        print(f"❌ Configuration error: {e}")
        return False

def test_chatbot_basic():
    """Test basic chatbot functionality."""
    print("\n🤖 Testing basic chatbot...")
    
    try:
        from basketball_chatbot import BasketballChatbot
        
        # Initialize chatbot
        chatbot = BasketballChatbot()
        print("✅ Chatbot initialized successfully")
        
        # Test simple response
        test_question = "What is basketball?"
        response = chatbot.generate_response(test_question)
        print(f"✅ Generated response: {response[:100]}...")
        
        return True
        
    except Exception as e:
        print(f"❌ Chatbot error: {e}")
        return False

def test_vector_store():
    """Test vector store functionality (if Pinecone is configured)."""
    print("\n🔍 Testing vector store...")
    
    try:
        from config import Config
        config = Config()
        
        if not config.PINECONE_API_KEY or not config.PINECONE_ENVIRONMENT:
            print("⚠️ Pinecone not configured, skipping vector store test")
            return True
        
        from vector_store import VectorStore
        
        vector_store = VectorStore()
        print("✅ Vector store initialized successfully")
        
        # Test embedding creation
        test_texts = ["basketball", "point guard", "scoring"]
        embeddings = vector_store.create_embeddings(test_texts)
        print(f"✅ Created embeddings: {len(embeddings)} vectors")
        
        return True
        
    except Exception as e:
        print(f"❌ Vector store error: {e}")
        return False

def main():
    """Main test function."""
    print("🏀 Basketball Analysis Chatbot - Test Suite")
    print("=" * 50)
    
    tests = [
        ("Imports", test_imports),
        ("Configuration", test_config),
        ("Knowledge Base", test_knowledge_base),
        ("Basic Chatbot", test_chatbot_basic),
        ("Vector Store", test_vector_store)
    ]
    
    passed = 0
    total = len(tests)
    
    for test_name, test_func in tests:
        try:
            if test_func():
                passed += 1
            else:
                print(f"❌ {test_name} test failed")
        except Exception as e:
            print(f"❌ {test_name} test error: {e}")
    
    print("\n" + "=" * 50)
    print(f"📊 Test Results: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 All tests passed! The chatbot is ready to use.")
        print("\n🚀 To run the application:")
        print("   streamlit run app.py")
    else:
        print("⚠️ Some tests failed. Please check the error messages above.")
        print("\n💡 Common solutions:")
        print("   - Run 'python setup.py' to configure the environment")
        print("   - Check your API keys in the .env file")
        print("   - Install missing dependencies with 'pip install -r requirements.txt'")

if __name__ == "__main__":
    main() 