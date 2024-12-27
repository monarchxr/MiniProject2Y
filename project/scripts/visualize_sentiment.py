import plotly.express as px
import pandas as pd

# Load the dataset
data = pd.read_csv(r"project\data\labeled.csv")

# Count the occurrences of each sentiment label
sentiment_counts = data['label'].value_counts().reset_index()
sentiment_counts.columns = ['Sentiment', 'Count']  # Rename columns for clarity

# Create a bar chart
fig = px.bar(
    sentiment_counts,
    x='Sentiment', 
    y='Count', 
    title="Sentiment Distribution",
    labels={'Sentiment': 'Sentiment', 'Count': 'Number of Comments'},
    color='Sentiment',
    color_discrete_sequence=px.colors.qualitative.Set2  # Custom color palette
)

# Update layout for better readability
fig.update_layout(
    xaxis_title="Sentiment",
    yaxis_title="Number of Comments",
    title_font_size=20,
    xaxis_tickangle=-45
)

# Display the chart
fig.show()
