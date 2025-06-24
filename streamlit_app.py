import streamlit as st
import pandas as pd

st.title("🐇 Rabbits and Foxes 🦊")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)

rabbits = 10 # x
foxes = 3 # y

rabbits_reproduction_rate = 1 # alpha
predation_rate = 2 # beta

fox_reproduction_rate = 1.8 # delta
fox_death_rate = 1.8 # gamma

time_step = 0.03

counts = [] # [x, y] at time = index
counts.append([rabbits, foxes]) # initialize

N = 1000 # number of time steps

for t in range(1, N + 1):
    
    rabbits += rabbits_reproduction_rate * rabbits - predation_rate * foxes * rabbits
    foxes += -fox_death_rate * foxes + fox_reproduction_rate * foxes * rabbits

    rabbits *= time_step
    foxes *= time_step

    rabbits = max(rabbits, 0)
    foxes = max(foxes, 0)

    counts.append([rabbits, foxes])

counts_df = pd.DataFrame(counts, columns=['rabbits', 'foxes'])
st.dataframe(counts_df)

st.scatter_chart(counts_df, x='rabbits', y='foxes')





