import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data-add file path 'FileNotFoundError' 
df = pd.read_csv("medical_examination.csv")

# Add 'overweight' column
df['overweight'] = np.where((df['weight']/(df['height']**2) * 10000)>25, 1, 0)

# Normalize data by making 0 always good and 1 always bad. If the value of 'cholesterol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.
df[['cholesterol', 'gluc']] = np.where((df[['cholesterol', 'gluc']]<= 1), 0,1)  

# Draw Categorical Plot
def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
    df_cat = pd.melt(df, value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])


    # Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the columns for the catplot to work correctly.
    df_cat = df.melt(id_vars=['cardio'], value_vars=['alco', 'active', 'cholesterol', 'gluc', 'smoke', 'overweight']).value_counts().to_frame(name='total').sort_values('variable', ascending=True).reset_index()
    

    # Draw the catplot with 'sns.catplot()'
    sns.catplot(data=df_cat, x='variable', y='total',hue='value', kind='bar', col='cardio')
    plt.close() #stops plot outputting twice

    # Get the figure for the output
    fig = sns.catplot(data=df_cat, x='variable', y='total',hue='value', kind='bar', col='cardio').fig
    plt.close() #stops plot outputting twice

    # Do not modify the next two lines
    fig.savefig('catplot.png')
    return fig


# Draw Heat Map
def draw_heat_map():
    # Clean the data
    df_heat = df.loc[(df['ap_lo'] <= df['ap_hi']) & (df['height'] >= df['height'].quantile(0.025)) & (df['height'] <= df['height'].quantile(0.975)) & 
                (df['weight'] >= df['weight'].quantile(0.025)) & (df['weight'] <= df['weight'].quantile(0.975))]

    # Calculate the correlation matrix
    corr = df_heat.corr()

    # Generate a mask for the upper triangle
    mask = np.triu(np.ones_like(corr)) 



    # Set up the matplotlib figure
    fig, ax = plt.subplots(figsize = (11,9)) 

    # Draw the heatmap with 'sns.heatmap()'
    sns.heatmap(corr, mask=mask, linewidths=0.5, linecolor="white", annot=True, fmt='.1f', vmin= -0.14, center=0.00, vmax=0.30, 
            cbar_kws={"shrink": 0.5,"ticks":[-0.08, 0.00, 0.08, 0.16, 0.24]})

    plt.close() #stops plot outputting twice


    # Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig
