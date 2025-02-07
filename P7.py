import pandas as pd
import sys

# Assuming df is already loaded

# Function to get the best room type based on reviews for a city
def best_room_type_by_reviews(city):
    city_df = df[df['City'] == city]
    if city_df.empty:
        return "No data available for this city."
    
    city_df = city_df.dropna(subset=['Reviews'])
    if city_df.empty:
        return "No reviews data available for this city."
    
    best_room = city_df.loc[city_df['Reviews'].idxmax()]
    return best_room['PType']

# Function to get the cheapest room in the city, its Location, and Type
def cheapest_room_in_city(city):
    city_df = df[df['City'] == city]
    if city_df.empty:
        return "No data available for this city."
    
    city_df = city_df.dropna(subset=['PPN'])
    if city_df.empty:
        return "No price data available for this city."
    
    cheapest_room = city_df.loc[city_df['PPN'].idxmin()]
    return f"Cheapest Room: {cheapest_room['ID']}, Location: {cheapest_room['Location']}, Type: {cheapest_room['PType']}"

# Function to get the costliest room in the city, its Location, and Type
def costliest_room_in_city(city):
    city_df = df[df['City'] == city]
    if city_df.empty:
        return "No data available for this city."
    
    city_df = city_df.dropna(subset=['PPN'])
    if city_df.empty:
        return "No price data available for this city."
    
    costliest_room = city_df.loc[city_df['PPN'].idxmax()]
    return f"Costliest Room: {costliest_room['ID']}, Location: {costliest_room['Location']}, Type: {costliest_room['PType']}"

# Function to get the average PPN for a city
def average_ppn_for_city(city):
    city_df = df[df['City'] == city]
    if city_df.empty:
        return "No data available for this city."
    
    city_df = city_df.dropna(subset=['PPN'])
    if city_df.empty:
        return "No price data available for this city."
    
    avg_ppn = city_df['PPN'].mean()
    return f"Average PPN for {city}: {avg_ppn}"

# Main script to take city name from command line argument
if __name__ == "__main__":
    # Get the city name from command line argument
    if len(sys.argv) < 2:
        print("Please provide a city name as a command line argument.")
        sys.exit(1)
    
    city_name = sys.argv[1]
    
    # Print the best room type based on reviews
    best_room = best_room_type_by_reviews(city_name)
    print(f"Best Room Type based on Reviews: {best_room}")

    # Print the cheapest room in the city, its location and type
    cheapest_room = cheapest_room_in_city(city_name)
    print(f"Cheapest Room: {cheapest_room}")

    # Print the costliest room in the city, its location and type
    costliest_room = costliest_room_in_city(city_name)
    print(f"Costliest Room: {costliest_room}")

    # Print the average PPN for the city
    avg_ppn = average_ppn_for_city(city_name)
    print(f"Average PPN for {city_name}: {avg_ppn}")
