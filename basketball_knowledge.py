import json
from typing import List, Dict

class BasketballKnowledgeBase:
    """Class to manage basketball knowledge and data collection."""
    
    def __init__(self):
        self.basketball_data = []
        
    def get_basketball_rules(self) -> List[Dict[str, str]]:
        """Get basic basketball rules and regulations."""
        return [
            {
                "title": "Basic Basketball Rules",
                "content": "Basketball is played with two teams of five players each. The objective is to score points by shooting the ball through the opponent's hoop. A field goal is worth 2 or 3 points depending on the distance. Free throws are worth 1 point."
            },
            {
                "title": "Scoring System",
                "content": "2 points for a field goal inside the three-point line, 3 points for a field goal beyond the three-point line, and 1 point for each successful free throw."
            },
            {
                "title": "Game Duration",
                "content": "A standard basketball game consists of four quarters. In the NBA, each quarter is 12 minutes long. Overtime periods are typically 5 minutes each if the game is tied."
            }
        ]
    
    def get_player_positions(self) -> List[Dict[str, str]]:
        """Get information about basketball player positions."""
        return [
            {
                "title": "Point Guard (PG)",
                "content": "The point guard is the team's primary ball handler and playmaker. They are responsible for bringing the ball up the court, setting up offensive plays, and distributing the ball to teammates."
            },
            {
                "title": "Shooting Guard (SG)",
                "content": "The shooting guard is primarily responsible for scoring points through shooting. They often work off screens to get open shots and may also handle the ball."
            },
            {
                "title": "Small Forward (SF)",
                "content": "The small forward is often the most versatile player on the team. They can score from inside and outside, defend multiple positions, and contribute in various ways."
            },
            {
                "title": "Power Forward (PF)",
                "content": "The power forward plays near the basket and is responsible for rebounding, scoring in the paint, and defending the post."
            },
            {
                "title": "Center (C)",
                "content": "The center is typically the tallest player on the team and plays closest to the basket. They are responsible for protecting the rim on defense and rebounding."
            }
        ]
    
    def get_all_basketball_knowledge(self) -> List[Dict[str, str]]:
        """Combine all basketball knowledge into a single list."""
        all_knowledge = []
        all_knowledge.extend(self.get_basketball_rules())
        all_knowledge.extend(self.get_player_positions())
        return all_knowledge
    
    def save_knowledge_to_file(self, filename: str = "basketball_knowledge.json"):
        """Save basketball knowledge to a JSON file."""
        knowledge = self.get_all_basketball_knowledge()
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(knowledge, f, indent=2, ensure_ascii=False)
        print(f"Basketball knowledge saved to {filename}") 