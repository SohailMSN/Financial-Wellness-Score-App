import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import time
import random

# Function to Calculate Financial Wellness Score
def calculate_score(income, savings, debt, investments, expenses):
    savings_ratio = (savings / income) * 30 if income > 0 else 0
    debt_ratio = (1 - (debt / income)) * 30 if income > 0 else 30
    investment_ratio = (investments / income) * 20 if income > 0 else 0
    expense_ratio = (1 - (expenses / income)) * 20 if income > 0 else 20
    return max(0, min(100, savings_ratio + debt_ratio + investment_ratio + expense_ratio))

# Fun Financial Wisdom
money_tips = [
    "💡 The key to financial success is consistency! Keep saving regularly.",
    "📈 Investing early means financial freedom later. Start today!",
    "💳 Avoid high-interest debt—credit card debt is a silent killer!",
    "🏡 Buying a home? Ensure your mortgage is under 30% of your income.",
    "🚀 Small investments now = big wealth later. Stay patient!",
]

# Streamlit UI Setup
st.set_page_config(page_title="💰 Financial Wellness Hub - By Sohail Nasir", layout="wide")
st.title("💰 **Ultimate Financial Wellness Hub** 🚀")
st.markdown("### Find out how financially fit you are and level up your wealth! 🎯")

# Sidebar Inputs
st.sidebar.header("🔢 **Enter Your Financial Details**")
income = st.sidebar.number_input("💵 Monthly Income (USD)", min_value=0, value=5000)
savings = st.sidebar.number_input("🏦 Savings Amount (USD)", min_value=0, value=1000)
investments = st.sidebar.number_input("📈 Investments (USD)", min_value=0, value=2000)
debt = st.sidebar.number_input("💳 Debt Amount (USD)", min_value=0, value=500)
expenses = st.sidebar.number_input("💸 Monthly Expenses (USD)", min_value=0, value=2500)

# Net Worth Calculation
net_worth = (savings + investments) - debt
st.sidebar.markdown(f"### 🌟 **Net Worth:** **${net_worth:,}**")

# Calculate Score
score = calculate_score(income, savings, debt, investments, expenses)

# Display Score with Emojis & Progress Bar
st.markdown("## 🎯 **Your Financial Wellness Score:**")
progress_color = "green" if score >= 70 else "orange" if score >= 40 else "red"
emoji = "😃" if score >= 70 else "😐" if score >= 40 else "😢"
st.progress(score / 100)
st.markdown(f"### {emoji} **{score}/100**")

# Gamification: Unlock Achievements
if score >= 90:
    st.balloons()
    st.success("🏆 **Financial Guru!** You're a pro at managing money!")
elif score >= 70:
    st.success("🚀 **Wealth Builder!** Keep pushing, you're on the right path!")
elif score >= 40:
    st.warning("⚠️ **Financial Learner!** You're doing okay, but there's room for improvement!")
else:
    st.error("🚨 **Debt Warrior!** Focus on reducing expenses and boosting savings ASAP!")

# Financial Tip of the Day
st.markdown(f"📜 **Tip of the Day:** {random.choice(money_tips)}")

# 📊 Financial Breakdown (Bar Chart)
st.subheader("📊 **Your Financial Breakdown**")
fig, ax = plt.subplots(figsize=(7, 5))
categories = ["Savings", "Debt", "Investments", "Expenses"]
values = [savings, debt, investments, expenses]
ax.bar(categories, values, color=["green", "red", "blue", "orange"])
ax.set_ylabel("Amount (USD)")
ax.set_title("Your Financial Breakdown")
st.pyplot(fig)

# 🎯 Savings Goal Tracker
st.subheader("🎯 **Set Your Savings Goal!**")
goal_amount = st.number_input("🎯 Target Savings Amount (USD)", min_value=0, value=10000)
goal_progress = (savings / goal_amount) * 100 if goal_amount > 0 else 0
st.progress(goal_progress / 100)
st.markdown(f"🚀 **You’ve saved {goal_progress:.2f}% towards your goal!**")

# 📈 Debt Payoff Calculator
st.subheader("📉 **Debt Payoff Plan**")
extra_payment = st.slider("💰 Extra Monthly Payment Towards Debt (USD)", 0, 1000, 100)
months_to_payoff = debt / extra_payment if extra_payment > 0 else 0
st.markdown(f"📅 **Estimated Debt-Free Time:** {months_to_payoff:.1f} months")

# 📈 Income Growth Projection
st.subheader("📈 **Income Growth Projection**")
growth_rate = st.slider("📊 Expected Annual Income Growth Rate (%)", 0, 20, 5)
years = np.arange(1, 11)
future_income = [income * (1 + (growth_rate / 100)) ** year for year in years]

fig, ax = plt.subplots(figsize=(7,5))
ax.plot(years, future_income, marker='o', linestyle='-', color='blue', label="Projected Income")
ax.set_xlabel("Years")
ax.set_ylabel("Income (USD)")
ax.set_title("Income Growth Over the Next 10 Years")
ax.legend()
st.pyplot(fig)

# 📊 Scenario Analysis
st.subheader("🔄 **Scenario Analysis: Adjust Savings & Debt**")
adjust_savings = st.slider("Increase Savings by (%)", -50, 100, 0)
adjust_debt = st.slider("Reduce Debt by (%)", -100, 100, 0)

new_savings = savings * (1 + adjust_savings / 100)
new_debt = debt * (1 - adjust_debt / 100)
new_score = calculate_score(income, new_savings, new_debt, investments, expenses)

# Show New Score with Animated Celebration
st.markdown(f"### 📈 **New Score after Adjustments:** **{new_score}/100**")
if new_score > score:
    st.balloons()
elif new_score < score:
    st.warning("⚠️ Be careful! This adjustment lowers your score.")

fig, ax = plt.subplots(figsize=(7,5))
ax.bar(["Current Score", "New Score"], [score, new_score], color=["red", "green"])
ax.set_ylabel("Score")
ax.set_title("Financial Score Comparison")
st.pyplot(fig)

# 📊 Historical Tracking (Simulated)
st.subheader("📊 **Your Financial Score Over Time (Simulated)**")
past_scores = np.clip(np.random.normal(loc=score, scale=10, size=10), 0, 100)
years = np.arange(10, 0, -1)

fig, ax = plt.subplots(figsize=(7,5))
ax.plot(years, past_scores, marker='o', linestyle='-', color='purple', label="Historical Score")
ax.axhline(y=score, color="red", linestyle="--", label="Current Score")
ax.set_xlabel("Years Ago")
ax.set_ylabel("Financial Score")
ax.set_title("Your Financial Score Trend (Past 10 Years)")
ax.legend()
st.pyplot(fig)

# Footer
st.markdown("---")
st.markdown("💡 **Tip by Sohail Nasir:** Aim for a score above 80 for financial stability. 🚀")


