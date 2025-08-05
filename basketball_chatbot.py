from langchain.llms import HuggingFacePipeline
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline
from typing import List, Dict, Any
import torch
from config import Config
from vector_store import VectorStore
from basketball_knowledge import BasketballKnowledgeBase

class BasketballChatbot:
    """Main basketball analysis chatbot using LangChain and Hugging Face."""
    
    def __init__(self):
        self.config = Config()
        self.vector_store = VectorStore()
        self.knowledge_base = BasketballKnowledgeBase()
        self._initialize_model()
    
    def _initialize_model(self):
        """Initialize the Hugging Face model."""
        try:
            print("Loading Hugging Face model...")
            
            # Use a smaller, more accessible model
            model_name = "microsoft/DialoGPT-medium"
            
            self.tokenizer = AutoTokenizer.from_pretrained(model_name)
            self.model = AutoModelForCausalLM.from_pretrained(model_name)
            
            self.pipe = pipeline(
                "text-generation",
                model=self.model,
                tokenizer=self.tokenizer,
                max_length=512,
                temperature=0.7
            )
            
            self.llm = HuggingFacePipeline(pipeline=self.pipe)
            print("Model loaded successfully!")
            
        except Exception as e:
            print(f"Error loading model: {e}")
            raise
    
    def setup_knowledge_base(self):
        """Set up the basketball knowledge base."""
        try:
            print("Setting up basketball knowledge base...")
            knowledge_items = self.knowledge_base.get_all_basketball_knowledge()
            self.vector_store.add_basketball_knowledge(knowledge_items)
            print("Knowledge base setup complete!")
        except Exception as e:
            print(f"Error setting up knowledge base: {e}")
    
    def get_relevant_context(self, question: str) -> str:
        """Get relevant context from vector database."""
        try:
            similar_items = self.vector_store.search_similar(question, top_k=3)
            context_parts = [f"{item['title']}: {item['content']}" for item in similar_items]
            return "\n\n".join(context_parts)
        except Exception as e:
            print(f"Error getting context: {e}")
            return ""
    
    def generate_response(self, question: str) -> str:
        """Generate a response to a user question."""
        try:
            context = self.get_relevant_context(question)
            
            prompt = f"""
You are a basketball expert. Use this context to answer: {context}

Question: {question}

Answer:"""
            
            response = self.llm(prompt)
            
            if isinstance(response, dict):
                response = response.get('generated_text', '')
            
            if prompt in response:
                response = response.replace(prompt, '').strip()
            
            return response
            
        except Exception as e:
            print(f"Error generating response: {e}")
            return "I'm having trouble processing your question. Please try asking about basketball rules, positions, or strategies." 