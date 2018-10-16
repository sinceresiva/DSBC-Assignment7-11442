import pandas as pd
import numpy as np
df=pd.read_csv('titanic.csv')
grouped_df = df.groupby(['sex']).size().reset_index(name='count')

import matplotlib.pyplot as plt 

# Create a list of colors 
colors = ["#E13F29", "#00AA80"]

# Create a pie chart
plt.pie(
    # using data total)arrests
    grouped_df['count'],
    # with the labels being officer names
    labels=grouped_df['sex'],
    # with no shadows
    shadow=False,
    # with colors
    colors=colors,
    # with the start angle at 90%
    startangle=90,
    # with one slide exploded out
    explode=(0,0.15),
    # with the percent listed as a fraction
    autopct='%1.1f%%'
)

# View the plot drop above
plt.axis('equal')

# View the plot
plt.tight_layout()
plt.show()
