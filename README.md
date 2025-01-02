# Sentiment Analysis on Dragon Ball Super: Super Hero Reviews

This project analyzes user reviews of the movie *Dragon Ball Super: Super Hero* to determine the sentiment (Positive, Neutral, or Negative) of each review. The analysis is performed using Python and the TextBlob library.

---

## Table of Contents

1. [Project Overview](#project-overview)
2. [Requirements](#requirements)

---

## Project Overview

The goal of this project is to process reviews from an Excel file, perform sentiment analysis, and save the results in a new file. Sentiment is determined using the TextBlob library, which calculates the polarity of each review:
- **Positive Sentiment**: Polarity > 0
- **Neutral Sentiment**: Polarity = 0
- **Negative Sentiment**: Polarity < 0

---

## Requirements

- Python 3.x
- Libraries: `pandas`, `textblob`, `openpyxl`

Install the dependencies with:
```bash
pip install pandas textblob openpyxl
