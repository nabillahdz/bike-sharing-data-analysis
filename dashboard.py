import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import streamlit as st


# Helper function to get max count per season and year
def get_season_year_max(df):
    return df.groupby(["season", "yr"]).agg({"cnt": "max"}).reset_index()

# Helper function to get casual and registered bike rentals per year
def get_rentals_by_year(df):
    return df.groupby(["yr"]).agg({"casual": "sum", "registered": "sum"}).reset_index()

# Helper function to get total rentals per year
def get_total_rentals(df):
    return df.groupby('yr')['cnt'].sum()

# Helper function to get total rentals per hour
def get_hourly_rentals(df):
    return df.groupby('hr')['cnt'].sum()

# Import data
hour_df = pd.read_csv('/Users/nabillahderiszulaeka/Documents/BANGKIT/DICODING/DATA ANALYSIS USING PYTHON/PROYEK ANALISIS DATA/data/hourcleaned_data.csv')
day_df = pd.read_csv('/Users/nabillahderiszulaeka/Documents/BANGKIT/DICODING/DATA ANALYSIS USING PYTHON/PROYEK ANALISIS DATA/data/daycleaned_data.csv')

# Streamlit App Layout
st.title("Bike Rentals Dashboard")
st.sidebar.title("Choose a data visualization")

# Sidebar options for visualization
vis_option = st.sidebar.selectbox(
    'Choose a plot:',
    ['Hourly Season-Year Bar Chart', 'Daily Season-Year Bar Chart', 
     'Hourly Weather Box Plot', 'Daily Weather Box Plot',
     'Stacked Rentals by Year', 'Yearly Rentals', 
     'Temperature vs Rentals', 'Hourly Rentals']
)

# Plotting the selected visualization

if vis_option == 'Hourly Season-Year Bar Chart':
    agg_df = get_season_year_max(hour_df)
    plt.figure(figsize=(10, 6))
    ax = sns.barplot(x='season', y='cnt', hue='yr', data=agg_df)
    plt.title('Number of Users per Season and Year (Using Hourly Data)')
    plt.xlabel('Season')
    plt.ylabel('Number of Users')
    plt.ylim(0, 1200)
    for p in ax.patches:
        ax.annotate(f'{int(p.get_height())}', 
                    (p.get_x() + p.get_width() / 2., p.get_height()), 
                    ha='center', va='bottom', fontsize=10, color='black')
    st.pyplot(plt)

elif vis_option == 'Daily Season-Year Bar Chart':
    agg_df2 = get_season_year_max(day_df)
    plt.figure(figsize=(10, 6))
    ax = sns.barplot(x='season', y='cnt', hue='yr', data=agg_df2)
    plt.title('Number of Users per Season and Year (Using Daily Data)')
    plt.xlabel('Season')
    plt.ylabel('Number of Users')
    plt.ylim(0, 10000)
    for p in ax.patches:
        ax.annotate(f'{int(p.get_height())}', 
                    (p.get_x() + p.get_width() / 2., p.get_height()), 
                    ha='center', va='bottom', fontsize=10, color='black')
    st.pyplot(plt)

elif vis_option == 'Hourly Weather Box Plot':
    plt.figure(figsize=(12, 6))
    plt.subplot(1, 2, 1)
    sns.boxplot(x='weathersit', y='casual', data=hour_df)
    plt.title('Casual Rentals by Weather Situation')
    plt.xlabel('Weather Situation')
    plt.ylabel('Casual Rentals')

    plt.subplot(1, 2, 2)
    sns.boxplot(x='weathersit', y='registered', data=hour_df)
    plt.title('Registered Rentals by Weather Situation')
    plt.xlabel('Weather Situation')
    plt.ylabel('Registered Rentals')

    plt.tight_layout()
    st.pyplot(plt)

elif vis_option == 'Daily Weather Box Plot':
    plt.figure(figsize=(12, 6))
    plt.subplot(1, 2, 1)
    sns.boxplot(x='weathersit', y='casual', data=day_df)
    plt.title('Casual Rentals by Weather Situation')
    plt.xlabel('Weather Situation')
    plt.ylabel('Casual Rentals')

    plt.subplot(1, 2, 2)
    sns.boxplot(x='weathersit', y='registered', data=day_df)
    plt.title('Registered Rentals by Weather Situation')
    plt.xlabel('Weather Situation')
    plt.ylabel('Registered Rentals')

    plt.tight_layout()
    st.pyplot(plt)

elif vis_option == 'Stacked Rentals by Year':
    props_df = get_rentals_by_year(day_df)
    plt.figure(figsize=(10, 6))
    plt.bar(props_df['yr'], props_df['casual'], label='Casual')
    plt.bar(props_df['yr'], props_df['registered'], label='Registered', bottom=props_df['casual'])
    plt.title('Total Bike Rentals by Season and Year')
    plt.xlabel('Season')
    plt.ylabel('Total Rentals')
    plt.legend()
    st.pyplot(plt)

elif vis_option == 'Yearly Rentals':
    yearly_rentals = get_total_rentals(day_df)
    plt.figure(figsize=(8, 4))
    plt.bar(yearly_rentals.index, yearly_rentals.values, color=['pink', 'skyblue'])
    plt.xlabel('Year')
    plt.ylabel('Total Bike Rentals')
    plt.title('Total Bike Rentals by Year')
    st.pyplot(plt)

elif vis_option == 'Temperature vs Rentals':
    plt.scatter(day_df['temp'], day_df['cnt'])
    plt.title('Temperature vs. Total Bike Rentals')
    plt.xlabel('Temperature')
    plt.ylabel('Total Bike Rentals')
    st.pyplot(plt)

elif vis_option == 'Hourly Rentals':
    hourly_rentals = get_hourly_rentals(hour_df)
    plt.figure(figsize=(10, 6))
    plt.bar(hourly_rentals.index, hourly_rentals.values, color='red')
    plt.title('Total Bike Rentals per Hour')
    plt.xlabel('Hour')
    plt.ylabel('Total Bike Rentals')
    st.pyplot(plt)

