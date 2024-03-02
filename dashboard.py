import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

def create_answer_for_question_1_df(df):
  answer_for_question_1_df = day_df.groupby(by="season_without_decode").agg({
  "cnt":"sum"}).reset_index()
  answer_for_question_1_df.rename(columns={
    "season_without_decode" : "season"
  }, inplace = True)
  return answer_for_question_1_df

def create_answer_for_question_2_df(df):
  answer_for_question_2_df = day_df.groupby(by = "working_or_holiday_without_decode").agg({
    "cnt" : "sum"
  }).reset_index()
  answer_for_question_2_df.rename(columns={
    "working_or_holiday_without_decode" : "Day category"
  }, inplace = True)
  return answer_for_question_2_df

#Load data
day_df = pd.read_csv("day_cleaned.csv")

#Prepare for data frame
answer_for_question_1_df = create_answer_for_question_1_df(day_df)
answer_for_question_2_df = create_answer_for_question_2_df(day_df)

st.header('Final Project Dashboard :sparkles:')
st.subheader("Number of bike rent by season")

fig, ax = plt.subplots(figsize=(16, 8))
colors = ["#D3D3D3", "#D3D3D3","#72BCD4", "#D3D3D3",]
sns.barplot(
    y='season',
    x='cnt',
    data=answer_for_question_1_df,
    palette=colors
)
plt.title("Number of bike sharing by seasons", loc="center", fontsize=15)
plt.xlabel("Number of bike sharing (*10^6)")
plt.ylabel(None)
st.pyplot(fig)

st.subheader("Number of bike rent by day category")

fig, ax = plt.subplots(figsize=(16, 8))
colors = ["#D3D3D3", "#72BCD4"]
sns.barplot(
    y='Day category',
    x='cnt',
    data=answer_for_question_2_df,
    palette=colors
)
plt.title("Number of bike sharing by day category", loc="center", fontsize=15)
plt.xlabel("Number of bike sharing (*10^6)")
plt.ylabel(None)
st.pyplot(fig)
