import pandas as pd
import statsmodels.api as sm
from statsmodels.formula.api import ols
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
import matplotlib.pyplot as plt
import numpy as np

# Step 1: Load Quantitative Data (Survey Results)
def load_survey_data(file_path):
    """
    Load survey data from a CSV file.
    """
    return pd.read_csv(file_path)

# Step 2: Perform Quantitative Analysis
def quantitative_analysis(data):
    """
    Perform regression analysis to test hypotheses.
    """
    if len(data) < 20:
        print("Warning: Sample size is less than 20. Results may not be reliable.")
    
    # Example: Regression for H1 (Engagement)
    model = ols('work_engagement ~ viva_usage + performance_transparency + digital_literacy', data=data).fit()
    print(model.summary())
    
    # Example: Mediation/Moderation Analysis
    # (You can use PROCESS macro or Python libraries like Pingouin for advanced mediation analysis)
    return model

# Step 3: Load Qualitative Data (Interview Transcripts)
def load_interview_data(file_path):
    """
    Load interview data from a text file or database.
    """
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        return None

# Step 4: Perform Qualitative Analysis
def qualitative_analysis(interview_text):
    """
    Perform sentiment analysis and thematic analysis on interview data.
    """
    nltk.download('vader_lexicon')
    sia = SentimentIntensityAnalyzer()
    sentiment = sia.polarity_scores(interview_text)
    print("Sentiment Analysis:", sentiment)
    
    # Example: Extract themes (manual coding or NLP-based topic modeling can be added here)
    # For simplicity, this example only performs sentiment analysis.
    return sentiment

# Step 5: Visualize Results
def visualize_results(data):
    """
    Create visualizations for survey results.
    """
    plt.scatter(data['viva_usage'], data['work_engagement'], label='Data Points')
    # 添加回归线
    x = data['viva_usage']
    y = data['work_engagement']
    m, b = np.polyfit(x, y, 1)
    plt.plot(x, m*x + b, color='red', label='Regression Line')
    plt.xlabel('Viva Usage')
    plt.ylabel('Work Engagement')
    plt.title('Viva Usage vs Work Engagement')
    plt.legend()
    plt.show()

# Main Function
if __name__ == "__main__":
    # Load survey data
    survey_data = load_survey_data('survey_results.csv')
    
    # Perform quantitative analysis
    quantitative_model = quantitative_analysis(survey_data)
    
    # Load interview data
    interview_text = load_interview_data('interview_transcripts.txt')
    
    # Perform qualitative analysis
    qualitative_results = qualitative_analysis(interview_text)
    
    # Visualize results
    visualize_results(survey_data)