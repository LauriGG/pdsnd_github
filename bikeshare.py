import pandas as pd

# City data files
CITY_DATA = {
    'chicago': 'chicago.csv',
    'new york': 'new_york_city.csv',
    'washington': 'washington.csv'
}

MONTHS = ['january', 'february', 'march', 'april', 'may', 'june']
DAYS = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

def get_city():
    """
    Asks the user to input a city and then validates the input.

    Returns:
        str: The chosen city.
    """
    while True:
        city = input('Would you like to see data for Chicago, New York, or Washington? ').lower()
        if city in CITY_DATA:
            return city
        else:
            print('Invalid input! Please enter a valid city.')

def get_filter():
    """
    Asks the user to input a filter type and validates the input.

    Returns:
        str: The chosen filter type.
    """
    while True:
        filter_type = input('Would you like to filter the data by month, day, or not at all? ').lower()
        if filter_type in ['month', 'day', 'none']:
            return filter_type
        else:
            print('Invalid input! Please enter a valid filter type.')

# This method returns the chosen month
def get_month():
    """
    Asks the user to input a month and validates the input.

    Returns:
        str: The chosen month.
    """
    while True:
        month = input('Which month - January, February, March, April, May, or June? ').lower()
        if month in MONTHS:
            return month
        else:
            print('Invalid input! Please enter a valid month.')

# This method returns the chosen day
def get_day():
    """
    Asks the user to input a day and validates the input.

    Returns:
        str: The chosen day.
    """
    while True:
        day = input('Which day - Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday? ').lower()
        if day in DAYS:
            return day
        else:
            print('Invalid input! Please enter a valid day.')
            
# This method loads a CSV file based on the chosen city
def load_data(city, month, day):
    """
    Loads the data from a CSV file based on the chosen city and applies filters based on the chosen month and day.

    Args:
        city (str): The chosen city.
        month (str): The chosen month.
        day (str): The chosen day.

    Returns:
        pd.DataFrame: The loaded and filtered data as a pandas DataFrame.
    """
    filename = CITY_DATA[city]
    df = pd.read_csv(filename)
    
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['Month'] = df['Start Time'].dt.month_name().str.lower()
    df['Day of Week'] = df['Start Time'].dt.day_name().str.lower()
    
    if month:
        df = df[df['Month'] == month]
    
    if day:
        df = df[df['Day of Week'] == day]
    
    return df

def display_data(df):
    """
    Displays rows of raw data to the user.

    Args:
        df (pd.DataFrame): The data to display.
    """
    start_idx = 0
    while True:
        display = input('Would you like to see 5 rows of raw data? Enter "yes" or "no": ').lower()
        if display == 'yes':
            print(df.iloc[start_idx:start_idx+5])
            start_idx += 5
        elif display == 'no':
            break
        else:
            print('Invalid input! Please enter either "yes" or "no".')
    
    print('-' * 40)

def calculate_stats(df):
    """
    Calculates and displays various statistics based on the provided data.

    Args:
        df (pd.DataFrame): The data to calculate statistics on.
    """
    print('Calculating the most frequent times of travel...\n')
    
    common_month = df['Month'].mode()[0]
    print('Most Common Month:', common_month)
    
    common_day = df['Day of Week'].mode()[0]
    print('Most Common Day of Week:', common_day)
    
    common_hour = df['Start Time'].dt.hour.mode()[0]
    print('Most Common Start Hour:', common_hour)
    
    print('-' * 40)

    print('Calculating the most popular stations and trip...\n')
    
    common_start_station = df['Start Station'].mode()[0]
    print('Most Commonly Used Start Station:', common_start_station)
    
    common_end_station = df['End Station'].mode()[0]
    print('Most Commonly Used End Station:', common_end_station)
    
    df['Trip'] = df['Start Station'] + ' to ' + df['End Station']
    common_trip = df['Trip'].mode()[0]
    print('Most Frequent Trip:', common_trip)
    
    print('-' * 40)

    print('Calculating trip duration...\n')
    
    total_duration = df['Trip Duration'].sum()
    print('Total Travel Time:', total_duration)
    
    mean_duration = df['Trip Duration'].mean()
    print('Mean Travel Time:', mean_duration)
    
    print('-' * 40)

    print('Calculating user stats...\n')
    
    user_counts = df['User Type'].value_counts()
    print('Counts of User Types:\n', user_counts)
    
    if 'Gender' in df:
        gender_counts = df['Gender'].value_counts()
        print('\nCounts of Gender:\n', gender_counts)
    else:
        print('\nGender information not available for this city.')
    
    if 'Birth Year' in df:
        earliest_birth_year = df['Birth Year'].min()
        print('\nEarliest Birth Year:', earliest_birth_year)
        
        recent_birth_year = df['Birth Year'].max()
        print('Most Recent Birth Year:', recent_birth_year)
        
        common_birth_year = df['Birth Year'].mode()[0]
        print('Most Common Birth Year:', common_birth_year)
    else:
        print('\nBirth year information not available for this city.')
    
    print('-' * 40)

def main():
    """
    The main function that runs the program.
    """
    while True:
        city = get_city()
        filter_type = get_filter()
        
        month = None
        day = None
        
        if filter_type == 'month':
            month = get_month()
        elif filter_type == 'day':
            day = get_day()
        
        df = load_data(city, month, day)
        display_data(df)
        calculate_stats(df)
        
        restart = input('Would you like to restart? Enter "yes" or "no": ').lower()
        if restart != 'yes':
            break

if __name__ == "__main__":
    main()
