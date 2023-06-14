import bikes #importing bikes.py module


def main(): #main function

    while True: #infinite loop to keep the program running until user exits with input 0

        #print menu
        input_command = int(input('''
        0. Exit
        1. Distance sum for user
        2. Average speed for user
        3. Duration sum for each city for a day
        4. User amount for a city
        5. Daily trip amount for a city
        6. Most popular station and number of trips for a city

        Give a number to choose a command: '''))

        print()
        
        #if conditions to check the input and call the function to fetch data from the database
        if input_command == 0:
            break
        elif input_command == 1:
            user = input('Enter user (example: "user555"): ')
            print()
            print(f'Distance sum for {user}: {bikes.distance_of_user(user)}')
        elif input_command == 2:
            user = input('Enter user (example: "user555"): ')
            print()
            print(f'Average speed for {user}: {bikes.speed_of_user(user)}')
        elif input_command == 3:
            day = input('Enter day (example: "2021-06-15"): ')
            print()
            print(f'Duration sum for each city for {day}: {bikes.duration_in_each_city(day)}')
        elif input_command == 4:
            city = input('Enter city (example: "city7"): ')
            print()
            print(f'User amount for {city}: {bikes.users_in_city(city)}')
        elif input_command == 5:
            city = input('Enter city (example: "city7"): ')
            print()
            print(f'Daily trip amount for {city}: {bikes.trips_on_each_day(city)}')
        elif input_command == 6:
            city = input('Enter city (example: "city7"): ')
            print()
            print(f'Most popular station and number of trips for {city}: {bikes.most_popular_start(city)}')



if __name__ == "__main__":
    main() #calling main function
    print('Program ended, thank you for using our program!')