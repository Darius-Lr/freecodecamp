import matplotlib
matplotlib.use("Agg")
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress


def draw_plot():
    # Read data from file
    df=pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.figure(figsize=(20, 6))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], label='original data')

    # Create first line of best fit
    slope, intercept, r, p, se = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    x_line = np.arange(df['Year'].min(), 2051)
    plt.plot(x_line, intercept + slope * x_line, color='r')


    # Create second line of best fit
    df_adjusted = df[df['Year'] >= 2000]
    slope2, intercept2, r2, p2, se2 = linregress(df_adjusted['Year'], df_adjusted['CSIRO Adjusted Sea Level'])
    x_line2 = np.arange(2000, 2051)
    plt.plot(x_line2, intercept2 + slope2 * x_line2, color='g', label='Fitted line (2000+)')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()