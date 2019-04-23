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
        city = input('\nWould you like to see data for Chicago,New York city, or Washington?\n')
        if city.lower() == 'chicago' or city.lower() == 'new york city' or city.lower() == 'washington':
            break
        

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input('\nPlease choose name of the month to filter by(january, february, ... , june), or "all" to apply no month filter\n')
        if month.lower() == 'january' or month.lower() == 'february' or month.lower() == 'march' or month.lower() == 'april' or month.lower() =='may'\
        or month.lower() == 'june' or month.lower() == 'all':        
            break
    
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input('\nPlease choose name of the day of week to filter by, or "all" to apply no day filter\n')
        if day.lower() == 'monday' or day.lower() == 'tuesday' or day.lower() == 'wednesday' or day.lower() == 'thursday' or day.lower() =='friday'\
        or day.lower() == 'saturday' or day.lower() == 'sunday' or day.lower() == 'all':        
            break
    print('-'*40)
    return city.lower(), month.lower(), day.lower()





def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - pandas DataFrame containing city data filtered by month and day
    """
    
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name


    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
    
        # filter by month to create the new dataframe
        df = df[df['month'] == month] 
        # 相当于一步筛选
    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
    
    return df
    


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month    
    popular_month = df['month'].mode()[0]    
    print('The most common month:', popular_month)

    # TO DO: display the most common day of week
    popular_weekday = df['day_of_week'].mode()[0]    
    print('The most common day of week:', popular_weekday)

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('The most common start hour:', popular_hour)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    
    popular_start_station = df['Start Station'].mode()[0]
    print('The most commonly used start station:', popular_start_station)

    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print('The most commonly used end station:', popular_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    df['trip'] = df['Start Station'] + ' -> ' + df['End Station']
    popular_trip = df['trip'].mode()[0]
    print('The most popular trip:', popular_trip)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('Total travel time:',total_travel_time)

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('Mean_travel_time:',mean_travel_time)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    counts_of_user_types = df['User Type'].value_counts()
    print('Counts of user type:', counts_of_user_types)

    # TO DO: Display counts of gender
    while True:
        try:
            counts_of_gender = df['Gender'].value_counts()
            print('Counts of gender:', counts_of_gender)
            break
        except:
            print("no data about 'Gender'")
            break

    # TO DO: Display earliest, most recent, and most common year of birth
    while True:
        try:        
            earliest_year_of_birth = df['Birth Year'].min()
            most_recent_year_of_birth = df['Birth Year'].max()
            most_common_year_of_birth = df['Birth Year'].mode()[0]
            print('The earliest year of birth:', earliest_year_of_birth)
            print('The most recent year of birth:', most_recent_year_of_birth)
            print('The most common year of birth:', most_common_year_of_birth)
            break
        except:
            print("no data about 'Birth Year'")
            break
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
