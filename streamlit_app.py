import streamlit as st
import pandas as pd
import colorsys

st.title("🐇 Rabbits and Foxes 🦊")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)

rabbits = 40 # x
foxes = 9 # y

rabbits_reproduction_rate = 0.1 # alpha
predation_rate = 0.02 # beta

fox_reproduction_rate = 0.01 # delta
fox_death_rate = 0.1 # gamma

time_step = 0.1

counts = [] # [x, y] at time = index
counts.append([rabbits, foxes]) # initialize

N = 2000 # number of time steps

for t in range(1, N):
    
    rabbits += (rabbits_reproduction_rate * rabbits - predation_rate * foxes * rabbits) * time_step
    foxes += (-fox_death_rate * foxes + fox_reproduction_rate * foxes * rabbits) * time_step

    # rabbits *= time_step
    # foxes *= time_step

    rabbits = max(rabbits, 0)
    foxes = max(foxes, 0)

    counts.append([rabbits, foxes])

counts_df = pd.DataFrame(counts, columns=['rabbits', 'foxes'])
counts_df['time'] = [i for i in range(N)]
# counts_df['color'] = [colorsys.hsv_to_rgb(i / N, 1.0, 1.0) for i in range(N)]
counts_df['color'] = counts_df['time'] / N
st.dataframe(counts_df)

min_value = 0
max_value = N
start_value = N // 2
step_size = 10
t = st.slider("Time",
              min_value=min_value,
              max_value=max_value,
              step=step_size,
              value=start_value)

st.scatter_chart(counts_df.iloc[:t, :], x='rabbits', y='foxes', color='color')






