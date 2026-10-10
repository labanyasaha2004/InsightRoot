# InsightRoot — Data Analytics & Root Cause Analysis

InsightRoot is an end-to-end data analytics project designed to transform raw data into actionable business insights through data cleaning, exploratory data analysis (EDA), statistical analysis, and root cause analysis.

## Project Overview

The project follows a structured analytics workflow, from generating and preparing data to identifying trends, investigating performance issues, and presenting insights through an interactive dashboard.

## Features

- **Data Generation:** Generate or prepare the dataset for analysis.
- **Data Cleaning:** Handle missing values, duplicates, inconsistent data, and data quality issues.
- **Exploratory Data Analysis (EDA):** Identify trends, patterns, distributions, and relationships in the data.
- **Root Cause Analysis:** Investigate factors contributing to changes in key metrics and business performance.
- **Interactive Dashboard:** Explore analytical findings and visualize key performance indicators.

## Project Structure

```text
InsightRoot/
├── app/
│   └── # Dashboard application
├── notebooks/
│   ├── 01_data_generation.ipynb
│   ├── 02_data_cleaning.ipynb
│   ├── 03_eda.ipynb
│   └── 04_root_cause_engine.ipynb
├── src/
│   └── # Source code and analytical modules
├── .gitignore
├── README.md
└── requirements.txt
```

## Tech Stack

- **Language:** Python
- **Data Analysis:** Pandas, NumPy
- **Visualization:** Matplotlib, Seaborn, Plotly (as applicable)
- **Dashboard:** Streamlit (if used in the application)
- **Development:** Jupyter Notebook, Visual Studio Code, Git, GitHub

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/labanyasaha2004/InsightRoot.git
cd InsightRoot
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the environment

**Windows — Command Prompt:**

```bash
venv\Scripts\activate
```

**Windows — PowerShell:**

```powershell
.\venv\Scripts\Activate.ps1
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the notebooks

Open the project in Jupyter Notebook or Visual Studio Code and execute the notebooks in the following order:

1. `01_data_generation.ipynb`
2. `02_data_cleaning.ipynb`
3. `03_eda.ipynb`
4. `04_root_cause_engine.ipynb`

### 6. Launch the dashboard

If the Streamlit application is located at `app/app.py`, run:

```bash
streamlit run app/app.py
```

Update the command if your dashboard's entry-point filename is different.

## Analytical Workflow

1. Generate or load the raw dataset.
2. Clean and validate the data.
3. Perform exploratory data analysis.
4. Identify significant trends and anomalies.
5. Investigate potential root causes using data-driven analysis.
6. Present findings through visualizations and an interactive dashboard.

## Project Goals

- Develop practical data analytics skills.
- Apply statistical methods to investigate business problems.
- Build a reproducible analytics workflow.
- Communicate findings through clear, actionable visualizations.

## Future Improvements

- Add automated data quality checks.
- Integrate interactive KPI monitoring.
- Expand root cause analysis with statistical testing.
- Deploy the dashboard for public access.
- Add sample visualizations and documented case studies.

## Author

**Labanya Saha**

GitHub: [@labanyasaha2004](https://github.com/labanyasaha2004)

---

*InsightRoot — Turning data into insights.*
