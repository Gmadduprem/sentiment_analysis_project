import re
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import nltk

from nltk.corpus import stopwords
from textblob import Word
from wordcloud import WordCloud
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


# FILE SETTINGS 


DATA_FILE = "Reviews_demo.csv"

OUTPUT_FILE = "sentiment_analysis_results.csv"

SCORE_CHART = "score_distribution.png"
SENTIMENT_CHART = "sentiment_distribution.png"
WORDCLOUD_FILE = "summary_wordcloud.png"
SCORE_SENTIMENT_CHART = "score_vs_sentiment.png"


# Here,  downloading 'REQUIRED NLTK DATA'

print("Downloading/checking NLTK resources...")

nltk.download("stopwords", quiet=True)
nltk.download("wordnet", quiet=True)
nltk.download("omw-1.4", quiet=True)

print("NLTK resources ready.")


# Here, TEXT PREPROCESSING FUNCTION

def preprocess_text(text, stop_words):

    text = str(text)

    text = text.lower()


    text = re.sub(r"[^\w\s]", "", text)


    words = text.split()


    words = [
        word
        for word in words
        if word not in stop_words
    ]

    # Lemmatize words
    words = [
        Word(word).lemmatize()
        for word in words
    ]


    return " ".join(words)




def main():

    print("\n========================================")
    print("   REVIEW SENTIMENT ANALYSIS")
    print("========================================\n")


    

    print("Loading dataset...")

    try:
        df = pd.read_csv(DATA_FILE)
    except FileNotFoundError:
        print(f"\nERROR: Could not find '{DATA_FILE}'.")
        print("Make sure the CSV file is in the same folder")
        print("as this Python script.")
        return

    print("Dataset loaded successfully.")

    print("\nDataset shape:")
    print(df.shape)


    
    required_columns = ["Text", "Score"]

    for column in required_columns:

        if column not in df.columns:

            print(
                f"\nERROR: Required column '{column}' "
                f"is missing from the dataset."
            )

            print("\nAvailable columns:")
            print(df.columns.tolist())

            return



    df = df.dropna(subset=["Text"]).copy()

    print("\nDataset after removing empty reviews:")
    print(df.shape)


  

    print("\n========================================")
    print("REVIEW SCORE DISTRIBUTION")
    print("========================================")

    score_counts = (
        df["Score"]
        .value_counts()
        .sort_index()
    )

    print(score_counts)



    plt.figure(figsize=(8, 5))

    sns.countplot(
        data=df,
        x="Score"
    )

    plt.title("Distribution of Review Scores")

    plt.xlabel("Review Score")

    plt.ylabel("Number of Reviews")

    plt.tight_layout()

    plt.savefig(
        SCORE_CHART,
        dpi=300
    )

    plt.show()

    

    stop_words = set(
        stopwords.words("english")
    )


    

    negation_words = {
        "not",
        "no",
        "never",
        "neither",
        "nor"
    }

    stop_words = stop_words - negation_words


    
    print("\nCleaning review text...")

    df["CleanText"] = df["Text"].apply(
        lambda text:
        preprocess_text(
            text,
            stop_words
        )
    )

    print("Text cleaning completed.")


    print("\n========================================")
    print("TEXT PREPROCESSING SAMPLE")
    print("========================================")

    for index, row in df.head(5).iterrows():

        print("\nOriginal:")
        print(row["Text"])

        print("\nCleaned:")
        print(row["CleanText"])

        print("-" * 60)


    if "Summary" in df.columns:

        summary_text = (
            df["Summary"]
            .dropna()
            .astype(str)
            .str.cat(sep=" ")
        )

        if summary_text.strip():

            print("\nCreating word cloud...")

            wordcloud = WordCloud(
                width=1200,
                height=700,
                background_color="white"
            ).generate(summary_text)

            plt.figure(
                figsize=(12, 7)
            )

            plt.imshow(
                wordcloud,
                interpolation="bilinear"
            )

            plt.axis("off")

            plt.title(
                "Review Summary Word Cloud"
            )

            plt.tight_layout()

            plt.savefig(
                WORDCLOUD_FILE,
                dpi=300
            )

            plt.show()

    print("\nRunning VADER sentiment analysis...")

    analyzer = SentimentIntensityAnalyzer()


    scores = df["CleanText"].apply(
        analyzer.polarity_scores
    )

    sentiment_scores = pd.DataFrame(
        scores.tolist(),
        index=df.index
    )


    df = pd.concat(
        [
            df,
            sentiment_scores
        ],
        axis=1
    )


    df["Sentiment"] = np.where(
        df["compound"] >= 0.05,
        "Positive",
        np.where(
            df["compound"] <= -0.05,
            "Negative",
            "Neutral"
        )
    )


    print("\n========================================")
    print("SENTIMENT RESULTS")
    print("========================================")

    print(
        df[
            [
                "Score",
                "compound",
                "Sentiment"
            ]
        ].to_string(index=False)
    )


    sentiment_counts = (
        df["Sentiment"]
        .value_counts()
    )

    print("\n========================================")
    print("SENTIMENT COUNTS")
    print("========================================")

    print(sentiment_counts)



    sentiment_percentages = (
        df["Sentiment"]
        .value_counts(
            normalize=True
        )
        * 100
    )

    print("\n========================================")
    print("SENTIMENT PERCENTAGES")
    print("========================================")

    for sentiment, percentage in sentiment_percentages.items():

        print(
            f"{sentiment}: "
            f"{percentage:.2f}%"
        )


  

    plt.figure(figsize=(8, 5))

    sentiment_counts.plot(
        kind="bar",
        rot=0
    )

    plt.title(
        "Sentiment Distribution"
    )

    plt.xlabel(
        "Sentiment"
    )

    plt.ylabel(
        "Number of Reviews"
    )

    plt.tight_layout()

    plt.savefig(
        SENTIMENT_CHART,
        dpi=300
    )

    plt.show()


    

    print("\nCreating score vs sentiment chart...")

    plt.figure(figsize=(10, 6))

    sns.countplot(
        data=df,
        x="Score",
        hue="Sentiment"
    )

    plt.title(
        "Review Score vs Sentiment"
    )

    plt.xlabel(
        "Review Score"
    )

    plt.ylabel(
        "Number of Reviews"
    )

    plt.tight_layout()

    plt.savefig(
        SCORE_SENTIMENT_CHART,
        dpi=300
    )

    plt.show()



    print("\nSaving results...")

    df.to_csv(
        OUTPUT_FILE,
        index=False
    )

    print(
        f"Results saved to: "
        f"{OUTPUT_FILE}"
    )




    print("\n========================================")
    print("FINAL ANALYSIS")
    print("========================================")

    print(
        f"Total reviews: {len(df)}"
    )

    print(
        f"Positive reviews: "
        f"{(df['Sentiment'] == 'Positive').sum()}"
    )

    print(
        f"Neutral reviews: "
        f"{(df['Sentiment'] == 'Neutral').sum()}"
    )

    print(
        f"Negative reviews: "
        f"{(df['Sentiment'] == 'Negative').sum()}"
    )



    print(
        f"\nAverage compound sentiment score: "
        f"{df['compound'].mean():.4f}"
    )


    print(
        f"Average review rating: "
        f"{df['Score'].mean():.2f}"
    )


    print("\n========================================")
    print("ANALYSIS COMPLETED SUCCESSFULLY")
    print("========================================")



if __name__ == "__main__":
    main()