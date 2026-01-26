# Real-vs-Fake-news-analysis
Exploratory data analysis of real vs fake news articles using Python

# Real vs Fake News Analysis

## Overview
This project explores structural and linguistic differences between real and fake news articles using Python-based exploratory data analysis. The goal is to identify interpretable patterns related to misinformation and information integrity that may support future machine learning approaches.

The analysis focuses on article length, word count, and subject distribution across labeled real and fake news datasets.

---

## Dataset
- **Source:** Fake and Real News Dataset (Kaggle)
- **Size:** 44,898 news articles
  - 23,481 FAKE articles
  - 21,417 REAL articles
- **Fields:** title, text, subject, date, label
- **Data Quality:** No missing values in key columns

The dataset is relatively balanced between classes, making it suitable for exploratory analysis and downstream machine learning tasks.

---

## Tools & Technologies
- Python
- pandas
- matplotlib
- seaborn
- Jupyter Notebook

---

## Future Work
- Apply NLP techniques (TF-IDF, n-grams) to textual data
- Train and evaluate machine learning classifiers for fake news detection
- Extend analysis to other forms of synthetic media (e.g., audio deepfakes)
