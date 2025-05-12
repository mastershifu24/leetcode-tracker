import streamlit as st
from tracker import LeetCodeTracker

tracker = LeetCodeTracker()
st.title("LeetCode Progress")

stats = tracker.get_stats()
st.metric("Total Solved", stats["total_solved"])
st.bar_chart(stats["by_difficulty"])

recommendation = tracker.recommend_problem()
if recommendation:
    st.write("Next recommended problem:")
    st.code(f"{recommendation['title']} ({recommendation['difficulty']})")
else:
    st.success("All problems solved! 🎉")