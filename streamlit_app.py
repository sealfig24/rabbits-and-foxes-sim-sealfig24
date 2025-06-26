import streamlit as st
import pandas as pd
import colorsys
import altair as alt

st.title("🐇 Rabbits and Foxes 🦊")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)


# st.slider("Rating", min_value=1, max_value=10, step=1, key="rating")
# st.session_state["rating"]

# Parameters
rabbits = 40 # x
foxes = 9 # y

rabbits_reproduction_rate = 0.1 # alpha
predation_rate = 0.02 # beta

fox_reproduction_rate = 0.01 # delta
fox_death_rate = 0.1 # gamma

time_step = 0.1

N = 2000 # number of time steps

def change_initial_conditions():
    global rabbits, foxes
    rabbits = st.session_state["initial_rabbits"]
    foxes = st.session_state["initial_foxes"]
    print("simulating")
    st.session_state["rf_counts_df"] = simulate()
    print("done simulating")

st.number_input("Rabbits", 0, 100, value=rabbits, placeholder="Default: 40", key="initial_rabbits", on_change=change_initial_conditions)
st.number_input("Foxes", 0, 100, value=foxes, placeholder="Default: 9", key="initial_foxes", on_change=change_initial_conditions)

def simulate():
    global rabbits, foxes

    print("in simulation")
    counts = [] # [x, y] at time = index
    counts.append([rabbits, foxes]) # initialize

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
    return counts_df

if "rf_counts_df" not in st.session_state:
    st.session_state["rf_counts_df"] = simulate()

counts_df = st.session_state["rf_counts_df"]

st.dataframe(counts_df)
st.write(st.session_state)

# now you only update df everytime you change the initial conditions
# instead of updating every time the slider is moved around

min_value = 0
max_value = N
start_value = N // 2
step_size = N // 10
t = st.slider("Time",
              min_value=min_value,
              max_value=max_value,
              step=step_size,
              value=start_value
              )


st.scatter_chart(counts_df.iloc[:t, :],
                 x='rabbits', y='foxes',
                 color='color')

