import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import random
from datetime import datetime, timedelta
from collections import deque
import re

st.set_page_config(page_title="Minimum Number of Platforms", layout="wide")

st.title("🚉 Minimum Number of Platforms - Streamlit App")
st.markdown("This app simulates train schedules and calculates the **minimum number of platforms** needed so that no train waits.")

# --- Step 1: User Input for Number of Trains ---
n = st.slider("Select number of trains to simulate", 10, 200, 50)

# --- Step 2: Generate Random Train Data ---
def generate_train_data(n):
    arrivals, departures, train_ids = [], [], [f"T{i+1}" for i in range(n)]
    for _ in range(n):
        arr_hour = random.randint(0, 23)
        arr_min = random.randint(0, 59)
        arr_time = f"{arr_hour:02d}:{arr_min:02d}"
        duration = random.randint(15, 180)
        arr_dt = datetime.strptime(arr_time, "%H:%M")
        dep_dt = arr_dt + timedelta(minutes=duration)
        departures.append(dep_dt.strftime("%H:%M"))
        arrivals.append(arr_time)
    df = pd.DataFrame({
        "Train_ID": train_ids,
        "Arrival": arrivals,
        "Departure": departures
    })
    df["Arrival_dt"] = pd.to_datetime(df["Arrival"], format="%H:%M")
    df["Departure_dt"] = pd.to_datetime(df["Departure"], format="%H:%M")
    return df.sort_values(by="Arrival_dt").reset_index(drop=True)

if st.button("🎯 Generate Schedule and Analyze"):
    df = generate_train_data(n)

    st.subheader("📋 Generated Train Schedule")
    st.dataframe(df[["Train_ID", "Arrival", "Departure"]])

    # --- Step 3: Calculate Minimum Platforms ---
    arrivals = sorted(df["Arrival_dt"].tolist())
    departures = sorted(df["Departure_dt"].tolist())
    i = j = 0
    platforms_needed = 0
    active_counts, times = [], []

    while i < len(arrivals) and j < len(departures):
        if arrivals[i] <= departures[j]:
            platforms_needed += 1
            times.append(arrivals[i])
            active_counts.append(platforms_needed)
            i += 1
        else:
            platforms_needed -= 1
            times.append(departures[j])
            active_counts.append(platforms_needed)
            j += 1

    min_platforms = max(active_counts)
    peak_index = active_counts.index(min_platforms)
    peak_time = times[peak_index].strftime("%H:%M")

    st.success(f"✅ **Minimum Platforms Required:** {min_platforms}")
    st.info(f"🕒 **Peak Concurrency:** {min_platforms} trains at {peak_time}")

    # --- Step 4: Visualization ---
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.plot(times, active_counts, label="Active Trains", linewidth=2)
    ax.axhline(y=min_platforms, color='red', linestyle='--', label=f"Peak = {min_platforms}")
    ax.axvline(x=times[peak_index], color='orange', linestyle='--', label=f"Peak Time = {peak_time}")
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M'))
    ax.set_xlabel("Time of Day (HH:MM)")
    ax.set_ylabel("Platforms Needed")
    ax.set_title("Train Platform Usage Over Time")
    ax.legend()
    ax.grid(True, linestyle='--', alpha=0.6)
    st.pyplot(fig)

    # --- CO-2 to CO-6 ---
    st.subheader("🧮 Recurrence Relation")
    st.code("P(n) = max(P(n-1), Overlap(arrival_n, departures))")

    st.subheader("💡 Greedy Approach Explanation")
    st.write("The algorithm uses a **greedy strategy**: it always allocates the earliest available platform by sorting arrivals and departures, ensuring minimum waiting time and optimal usage.")

    st.subheader("🔍 String Matching Example (Train IDs containing 5–9)")
    matches = [tid for tid in df["Train_ID"].tolist() if re.search(r"T[5-9]", tid)]
    st.write(matches)

    st.subheader("📘 Problem Class & Optimality")
    st.write("**Problem Class:** P (Polynomial Time). The greedy solution is optimal since sorted arrivals/departures lead to globally optimal allocation.")

    st.subheader("🔗 Graph Dependency Example (Topological Sort)")
    graph = {"T1": ["T3"], "T2": ["T4"], "T3": [], "T4": []}

    def topological_sort(graph):
        indegree = {u: 0 for u in graph}
        for u in graph:
            for v in graph[u]:
                indegree[v] += 1
        queue = deque([u for u in indegree if indegree[u] == 0])
        topo_order = []
        while queue:
            u = queue.popleft()
            topo_order.append(u)
            for v in graph[u]:
                indegree[v] -= 1
                if indegree[v] == 0:
                    queue.append(v)
        return topo_order

    st.code(str(topological_sort(graph)))

# --- Footer ---
st.markdown("---")
