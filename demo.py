#!/usr/bin/env python3
"""
Demo script for Basketball Analysis Chatbot
This script provides a simple command-line interface to test the chatbot.
"""

import sys
import os

def demo_knowledge_base():
    """Demonstrate the basketball knowledge base."""
    print("📚 Basketball Knowledge Base Demo")
    print("=" * 40)
    
    try:
        from basketball_knowledge import BasketballKnowledgeBase
        
        kb = BasketballKnowledgeBase()
        
        # Show basketball rules
        print("\n🏀 Basketball Rules:")
        rules = kb.get_basketball_rules()
        for i, rule in enumerate(rules, 1):
            print(f"{i}. {rule['title']}")
            print(f"   {rule['content']}")
            print()
        
        # Show player positions
        print("👥 Player Positions:")
        positions = kb.get_player_positions()
        for i, position in enumerate(positions, 1):
            print(f"{i}. {position['title']}")
            print(f"   {position['content']}")
            print()
        
        return True
        
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def demo_chatbot():
    """Demonstrate the chatbot functionality."""
    print("\n🤖 Basketball Chatbot Demo")
    print("=" * 40)
    print("Type 'quit' to exit the demo")
    print()
    
    try:
        from basketball_chatbot import BasketballChatbot
        
        # Initialize chatbot
        print("Initializing chatbot...")
        chatbot = BasketballChatbot()
        print("✅ Chatbot ready!")
        print()
        
        # Interactive chat loop
        while True:
            user_input = input("You: ").strip()
            
            if user_input.lower() in ['quit', 'exit', 'q']:
                print("👋 Thanks for trying the basketball chatbot!")
                break
            
            if not user_input:
                continue
            
            print("🏀 Basketball Bot: ", end="", flush=True)
            
            try:
                response = chatbot.generate_response(user_input)
                print(response)
            except Exception as e:
                print(f"Sorry, I encountered an error: {e}")
            
            print()
        
        return True
        
    except Exception as e:
        print(f"❌ Error initializing chatbot: {e}")
        print("💡 Make sure you have installed the required dependencies:")
        print("   pip install -r requirements.txt")
        return False

def demo_sample_questions():
    """Show sample questions and expected responses."""
    print("\n❓ Sample Questions Demo")
    print("=" * 40)
    
    sample_questions = [
        "What are the basic rules of basketball?",
        "What is the role of a point guard?",
        "How many points is a three-pointer worth?",
        "What are the different player positions?",
        "How long is a basketball game?"
    ]
    
    print("Here are some example questions you can ask:")
    for i, question in enumerate(sample_questions, 1):
        print(f"{i}. {question}")
    
    print("\n💡 Try asking these questions in the interactive demo!")

def main():
    """Main demo function."""
    print("🏀 Basketball Analysis Chatbot - Demo")
    print("=" * 50)
    
    print("This demo showcases the basketball analysis chatbot features.")
    print("Choose an option:")
    print("1. View Basketball Knowledge Base")
    print("2. Interactive Chat Demo")
    print("3. Sample Questions")
    print("4. Run All Demos")
    print("5. Exit")
    
    while True:
        try:
            choice = input("\nEnter your choice (1-5): ").strip()
            
            if choice == '1':
                demo_knowledge_base()
            elif choice == '2':
                demo_chatbot()
            elif choice == '3':
                demo_sample_questions()
            elif choice == '4':
                print("\n" + "="*50)
                demo_knowledge_base()
                demo_sample_questions()
                demo_chatbot()
            elif choice == '5':
                print("👋 Thanks for trying the demo!")
                break
            else:
                print("❌ Invalid choice. Please enter 1-5.")
                
        except KeyboardInterrupt:
            print("\n\n👋 Demo interrupted. Goodbye!")
            break
        except Exception as e:
            print(f"❌ Error: {e}")

if __name__ == "__main__":
    main() 