# Week 2 — Data Handling & Visualization

This week focuses on understanding datasets, performing data preprocessing, and creating meaningful visualizations as part of the AI/ML Fellowship.

## Topics Covered

- Understanding datasets and data types
- Numerical computing with NumPy
- Data manipulation using Pandas
- Data visualization with Matplotlib and Seaborn
- Data cleaning and preparation techniques
- Creating effective visual representations of data
## Task Description
This project performs Exploratory Data Analysis (EDA) to uncover patterns and relationships that influenced survival on the Titanic.

Steps performed:
- Data loading and inspection
- Data cleaning and preprocessing
- Feature engineering
- Data visualization
- Insight extraction

## Titanic Dataset EDA

The Titanic dataset contains information about passengers aboard the Titanic, including:
- PassengerId
- Survival (0 = No, 1 = Yes)
- Passenger Class (Pclass)
- Name
- Sex
- Age
- SibSp (siblings/spouses aboard)
- Parch (parents/children aboard)
- Ticket
- Fare
- Cabin


## Tools & Technologies

- Google Colab — Cloud-based notebook environment
- Python — Core programming language
- Pandas — Data manipulation and analysis
- NumPy — Numerical computations
- Matplotlib — Basic data visualization
- Seaborn — Advanced statistical visualization

```bash

Week2-data-handling-and-visualization/
│── Titanic_Dataset.csv
│── data_handling_visalization_task12.ipynb
│── README.md
│── requirements.txt
```

## Notebook Guidelines

Your notebook should include:

- Proper data loading and initial inspection
- Data cleaning and preprocessing steps
- Clear and meaningful visualizations
- Well-structured code with markdown explanations

## How to Run

1. Open Google Colab
2. Upload the titanic_eda.ipynb file
3. Run each cell sequentially or use “Run All” from the Runtime menu

## Analysis Workflow

- Data loading and initial exploration
- Identifying and handling missing values
- Data cleaning and preprocessing
- Univariate and bivariate analysis
- Visualization of relationships between features
- Extracting insights and conclusions

## Key Insights

- Female passengers had a noticeably higher survival rate compared to males
- Passengers in higher classes were more likely to survive
- Age and family size showed some influence on survival probability
- Higher ticket fares (often linked to higher class) were associated with better survival chances