"""
Stock price analysis with Random, Pandas and Matplotlib:

The program simulates daily stock price changes,
calculates statistical metrics, and visualizes
the stock price development using a line chart.

author: Pferdeliebe
"""

import random
import matplotlib.pyplot as plt
import pandas as pd

current_day = 1000
day = "day "
days = [day + str(x) for x in range(1, 7001)]
values = [current_day]
daily_changes = []
stocks = {}

def show_day(number_of_day):
    """Displays the value for the given day."""
    print(f"value of {day + str(number_of_day)}: {stocks[day + str(number_of_day)]: .2f}")

def create_dictionary():
    """Creates a dictionary."""
    for n, m in zip(days, values):
        stocks[n] = m

def standard_deviation():
    """Displays the standard deviation."""
    standard_deviation = df.value.std()
    print(f"standard deviation: {standard_deviation: .2f}")

def maximum_show():
    """Determines and displays the global maximum."""
    max_value = df.value.max()
    max_day = df.value.idxmax()
    print(f"maximal value: {max_value: .2f},", f"day: {max_day}")
    return max_value, max_day

def minimum_show():
    """Determines and displays the global minimum."""
    min_value = df.value.min()
    min_day = df.value.idxmin()
    print(f"minimal value: {min_value: .2f},", f"day: {min_day}")
    return min_value, min_day

def mean_show():
    """Determines and displays the arithmetic mean."""
    arithmetic_mean = df.value.mean()
    print(f"arithmetic mean: {arithmetic_mean:.2f}")
    return arithmetic_mean

def line_chart(mittelwert, max_wert, max_tag, min_wert, min_tag):
    """Creates the line chart."""
    df["value"].plot(kind="line", label="stock price")
    plt.xlabel("day")
    plt.ylabel("value")
    plt.title("stock price")
    plt.axhline(y=mittelwert, color="pink", label="arithmetic mean")
    plt.scatter(max_tag, max_wert, color="red", s=100, marker=".")
    plt.annotate("maximum",
                 (max_tag, max_wert),
                 xytext=(2, 2),
                 textcoords="offset points")
    plt.scatter(min_tag, min_wert, color="orange", s=100, marker=".")
    plt.annotate("minimum",
                 (min_tag, min_wert),
                 xytext=(2, 2),
                 textcoords="offset points")
    plt.legend(loc="best")
    plt.show()

def create_df():
    """Creates the DataFrame."""
    global df
    d = {
        "day": days,
        "value": values
    }

    df = pd.DataFrame(d)
    return df

def calculation():
    """Calculates the days' values."""
    global current_day
    for t in range(1, 7000):
        next_day = current_day * (1 + daily_changes[t - 1])
        values.append(next_day)
        current_day = next_day

def random_daily_change():
    """Creates a random daily change."""
    for i in range(1,7000):
        daily_change = random.uniform(-0.02, 0.02)
        daily_changes.append(daily_change)

def main():
    random_daily_change()
    calculation()

    create_df()

    max_value, max_day = maximum_show()
    min_value, min_day = minimum_show()
    arithmetic_mean = mean_show()

    line_chart(arithmetic_mean, max_value, max_day, min_value, min_day)

    standard_deviation()

    create_dictionary()
    show_day(2)


if __name__ == "__main__":
    main()








