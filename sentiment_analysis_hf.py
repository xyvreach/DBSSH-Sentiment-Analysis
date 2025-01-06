# Authored by Hector J. Rodriguez M.

import pandas as pd
from transformers import pipeline

# 1) Load the spreadsheet
file_path = 'sentimentAnalysis/DBSSH_reviews.xlsx'  # Replace with your file name
data = pd.ExcelFile(file_path)

# 2) Parse the sheet
sheet_data = data.parse('Sheet1')  # Adjust the sheet name if necessary

# 3) Initialize the Hugging Face sentiment analysis pipeline
sentiment_analyzer = pipeline("sentiment-analysis")

# 4) Define a function to analyze sentiment using the pipeline
def analyze_sentiment(review_text):
    """
    Takes in a review string and returns the predicted label 
    and confidence score from the sentiment analysis pipeline.
    """
    # The pipeline returns a list of results; grab the first (and only) result
    result = sentiment_analyzer(review_text)[0]
    return {
        "Sentiment_Label": result["label"],
        "Sentiment_Score": result["score"]
    }

# 5) Apply the sentiment analysis to each review and store results
analysis_results = sheet_data['Review'].apply(analyze_sentiment)

# 6) Extract the sentiment label and score into separate columns
sheet_data['Sentiment_Label'] = analysis_results.apply(lambda x: x['Sentiment_Label'])
sheet_data['Sentiment_Score'] = analysis_results.apply(lambda x: x['Sentiment_Score'])

# 7) Save the results to a new Excel file
output_file = 'DBSSH_Sentiment_Analysis_HF_Output_updated.xlsx'
sheet_data.to_excel(output_file, index=False)

print(f"Sentiment analysis complete! Results saved to '{output_file}'")
