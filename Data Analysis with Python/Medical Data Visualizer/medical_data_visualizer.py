import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np


# 1
df = pd.read_csv("medical_examination.csv")

# 2
df["BMI"] = df["weight"] / ((df["height"] / 100) ** 2)
df["overweight"] = df["BMI"].apply(lambda x: 1 if x > 25 else 0)
df.drop('BMI', axis=1, inplace=True)

# 3
df['cholesterol'] = df['cholesterol'].apply(lambda x: 1 if x > 1 else 0)
df['gluc'] = df['gluc'].apply(lambda x: 1 if x > 1 else 0)


# 4
def draw_cat_plot():
    # 5
    df_cat = pd.melt(df, id_vars=['cardio'],
                     value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])

    # 6

    df_cat = (
        df_cat
        .groupby(['cardio', 'variable', 'value'])
        .size()
        .reset_index(name='total')
    )

    # 7

    g = sns.catplot(data=df_cat, x='variable', y='total', hue='value', col='cardio', kind='bar')

    # 8
    fig = g.fig

    # 9
    fig.savefig('catplot.png')
    return fig


# 10
def draw_heat_map():
    # 11
    height_low = df['height'].quantile(0.025)
    height_high = df['height'].quantile(0.975)
    weight_low = df['weight'].quantile(0.025)
    weight_high = df['weight'].quantile(0.975)
    df_heat = df[
        (df['ap_lo'] < df['ap_hi']) &
        (df['height'].between(height_low, height_high)) &
        (df['weight'].between(weight_low, weight_high))
        ]
    # 12
    corr = df_heat.corr()

    # 13
    mask = np.triu(np.ones_like(corr, dtype=bool))

    # 14
    fig, ax = plt.subplots(figsize=(12, 12))

    # 15

    sns.heatmap(corr, mask=mask, annot=True, fmt=".1f", cmap="crest")

    # 16
    fig.savefig('heatmap.png')
    return fig
