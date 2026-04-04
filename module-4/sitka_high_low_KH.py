import csv
import sys
from datetime import datetime
from matplotlib import pyplot as plt

FILENAME = 'sitka_weather_2018_simple.csv'

def print_instructions():
    print("\n" + "=" * 40)
    print("   Sitka Weather Viewer - 2018")
    print("=" * 40)
    print("View daily temperature graphs for Sitka, AK.")
    print("\nMenu Options:")
    print("  HIGH - View High temperatures (red)")
    print("  LOW  - View Low  temperatures (blue)")
    print("  EXIT - Exit the program")
    print("=" * 40)

def load_weather_data():
    dates, highs, lows = [], [], []
    with open(FILENAME) as f:
        reader = csv.reader(f)
        header_row = next(reader)
        for row in reader:
            current_date = datetime.strptime(row[2], '%Y-%m-%d')
            dates.append(current_date)
            highs.append(int(row[5]))
            lows.append(int(row[6]))
    return dates, highs, lows

def plot_temperatures(dates, temps, label, color):
    fig, ax = plt.subplots()
    ax.plot(dates, temps, c=color)
    plt.title(f"Daily {label} Temperatures - Sitka, AK 2018", fontsize=24)
    plt.xlabel('', fontsize=16)
    fig.autofmt_xdate()
    plt.ylabel("Temperature (F)", fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)
    plt.show()

def main():
    print_instructions()

    print("\nLoading weather data...", end=' ')
    try:
        dates, highs, lows = load_weather_data()
        print("Done.")
    except FileNotFoundError:
        print(f"\nError: '{FILENAME}' not found. Make sure it's in the same folder.")
        sys.exit(1)

    while True:
        print("\nEnter your choice (HIGH / LOW / EXIT): ", end='')
        choice = input().strip().upper()

        if choice == 'HIGH':
            print("Generating high temperatures graph...")
            plot_temperatures(dates, highs, "High", "red")

        elif choice == 'LOW':
            print("Generating low temperatures graph...")
            plot_temperatures(dates, lows, "Low", "blue")

        elif choice == 'EXIT':
            print("\n" + "=" * 40)
            print("  Thanks for using Sitka Weather Viewer!")
            print("  Stay cool. Goodbye!")
            print("=" * 40 + "\n")
            sys.exit(0)

        else:
            print(f"  '{choice}' is not a valid option. Please enter HIGH, LOW, or EXIT.")

if __name__ == '__main__':
    main()