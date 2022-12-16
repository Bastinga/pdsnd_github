import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input("Select a city from {}, {} or {}:".format(*CITY_DATA.keys())).strip().lower()
        if city in CITY_DATA.keys():
            break
            
    # TO DO: get user input for month (all, january, february, ... , june)
    month = input("Enter the month you want to analyse (all, january, february, ... , june): ")

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input("Enter the day you want to analyse: ")

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june','july', 'august','september','ocotber','november','december']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['Start Time'].dt.month == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday','sunday']
        day = days.index(day) + 1
        df = df[df['Start Time'].dt.day == day]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    df['month'] = df['Start Time'].dt.month
    popular_month = df['month'].mode()[0]

    # TO DO: display the most common day of week
    df['day'] = df['Start Time'].dt.day
    popular_day = df['day'].mode()[0]

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]

    print('Most Popular Start Month:', popular_month)
    print('Most Popular Start Day:', popular_day)
    print('Most Popular Start Hour:', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    
    Starting_place = df['Start Station'].value_counts()
    print('Most Popular Start Station: ', Starting_place)
    # TO DO: display most commonly used end station
    End_place = df['End Station'].value_counts()
    print('Most Popular End Station: ', End_place)

    # TO DO: display most frequent combination of start station and end station trip

    combined = df[['Start Station','End Station']].value_counts()
    print('Most Popular Start and End Station: ', combined)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    travel_time = df['Trip Duration'].sum()
    travel_time_h = travel_time / 3600
    travel_time_day= travel_time_h / 24
    print('Total travel time in days: ', travel_time_day)
    # TO DO: display mean travel time
    travel_time_avg_sec = df['Trip Duration'].mean()
    travel_time_avg_min = travel_time_avg_sec / 60
    print('Average time of travel in minutes: ', travel_time_avg_min)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    User_typ = df['User Type'].value_counts()
    print('Count of user types: ', User_typ)

    # TO DO: Display counts of gender
    gender = df['Gender'].value_counts()
    print('Count of gender: ', gender)

    # TO DO: Display earliest, most recent, and most common year of birth
    birth_min = df['Birth Year'].min()
    print('Most recent of gender: ', birth_min)
    birth_max = df['Birth Year'].max()
    print('Most recent of gender: ', birth_max)
    common = df['Birth Year'].value_counts().index[0]
    print('Most recent of gender: ', common)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
