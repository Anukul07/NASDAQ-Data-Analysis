#### NASDAQ Corporate Financial Analysis

## This project retrieves, cleans, and analyzes corporate financial data from the Nasdaq Data Link API (using the MER/F1 table). The primary goal is to analyze the 'Accrued Expenses Turnover' metric to identify time-series trends and compare financial performance across geographical regions.

---

## Key Findings & Visualizations

The analysis uncovered several key insights, most importantly that the dataset is heavily skewed by extreme outliers. This required separating the data into a "Core Group" and an "Outlier Group" for meaningful analysis.

#### Finding 1: Time-Series Trend (Core Group)

After removing outliers (like Ultrapetrol and Nielsen) that squashed the y-axis, the trends of the "core" companies became clear. The analysis shows two distinct profiles: companies with clear downward trends (like Apple Inc.) and companies that are volatile but stable in a narrow range (like Accenture plc).

#### Finding 2: Geographical Averages

The geographical analysis shows that the average turnover ratio by country is heavily influenced by the outliers. The Bahamas (home to Ultrapetrol) and the United States (home to Nielsen) show significantly higher averages, confirming that these companies belong in different class from the rest of the dataset.

#### Finding 3: Data Integrity

A key part of the project was identifying and handling data integrity issues.

- Outliers: The 'Accrued Expenses Turnover' metric ranged from ~7 to over 200, making a single-scale analysis impossible.
- Unreliable Columns: The region column was found to be unreliable (e.g., a company with country as 'USA' had region as 'Europe'). The analysis pivoted to use the more accurate country_code column instead.

---

## Tech stack

- Python
- Pandas: For data manipulation and cleaning.
- Matplotlib & Seaborn: For data visualization.
- Jupyter Notebook: For EDA.
- Nasdaq Data Link API: For data retrieval.
- Dotenv: For secure API key management.

---

## To run this project

1. Clone the repository
   git clone https://github.com/Anukul07/NASDAQ-Data-Analysis.git
   cd NASDAQ-Data-Analysis
2. Set up the Conda Environment
   conda env create -f environment.yml
   conda activate venv
3. Set up your API Key
   1. Create a file named .env in the root of the project folder.
   2. Then add your API key : NASDAQ_API_KEY="API_KEY_HERE"
4. Run the Analysis
   Navigate to notebooks/financial_analysis.ipynb and run the cells.

---

## Project structure

The repository is organized to separate exploratory code from reusable functions and data.
NASDAQ-Data-Analysis/
├── .gitignore  
├── README.md  
├── environment.yml  
├── .env  
│
├── notebooks/
│ └── financial_analysis.ipynb # Main notebook with analysis
│
├── src/
│ ├── **init**.py  
│ ├── data_retrieval.py # Module for fetching data from the API
│ └── analysis.py # Module for cleaning & enhancing data
│
├── data/
│ ├── .gitignore  
│ ├── raw/ # (Empty) For raw API output
│ └── processed/ # (Empty) For cleaned data
│
└── charts/
├── core_group_trend.png  
 └── country_avg_bar.png
