import json
from typing import List, Dict

class LeetCodeTracker:
    def __init__(self, file_path: str = "problems.json"):
        self.file_path = file_path
    
    def load_problems(self) -> List[Dict]:
        with open(self.file_path, "r") as f:
            return json.load(f)["problems"]
    
    def get_stats(self) -> Dict:
        problems = self.load_problems()
        solved = [p for p in problems if p["solved"]]
        return {
            "total_solved": len(solved),
            "by_difficulty": {
                "easy": len([p for p in solved if p["difficulty"] == "easy"]),
                "medium": len([p for p in solved if p["difficulty"] == "medium"]),
                "hard": len([p for p in solved if p["difficulty"] == "hard"])
            }
        }
    
    def recommend_problem(self) -> Dict:
        problems = [p for p in self.load_problems() if not p["solved"]]
        return problems[0] if problems else None