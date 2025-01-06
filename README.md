# Sentiment Analysis on Dragon Ball Super: Super Hero Reviews

This project analyzes user reviews of the movie *Dragon Ball Super: Super Hero* to determine the sentiment (Positive, Neutral, or Negative) of each review. The analysis is performed using Python with two different approaches: the TextBlob library and the Hugging Face `transformers` pipeline.

---

## Table of Contents

- [Project Overview](#project-overview)
- [Requirements](#requirements)
- [Usage Instructions](#usage-instructions)

---

## Project Overview

The goal of this project is to process reviews from an Excel file, perform sentiment analysis, and save the results in a new file. Sentiment is determined using two methods:

### **1. TextBlob Library**
- Sentiment is calculated based on polarity:
  - **Positive Sentiment**: Polarity > 0
  - **Neutral Sentiment**: Polarity = 0
  - **Negative Sentiment**: Polarity < 0

### **2. Hugging Face Transformers**
- Sentiment is analyzed using a pre-trained model available on Hugging Face.
- The analysis returns:
  - **Sentiment_Label**: The predicted sentiment (e.g., POSITIVE or NEGATIVE).
  - **Sentiment_Score**: The confidence score for the prediction.

---

## Requirements

### **General Requirements**
- Python 3.x
- Excel file with reviews stored in a specific column (e.g., "Review").

### **Libraries for TextBlob Version**
Install the dependencies with:

pip install pandas textblob openpyxl

### **Libraries for Hugging Face Version**
Install the additional dependencies with:

pip install pandas transformers openpyxl

---

### **Usage Instructions**

1. **Prepare the Input File**  
   Place your Excel file in the `sentimentAnalysis` folder (or update the file path in the script).

2. **Run the TextBlob Script**  
   Use the `sentiment_analysis.py` file to perform sentiment analysis with TextBlob:


   python sentiment_analysis.py
**Output**: `DBSSH_Sentiment_Analysis_Output.xlsx`

### Run the Hugging Face Script  
Use the `sentiment_analysis_hf.py` file to perform sentiment analysis with the Hugging Face `transformers` pipeline:


python sentiment_analysis_hf.py

**Output**: `DBSSH_Sentiment_Analysis_HF_Output_updated.xlsx`

### Analyze the Results  
Both scripts save the results as Excel files with added columns for sentiment labels and scores.

