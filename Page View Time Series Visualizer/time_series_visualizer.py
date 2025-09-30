import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv',index_col="date"
                 ,parse_dates=True)

# Clean data
low_views=df['value'].quantile(0.025)
high_views=df['value'].quantile(0.975)
df = df[(df['value']>low_views) & (df['value']<high_views)]



def draw_line_plot():
    # Draw line plot
    plt.figure(figsize=(10, 5))
    x = df.index
    y = df['value']
    plt.plot(x, y)
    plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    plt.xlabel('Date')
    plt.ylabel('Page Views')

    fig = plt.gcf()

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    plt.figure(figsize=(10, 5))
    df = pd.read_csv('fcc-forum-pageviews.csv', index_col="date")
    months = []
    years = []
    for x in df.index:
        parts = x.split('-')
        months.append(parts[1])
        years.append(parts[0])
    data = {
        "years": years,
        "months": months,
        "value": df['value'].values
    }
    df_bar = pd.DataFrame(data)
    df_bar['average'] = df_bar.groupby(['years', 'months'])['value'].transform('mean')
    df_grouped = df_bar.groupby(['years', 'months'])['value'].mean().unstack()

    # Draw bar plot

    fig = df_grouped.plot(kind='bar').figure
    month_names = [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ]
    plt.legend(title="Months", labels=month_names)
    plt.xlabel("Years")
    plt.ylabel("Average Page Views")



    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    plt.figure(figsize=(10, 5))
    df = pd.read_csv('fcc-forum-pageviews.csv', index_col="date"
                     , parse_dates=True)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)

    plt.subplot(1,2,1)
    sns.boxplot(data=df_box, x="year", y="value")
    plt.title('Year-wise Box Plot (Trend)')
    plt.xlabel("Year")
    plt.ylabel("Page Views")
    plt.yticks(range(0, 210000, 20000))
    plt.subplot(1,2,2)
    sns.boxplot(data=df_box, x="month", y="value",
                order=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
    plt.title('Month-wise Box Plot (Seasonality)')
    plt.xlabel("Month")
    plt.ylabel("Page Views")
    plt.yticks(range(0, 210000, 20000))
    fig = plt.gcf()


    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
