import pinecone
from sentence_transformers import SentenceTransformer
from typing import List, Dict, Any
import uuid
from config import Config

class VectorStore:
    """Class to manage Pinecone vector database operations."""
    
    def __init__(self):
        self.config = Config()
        self.embedding_model = SentenceTransformer(self.config.EMBEDDING_MODEL)
        self._initialize_pinecone()
    
    def _initialize_pinecone(self):
        """Initialize Pinecone client and index."""
        try:
            pinecone.init(
                api_key=self.config.PINECONE_API_KEY,
                environment=self.config.PINECONE_ENVIRONMENT
            )
            
            # Check if index exists, if not create it
            if self.config.PINECONE_INDEX_NAME not in pinecone.list_indexes():
                pinecone.create_index(
                    name=self.config.PINECONE_INDEX_NAME,
                    dimension=self.config.VECTOR_DIMENSION,
                    metric=self.config.METRIC
                )
                print(f"Created Pinecone index: {self.config.PINECONE_INDEX_NAME}")
            
            self.index = pinecone.Index(self.config.PINECONE_INDEX_NAME)
            print(f"Connected to Pinecone index: {self.config.PINECONE_INDEX_NAME}")
            
        except Exception as e:
            print(f"Error initializing Pinecone: {e}")
            raise
    
    def create_embeddings(self, texts: List[str]) -> List[List[float]]:
        """Create embeddings for a list of texts."""
        try:
            embeddings = self.embedding_model.encode(texts)
            return embeddings.tolist()
        except Exception as e:
            print(f"Error creating embeddings: {e}")
            raise
    
    def add_basketball_knowledge(self, knowledge_items: List[Dict[str, str]]):
        """Add basketball knowledge items to the vector database."""
        try:
            vectors = []
            
            for item in knowledge_items:
                # Combine title and content for embedding
                text = f"{item['title']}: {item['content']}"
                embedding = self.create_embeddings([text])[0]
                
                vector = {
                    'id': str(uuid.uuid4()),
                    'values': embedding,
                    'metadata': {
                        'title': item['title'],
                        'content': item['content'],
                        'type': 'basketball_knowledge'
                    }
                }
                vectors.append(vector)
            
            # Insert vectors in batches
            batch_size = 100
            for i in range(0, len(vectors), batch_size):
                batch = vectors[i:i + batch_size]
                self.index.upsert(vectors=batch)
            
            print(f"Added {len(vectors)} basketball knowledge items to vector database")
            
        except Exception as e:
            print(f"Error adding basketball knowledge: {e}")
            raise
    
    def search_similar(self, query: str, top_k: int = 5) -> List[Dict[str, Any]]:
        """Search for similar basketball knowledge based on a query."""
        try:
            # Create embedding for the query
            query_embedding = self.create_embeddings([query])[0]
            
            # Search in Pinecone
            results = self.index.query(
                vector=query_embedding,
                top_k=top_k,
                include_metadata=True
            )
            
            # Format results
            formatted_results = []
            for match in results.matches:
                formatted_results.append({
                    'id': match.id,
                    'score': match.score,
                    'title': match.metadata.get('title', ''),
                    'content': match.metadata.get('content', ''),
                    'type': match.metadata.get('type', '')
                })
            
            return formatted_results
            
        except Exception as e:
            print(f"Error searching vector database: {e}")
            return []
    
    def get_all_knowledge(self) -> List[Dict[str, Any]]:
        """Retrieve all basketball knowledge from the vector database."""
        try:
            # Fetch all vectors (this might be expensive for large datasets)
            results = self.index.query(
                vector=[0] * self.config.VECTOR_DIMENSION,  # Dummy vector
                top_k=10000,  # Large number to get all
                include_metadata=True
            )
            
            formatted_results = []
            for match in results.matches:
                if match.metadata.get('type') == 'basketball_knowledge':
                    formatted_results.append({
                        'id': match.id,
                        'title': match.metadata.get('title', ''),
                        'content': match.metadata.get('content', ''),
                        'type': match.metadata.get('type', '')
                    })
            
            return formatted_results
            
        except Exception as e:
            print(f"Error retrieving all knowledge: {e}")
            return []
    
    def delete_all_knowledge(self):
        """Delete all basketball knowledge from the vector database."""
        try:
            # Get all knowledge IDs
            all_knowledge = self.get_all_knowledge()
            ids_to_delete = [item['id'] for item in all_knowledge]
            
            if ids_to_delete:
                self.index.delete(ids=ids_to_delete)
                print(f"Deleted {len(ids_to_delete)} basketball knowledge items")
            else:
                print("No basketball knowledge items to delete")
                
        except Exception as e:
            print(f"Error deleting basketball knowledge: {e}")
            raise 