#Set variables to change prices of hotel and rental car when required
hotel_per_night = 100
rental_per_day = 50

#Dictionary of available flight options
flight_options = {
    "LONDON": 400,
    "TOKYO": 900,
    "BERLIN": 500,
    "FARO": 300,
    #Please add more cities as required
}

#Function to ensure user enters a valid int
def get_valid_int(prompt):
    while True:
        try:
            user_input = int(input(prompt))
            return user_input
        except ValueError:
            print("Please enter a number")

#Function to calculate the total cost of the hotel
def hotel_cost(num_nights):
    return num_nights * hotel_per_night

#Function to calculate the total cost of the rental car
def car_rental(rental_days):
    return rental_days * rental_per_day

#Function to calculate the total cost of the flight based off the city chosen
def plane_cost(city_flight, flight_cost):
    return flight_cost.get(city_flight)

#Function to calculate the total cost of the holiday
def holiday_cost(city_flight, num_nights, rental_days, flight_cost):
    flight_cost = plane_cost(city_flight, flight_cost)
    hotel_cost_value = hotel_cost(num_nights)
    car_rental_cost = car_rental(rental_days)

    total_cost = flight_cost + hotel_cost_value + car_rental_cost
    return total_cost

#Function to display the flight options
def display_options(flight_options):
    print("\nFlight Options:")
    for city, cost in flight_options.items():
        print(f"{city}: £{cost}")

#Function to check if valid option chosen
def get_valid_city(flight_options):
    while True:
        city_flight = input("Please enter your city of departure:\n").upper()
        if city_flight in flight_options:
            return city_flight
        else:
            print(f"""\nApologies, we do not currently fly to {city_flight}.
Please choose an option from the below list:""")
            display_options(flight_options)

display_options(flight_options)

#Request user input for days staying and hire car requirements
num_nights = get_valid_int("Please enter the number of nights you will be staying:\n" )
rental_days = get_valid_int("Please enter the number of days you will require a hire car:\n")

#Call function to request destination and confirm it is within the available options
city_flight = get_valid_city(flight_options)

#Calls function to calculate the total cost
total_holiday_cost = holiday_cost(city_flight, num_nights, rental_days, flight_options)

#Displays user input
print(f"""
Holiday Details:
Destination: {city_flight}
Hotel Cost: £{hotel_cost(num_nights)}
Flight Cost: £{plane_cost(city_flight, flight_options)}
Car Rental Cost: £{car_rental(rental_days)}
Total Holiday Cost: £{total_holiday_cost}
""")
