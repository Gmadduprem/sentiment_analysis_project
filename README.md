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

---

### 🧹 Text Preprocessing

Before sentiment analysis, the review text is cleaned and normalized.

The preprocessing pipeline includes:

**1. Convert to Lowercase**

All review text is converted to lowercase to make text processing consistent.

**2. Remove Punctuation**

Special characters and punctuation are removed from the review text.

**3. Tokenization**

The cleaned text is separated into individual words.

**4. Stopword Removal**

Common English stopwords are removed to reduce unnecessary words.

**5. Negation Preservation**

Important negation words are preserved because they can affect sentiment.

The project preserves:

not
no
never
neither
nor

**6. Lemmatization**

Words are converted into their base form using lemmatization.

---

## 🤖 Sentiment Analysis

The project uses VADER Sentiment Analysis to calculate sentiment scores.

**VADER generates:**

negative score
neutral score
positive score
compound score

The compound score is used to determine the final sentiment category.

Sentiment Classification Rules
Compound Score	Sentiment
>= 0.05	Positive
<= -0.05	Negative
Between -0.05 and 0.05	Neutral

---

## 📊 Analysis Results

The project analyzed:

Total Reviews: 20
Review Score Distribution
Review Score	Number of Reviews
1	4
2	4
3	2
4	4
5	6
Total	20
Average Review Rating
3.20 / 5

The most common review rating in the dataset is:

5 stars

with 6 reviews.

---

## 😊 Sentiment Distribution

The sentiment analysis produced the following results:

Sentiment	Number of Reviews	Percentage
Positive	12	60%
Negative	8	40%
Neutral	0	0%
Total	20	100%
Average Compound Sentiment Score
0.2432

The dataset contains more positive reviews than negative reviews.

---

## ⭐ Review Score vs Sentiment

The relationship between review score and sentiment is summarized below:

Review Score	Negative	Positive
1	4	0
2	3	1
3	1	1
4	0	4
5	0	6
Observations
All 1-star reviews were classified as Negative.
Most 2-star reviews were classified as Negative.
3-star reviews were divided between Positive and Negative.
All 4-star reviews were classified as Positive.
All 5-star reviews were classified as Positive.

This indicates a strong relationship between numerical review ratings and detected textual sentiment within this dataset.

---

## ☁️ Review Summary Word Cloud

The project generates a word cloud from the Summary column.

The word cloud highlights frequently occurring terms in the review summaries.

Some prominent terms include:

Excellent
Product
Good
Recommended
Quality
Experience
Value
Great
Poor
Terrible
Better
Worth
Fantastic
Perfect
Disappointed
Satisfied

The word cloud provides a visual representation of frequently used vocabulary in the review summaries.

---

## 📈 Visualizations

The project generates four main visualization files.

1. Review Score Distribution
score_distribution.png

Displays the number of reviews associated with each review score from 1 to 5.

2. Sentiment Distribution
sentiment_distribution.png

Displays the number of Positive, Negative, and Neutral reviews.

3. Review Score vs Sentiment
score_vs_sentiment.png

Shows the relationship between numerical review scores and sentiment classifications.

4. Review Summary Word Cloud
summary_wordcloud.png

Displays frequently occurring words from review summaries.

---

## 📁 Project Structure


review-sentiment-analysis/
│
├── sentiment_analysis.py
├── Reviews_demo.csv
├── requirements.txt
│
├── sentiment_analysis_results.csv
│
├── score_distribution.png
├── sentiment_distribution.png
├── score_vs_sentiment.png
├── summary_wordcloud.png
│
└── README.md

---

## ⚙️ Installation

Prerequisites

Make sure Python 3.x is installed on your system.

Check the Python version:

python --version

or:

python3 --version

---

## 📦 Install Dependencies

Clone the repository:

git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY.git

Navigate to the project directory:

cd YOUR-REPOSITORY

Install the required Python packages:

pip install -r requirements.txt

---

## ▶️ How to Run

Make sure the following files are available in the project directory:

sentiment_analysis.py
Reviews_demo.csv
requirements.txt

Run the Python script:

python sentiment_analysis.py

The program will:

Load the review dataset.
Validate the required columns.
Remove missing review text.
Clean the review text.
Perform text preprocessing.
Run VADER sentiment analysis.
Classify the reviews.
Calculate sentiment statistics.
Generate visualizations.
Save the final analysis results.

---

## 📤 Output

After successful execution, the following files are generated:

sentiment_analysis_results.csv
score_distribution.png
sentiment_distribution.png
score_vs_sentiment.png
summary_wordcloud.png
Sentiment Analysis Output

The generated CSV contains the original dataset information together with additional analytical fields such as:

CleanText
neg
neu
pos
compound
Sentiment

--- 

## 🔍 Key Findings

Based on the analyzed dataset:

20 reviews were analyzed.
The average review rating was 3.20/5.
12 reviews (60%) were classified as Positive.
8 reviews (40%) were classified as Negative.
0 reviews were classified as Neutral.
The average VADER compound score was 0.2432.
Rating 5 was the most frequent review score.
All 1-star reviews were classified as Negative.
All 4-star and 5-star reviews were classified as Positive.
The dataset shows a noticeable relationship between numerical ratings and textual sentiment.

---

## 💡 Applications

This type of sentiment-analysis system can be applied to:

Customer feedback analysis
Product review analysis
E-commerce review monitoring
Customer satisfaction analysis
Product quality evaluation
Brand feedback analysis
Market research
Review classification
Opinion mining
Business intelligence

---

## 🚀 Future Improvements

The current project can be extended with the following features:

Support for larger datasets.
Interactive dashboards.
Product-level sentiment analysis.
Review helpfulness analysis.
Sentiment trends over time.
Comparison of multiple sentiment-analysis techniques.
Advanced NLP models.
Transformer-based sentiment classification.
Automated report generation.
Interactive filtering and visualization.
Unit testing and automated testing.
Command-line configuration for input and output files.

These are proposed enhancements and are not part of the current implementation.

---

## 🧠 Skills Demonstrated

This project demonstrates practical knowledge of:

Python Programming
Natural Language Processing
Text Preprocessing
Sentiment Analysis
VADER
Pandas
NumPy
NLTK
TextBlob
Matplotlib
Seaborn
WordCloud
CSV Data Processing
Data Visualization
Statistical Analysis
File Handling
Exception Handling

---

## 🔑 Keywords


Python
Natural Language Processing
NLP
Sentiment Analysis
VADER
VADER Sentiment
Text Analysis
Text Preprocessing
Customer Reviews
Product Reviews
Review Analysis
Data Analysis
Data Science
Data Visualization
Pandas
NumPy
NLTK
TextBlob
Matplotlib
Seaborn
WordCloud
Opinion Mining
Customer Feedback
