import streamlit as st
import random

# Set page config
st.set_page_config(
    page_title="Growth Mindset App",
    page_icon="🌱",
    layout="centered"
)

# Title and introduction
st.title("🌱 Growth Mindset Journey")
st.write("Develop and strengthen your growth mindset with this interactive app!")

# Growth mindset quotes
growth_quotes = [
    "The only way to learn is to challenge yourself.",
    "Mistakes are proof that you're trying.",
    "Everything is hard before it becomes easy.",
    "Your effort determines your success.",
    "The more you learn, the more you grow."
]

# Display random quote
st.subheader("💭 Quote of the Day")
st.info(random.choice(growth_quotes))

# Growth mindset assessment
st.subheader("📝 Quick Self-Assessment")
st.write("Rate yourself on these statements (1 = Strongly Disagree, 5 = Strongly Agree):")

questions = {
    "I believe I can improve my abilities through effort": 0,
    "I see challenges as opportunities to learn": 0,
    "I learn from feedback and criticism": 0,
    "I persist when facing setbacks": 0
}

for question in questions.keys():
    questions[question] = st.slider(question, 1, 5, 3)

total_score = sum(questions.values())
max_score = len(questions) * 5

# Display results
st.subheader("🎯 Your Growth Mindset Score")
score_percentage = (total_score / max_score) * 100
st.progress(score_percentage / 100)
st.write(f"Your score: {total_score}/{max_score} ({score_percentage:.1f}%)")

# Provide feedback based on score
if score_percentage >= 80:
    st.success("Great job! You have a strong growth mindset!")
elif score_percentage >= 60:
    st.info("You're on the right track! Keep developing your growth mindset.")
else:
    st.warning("There's room for improvement. Remember, your abilities can be developed!")

# Growth mindset tips
st.subheader("🌟 Tips for Developing a Growth Mindset")
tips = [
    "Embrace challenges as opportunities",
    "Learn from criticism and feedback",
    "Put in effort and practice regularly",
    "Stay persistent through setbacks",
    "Get inspired by others' success"
]

for tip in tips:
    st.write(f"• {tip}")

# Add a motivational button
if st.button("Get Motivated! 🚀"):
    st.balloons()
    st.write("You've got this! Every step forward is progress!")
