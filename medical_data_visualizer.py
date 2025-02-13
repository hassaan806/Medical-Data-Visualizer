import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("medical_examination.csv")

# Add 'overweight' column (BMI > 25 is overweight)
df['overweight'] = ((df['weight'] / (df['height'] / 100) ** 2) > 25).astype(int)

# Normalize data (0 = good, 1 = bad) for cholesterol and glucose
df['cholesterol'] = (df['cholesterol'] > 1).astype(int)
df['gluc'] = (df['gluc'] > 1).astype(int)

# Draw Categorical plot
def draw_cat_plot():
    df_cat = pd.melt(df, id_vars=["cardio"], 
                     value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])

    # Group and count values
    df_cat = df_cat.groupby(['cardio', 'variable', 'value']).size().reset_index(name="total")

    # Create seaborn categorical plot
    fig = sns.catplot(x="variable", y="total", hue="value", col="cardio", kind="bar", data=df_cat)
    fig.set_axis_labels("Variable", "Total")
    fig = fig.fig  # Convert FacetGrid to Matplotlib figure
    return fig

# Draw Heat Map plot
def draw_heat_map():
    # Clean the data
    df_heat = df[
        (df['ap_lo'] <= df['ap_hi']) &
        (df['height'] >= df['height'].quantile(0.025)) &
        (df['height'] <= df['height'].quantile(0.975)) &
        (df['weight'] >= df['weight'].quantile(0.025)) &
        (df['weight'] <= df['weight'].quantile(0.975))
    ]

    corr = df_heat.corr()

    # Generate a mask for the upper triangle
    mask = np.triu(np.ones_like(corr, dtype=bool))

    # Set up matplotlib figure
    fig, ax = plt.subplots(figsize=(12, 8))

    sns.heatmap(corr, mask=mask, annot=True, fmt=".1f", cmap="coolwarm", vmax=0.3, vmin=-0.1, linewidths=0.5, ax=ax)

    return fig
