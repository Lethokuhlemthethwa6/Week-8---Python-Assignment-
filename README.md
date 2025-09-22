CORD-19 Data Explorer

A beginner-friendly data analysis and visualization project using the CORD-19 metadata dataset.
This project explores research publications related to COVID-19, covering trends over time, top journals, and title word patterns.
The analysis is presented both in Jupyter Notebook/Python scripts and an interactive Streamlit app.

🚀 Project Overview

This project was built as part of a data analysis assignment.
It focuses on:

Loading and exploring real-world data

Cleaning & preparing research metadata

Visualizing key patterns (publication trends, journals, keywords)

Building a simple Streamlit app for interactive exploration

📂 Project Structure
Frameworks_Assignment/
│── metadata.csv        # Dataset (not included in repo, download separately)
│── analysis.ipynb      # Jupyter Notebook with analysis
│── app.py              # Streamlit app
│── README.md           # Documentation

⚙️ Setup Instructions
1. Clone the repo
git clone https://github.com/<your-username>/Frameworks_Assignment.git
cd Frameworks_Assignment

2. Install dependencies
pip install pandas matplotlib seaborn streamlit wordcloud

3. Download dataset

Go to the CORD-19 dataset on Kaggle
.

Download metadata.csv and place it inside the project folder.

📊 Analysis & Findings

Publications by Year

Sharp rise in research papers from 2020 (COVID-19 outbreak).

Top Journals

Certain journals published significantly more COVID-19 research.

Word Patterns in Titles

Common words include COVID-19, SARS-CoV-2, pandemic, outbreak.

Abstract Word Count

Distribution shows variability in abstract length.

Example Visualizations

(Add screenshots here once you generate plots)

📈 Bar chart: Publications by Year

📊 Top Journals

☁️ Word Cloud of Titles

🖥️ Streamlit Application

Run the interactive app:

streamlit run app.py


Features:

Filter publications by year range

View top journals dynamically

Explore sample data tables

Visualize publication trends

📝 Reflection

This project gave me hands-on experience with:

Handling missing data in a real dataset

Performing basic exploratory data analysis (EDA)

Creating visualizations with Matplotlib/Seaborn

Building an interactive dashboard with Streamlit

Challenges

Large dataset size made processing slow → solved by sampling.

Many missing values (journal, abstract) → dropped/cleaned.

Key Takeaways

Real-world data is messy; cleaning is just as important as analysis.

Streamlit makes it easy to share insights interactively.

Even basic analysis can reveal interesting patterns in research trends.

📌 Next Steps (Optional Enhancements)

Add search functionality by author/journal

Include more advanced NLP analysis on abstracts

Deploy Streamlit app on Streamlit Cloud

📜 License

This project is for educational purposes only.