import pandas as pd
from textblob import TextBlob

# Load the spreadsheet
file_path = 'sentimentAnalysis/DBSSH_reviews.xlsx'  # Replace with your file name
data = pd.ExcelFile(file_path)

# Parse Sheet1
sheet_data = data.parse('Sheet1')  # Adjust the sheet name if necessary

# Perform sentiment analysis
sheet_data['Sentiment_Polarity'] = sheet_data['Review'].apply(lambda x: TextBlob(x).sentiment.polarity)
sheet_data['Sentiment_Label'] = sheet_data['Sentiment_Polarity'].apply(
    lambda polarity: 'Positive' if polarity > 0 else ('Negative' if polarity < 0 else 'Neutral')
)

# Save the results to a new Excel file
sheet_data.to_excel('DBSSH_Sentiment_Analysis_Output.xlsx', index=False)

print("Sentiment analysis complete! Results saved to 'Sentiment_Analysis_Output.xlsx'")
