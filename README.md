# 🚉 Minimum Railway Platforms

A Python project that calculates the minimum number of railway platforms required for a given train schedule. It uses a sorting-based algorithm and an interactive Streamlit web application to display the results and visualize platform usage.

**GitHub Repository:** https://github.com/Dhruvv125/Minimum-Railway-Platforms

## 📌 Project Overview

Railway stations need sufficient platforms to accommodate trains arriving and departing at different times. This project calculates the minimum number of platforms required so that no train has to wait because a platform is unavailable.

The application generates train schedules, analyzes overlapping arrival and departure times, and displays the result with a graph.

## ✨ Features

- Generate random train schedules for 10 to 200 trains.
- Display train IDs, arrival times, and departure times.
- Calculate the minimum number of platforms required.
- Display peak train concurrency.
- Visualize platform usage with Matplotlib.
- Explore algorithm examples and related computer science concepts.
- Use a Jupyter Notebook for further learning.

## 🧰 Technologies Used

- **Python** — Main programming language
- **Streamlit** — Interactive web application
- **Pandas** — Data handling
- **Matplotlib** — Graph visualization
- **Jupyter Notebook** — Algorithm exploration

## 📁 Project Structure

```text
Minimum-Railway-Platforms/
├── streamlit_app.py
├── Minimum Platform.ipynb
├── train_schedule.csv
├── requirements.txt
└── README.md
```

## ⚙️ Requirements

- Python 3.10–3.12 recommended
- pip
- Visual Studio Code (optional)

## 🚀 Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/Dhruvv125/Minimum-Railway-Platforms.git
cd Minimum-Railway-Platforms
```

Alternatively, download the repository as a ZIP file and extract it.

### 2. Create a virtual environment

**Windows (PowerShell):**

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
```

**macOS / Linux:**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

The project's pinned dependencies are:

- `streamlit==1.38.0`
- `pandas==2.2.2`
- `matplotlib==3.9.2`

### 4. Run the application

```bash
python -m streamlit run streamlit_app.py
```

Open the local URL shown in the terminal, usually:

```text
http://localhost:8501
```

## 💻 Running in VS Code

1. Open the project folder in VS Code.
2. Select **Terminal → New Terminal**.
3. Create and activate the virtual environment.
4. Install the dependencies using `python -m pip install -r requirements.txt`.
5. Press `Ctrl + Shift + P`.
6. Select **Python: Select Interpreter**.
7. Choose the Python interpreter inside `.venv`.
8. Run the following command:

```powershell
python -m streamlit run streamlit_app.py
```

9. Open the URL displayed in the terminal.

## 🧠 Algorithm

The minimum-platform problem can be solved by sorting the arrival and departure times separately.

1. Sort all arrival times.
2. Sort all departure times.
3. Compare the next arrival time with the next departure time.
4. If a train arrives before the next train departs, increase the number of occupied platforms.
5. Otherwise, decrease the number of occupied platforms because a train has departed.
6. Track the maximum number of simultaneously occupied platforms.

The maximum number of simultaneously occupied platforms is the minimum number of platforms required.

### Time Complexity

For `n` trains:

- **Time Complexity:** `O(n log n)`, primarily due to sorting.
- **Auxiliary Space:** `O(n)` for storing the sorted times and related data.

## 📊 How to Use the Application

1. Start the Streamlit application.
2. Select the number of trains using the slider.
3. Click **Generate Schedule and Analyze**.
4. View the generated train schedule.
5. Check the calculated minimum number of platforms.
6. Examine the graph showing platform usage.
7. Explore the additional algorithm examples.

The generated results may change each time because the application uses random train schedules.

## 📓 Running the Jupyter Notebook

To run the notebook, install Jupyter:

```bash
python -m pip install notebook
python -m notebook
```

Alternatively, open `Minimum Platform.ipynb` using the Jupyter extension in VS Code.

## 📂 Dataset

The project includes `train_schedule.csv`, which contains train schedule data for reference and analysis.

**Note:** The current Streamlit application generates random schedules and does not directly load the CSV file as its input.

## ⚠️ Limitations

- **Midnight rollover:** Train schedules crossing midnight may require date-aware calculations to avoid incorrect results.
- **Random schedules:** The main application uses randomly generated data.
- **CSV integration:** The CSV file is included but is not currently used by the main application.
- **Educational examples:** Additional algorithm examples are separate from the minimum-platform calculation.

## 🔧 Troubleshooting

### Error: `ModuleNotFoundError`

Install the dependencies:

```bash
python -m pip install -r requirements.txt
```

### Error: `streamlit` is not recognized

Run Streamlit through Python:

```bash
python -m streamlit run streamlit_app.py
```

### PowerShell activation error

Use the virtual environment's Python executable directly:

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m streamlit run streamlit_app.py
```

### Port 8501 is already in use

Run the application on another port:

```bash
python -m streamlit run streamlit_app.py --server.port 8502
```

Then open `http://localhost:8502`.

## 🎯 Project Objective

The objective of this project is to demonstrate how sorting and a greedy approach can solve a practical railway scheduling problem. The interactive interface and graph make the results easier to understand.
