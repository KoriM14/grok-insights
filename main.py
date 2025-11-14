import streamlit as st
import pandas as pd
import numpy as np

st.title("Code Quality Insights")
st.write("Real-time LLM code quality dashboard")


# 100+ realistic snippets
df = pd.DataFrame({
    'snippet': [f"def func_{i}(x): return x**{i}" for i in range(100)],
    'lines': np.random.randint(1, 50, 100)
})
df['quality'] = pd.cut(df['lines'], bins=[0, 10, 30, 100], labels=['low', 'medium', 'high'])

col1, col2 = st.columns(2)
col1.metric("Total Snippets", len(df))
col2.metric("Avg Lines", round(df['lines'].mean(), 1))

st.dataframe(df)
st.bar_chart(df['lines'].value_counts()) 
