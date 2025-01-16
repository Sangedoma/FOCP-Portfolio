import sys
import os
from tabulate import tabulate

def convert_time_to_seconds(lap_time):
    try:
        minutes, seconds = lap_time.split(":")
        return int(minutes) * 60 + float(seconds)
    except ValueError:
        
        return float(lap_time)

def load_driver_details(filename):
    driver_details = {}
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            for line in file:
                parts = line.strip().split(',')
                if len(parts) >= 4:
                    code = parts[1]
                    name = parts[2]
                    team = parts[3]
                    driver_details[code] = (name, team)
    return driver_details

def process_lap_times(lap_filename, driver_filename):
    if not os.path.exists(lap_filename):
        print("Error: Lap times file does not exist.")
        return
    
    driver_details = load_driver_details(driver_filename)
    
    with open(lap_filename, 'r') as file:
        lines = file.readlines()
    
    if not lines:
        print("Error: Lap times file is empty.")
        return
    
    race_location = lines[0].strip()
    print(f"Race Name: {race_location}\n")
    
    driver_times = {}
    
    for line in lines[1:]:
        parts = line.strip().split()
        
        
        if len(parts) != 2:
            print(f"Skipping invalid entry: {line.strip()}")
            continue

        code, lap_time = parts
        
        try:
            time_in_seconds = convert_time_to_seconds(lap_time)
        except ValueError:
            print(f"Skipping invalid time format: {lap_time}")
            continue

        if code not in driver_times:
            driver_times[code] = []
        driver_times[code].append(time_in_seconds)
    
    if not driver_times:
        print("No valid lap times found.")
        return
    
    sorted_fastest_times = []
    table_data = []
    all_times = []
    
    for driver, times in driver_times.items():
        best_time = min(times)
        avg_time = sum(times) / len(times)
        sorted_fastest_times.append((driver, best_time))
        all_times.extend(times)
        name, team = driver_details.get(driver, ("Unknown", "Unknown"))
        table_data.append([driver, name, team, f"{avg_time:.3f}", f"{best_time:.3f}"])
    
    overall_fastest_driver, overall_fastest_time = min(sorted_fastest_times, key=lambda x: x[1])
    sorted_fastest_times.sort(key=lambda x: x[1], reverse=True)

    
    print("Driver Performance (Fastest Lap in Descending Order):")
    print(tabulate(table_data, headers=["Code", "Name", "Team", "Average Lap Time", "Fastest Lap"], tablefmt="grid"))
    print(f"\nOverall Fastest Lap: {overall_fastest_time:.3f} by {overall_fastest_driver} ({driver_details.get(overall_fastest_driver, ('Unknown',))[0]})")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <lap_times_filename> <drivers_filename>")
    else:
        process_lap_times(sys.argv[1], sys.argv[2])