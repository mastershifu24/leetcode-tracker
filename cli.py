from tracker import LeetCodeTracker
import typer

app = typer.Typer()
tracker = LeetCodeTracker()

@app.command()
def stats():
    stats = tracker.get_stats()
    print(f"Solved: {stats['total_solved']}")
    print(f"Easy: {stats['by_difficulty']['easy']}")
    print(f"Medium: {stats['by_difficulty']['medium']}")
    print(f"Hard: {stats['by_difficulty']['hard']}")

@app.command()
def recommend():
    problem = tracker.recommend_problem()
    if problem:
        print(f"Try: {problem['title']} ({problem['difficulty']})")
    else:
        print("All problems solved!")

if __name__ == "__main__":
    app()