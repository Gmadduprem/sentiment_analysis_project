# Review Sentiment Analysis Using VADER and NLP

A Python-based Natural Language Processing (NLP) project for analyzing product reviews, preprocessing review text, classifying customer sentiment using VADER, and generating statistical visualizations.

![Python](https://img.shields.io/badge/Python-3.x-blue)
![NLP](https://img.shields.io/badge/NLP-Sentiment%20Analysis-green)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-orange)
![VADER](https://img.shields.io/badge/VADER-Sentiment-purple)

---

## 📌 Overview

**Review Sentiment Analysis Using VADER and NLP** is a Python-based Natural Language Processing project designed to analyze customer product reviews and identify their overall sentiment.

The project processes review data stored in a CSV file and performs text preprocessing, sentiment analysis, statistical analysis, and visualization.

The system classifies reviews into three possible sentiment categories:

- Positive
- Negative
- Neutral

The project uses **VADER (Valence Aware Dictionary and sEntiment Reasoner)** for sentiment analysis and generates multiple visualizations to understand review ratings, sentiment distribution, and the relationship between numerical ratings and textual sentiment.

---

## 🎯 Project Objectives

The main objectives of this project are:

- Analyze customer product reviews.
- Clean and preprocess review text.
- Remove unnecessary stopwords.
- Preserve important negation words.
- Apply word lemmatization.
- Perform sentiment analysis using VADER.
- Classify reviews as Positive, Negative, or Neutral.
- Analyze the distribution of review scores.
- Compare review scores with sentiment classifications.
- Generate a word cloud from review summaries.
- Export the complete analysis results into a CSV file.

---

## ✨ Features

### Data Processing

- CSV dataset loading
- Dataset shape inspection
- Required-column validation
- Missing review removal
- Automated result generation

### Text Preprocessing

- Convert text to lowercase
- Remove punctuation
- Tokenize review text
- Remove English stopwords
- Preserve important negation words
- Lemmatize words

### Sentiment Analysis

- VADER sentiment analysis
- Compound sentiment score calculation
- Positive sentiment classification
- Negative sentiment classification
- Neutral sentiment classification
- Sentiment percentage calculation

### Data Visualization

The project generates:

1. Review Score Distribution
2. Sentiment Distribution
3. Review Score vs Sentiment
4. Review Summary Word Cloud

---

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| NumPy | Numerical operations |
| Pandas | Data processing and analysis |
| Matplotlib | Data visualization |
| Seaborn | Statistical visualization |
| NLTK | Natural Language Processing |
| TextBlob | Word processing and lemmatization |
| VADER Sentiment | Sentiment analysis |
| WordCloud | Review-summary visualization |

---

## 📚 Python Libraries

The project uses the following dependencies:

```text
numpy
pandas
matplotlib
seaborn
nltk
textblob
wordcloud
vaderSentiment
```

---

## 📂 Dataset

The project uses a CSV dataset named:

```text
Reviews_demo.csv
```
---

## 🔄 Project Workflow


                    Reviews_demo.csv
                           |
                           v
                   Load Dataset
                           |
                           v
                  Validate Columns
                           |
                           v
                Remove Missing Reviews
                           |
                           v
                 Text Preprocessing
                           |
          +----------------+----------------+
          |                |                |
          v                v                v
      Lowercase      Stopword Removal   Punctuation
          |                |                |
          +----------------+----------------+
                           |
                           v
                     Lemmatization
                           |
                           v
                  Clean Review Text
                           |
                           v
                 VADER Sentiment
                      Analysis
                           |
                           v
                 Compound Score
                           |
                           v
              Sentiment Classification
                           |
             +-------------+-------------+
             |             |             |
             v             v             v
          Positive      Negative      Neutral
             |             |             |
             +-------------+-------------+
                           |
                           v
                  Statistical Analysis
                           |
             +-------------+-------------+
             |             |             |
             v             v             v
        Score Chart  Sentiment Chart  Word Cloud
                           |
                           v
                 Score vs Sentiment
                           |
                           v
            sentiment_analysis_results.csv

