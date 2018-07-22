# Begin Lesson
# Line Graphs with Matplotlib

import codecademylib
from matplotlib import pyplot as plt

days = [0, 1, 2, 3, 4, 5, 6]
money_spent = [10, 12, 12, 10, 14, 22, 24]

plt.plot(days, money_spent)
plt.show()

import codecademylib
from matplotlib import pyplot as plt

time = [0, 1, 2, 3, 4]
revenue = [200, 400, 650, 800, 850]
costs = [150, 500, 550, 550, 560]

plt.plot(time, revenue)
plt.plot(time, costs)
plt.show()


import codecademylib
from matplotlib import pyplot as plt

time = [0, 1, 2, 3, 4]
revenue = [200, 400, 650, 800, 850]
costs = [150, 500, 550, 550, 560]

plt.plot(time, revenue,
        color='purple',
        linestyle='--')
plt.plot(time, costs,
        color='#82edc9',
        marker = 's')
plt.show()

import codecademylib
from matplotlib import pyplot as plt

x = range(12)
y = [3000, 3005, 3010, 2900, 2950, 3050, 3000, 3100, 2980, 2980, 2920, 3010]
plt.plot(x, y)

#your code here
plt.axis([0, 12, 2900, 3100])
plt.show()

import codecademylib
from matplotlib import pyplot as plt

x = range(12)
y = [3000, 3005, 3010, 2900, 2950, 3050, 3000, 3100, 2980, 2980, 2920, 3010]
plt.plot(x, y)
plt.axis([0, 12, 2900, 3100])
plt.xlabel('Time')
plt.ylabel('Dollars spent on coffee')
plt.title('My Last Twelve Years of Coffee Drinking')
plt.show()

import codecademylib
from matplotlib import pyplot as plt

months = range(12)
temperature = [36, 36, 39, 52, 61, 72, 77, 75, 68, 57, 48, 48]
flights_to_hawaii = [1200, 1300, 1100, 1450, 850, 750, 400, 450, 400, 860, 990, 1000]

plt.subplot(1, 2, 1)
plt.plot(months, temperature)

plt.subplot(1, 2, 2)
plt.plot(temperature, flights_to_hawaii, "o")

plt.show()

import codecademylib
from matplotlib import pyplot as plt

x = range(7)
straight_line = [0, 1, 2, 3, 4, 5, 6]
parabola = [0, 1, 4, 9, 16, 25, 36]
cubic = [0, 1, 8, 27, 64, 125, 216]

plt.subplot(2, 1, 1)
plt.plot(x, straight_line)
plt.subplot(2, 2, 3)
plt.plot(x, parabola)
plt.subplot(2, 2, 4)
plt.plot(x, cubic)
plt.subplots_adjust(bottom=0.2,
                   wspace=0.35)
plt.show()

import codecademylib
from matplotlib import pyplot as plt

months = range(12)
hyrule = [63, 65, 68, 70, 72, 72, 73, 74, 71, 70, 68, 64]
kakariko = [52, 52, 53, 68, 73, 74, 74, 76, 71, 62, 58, 54]
gerudo = [98, 99, 99, 100, 99, 100, 98, 101, 101, 97, 98, 99]

plt.plot(months, hyrule)
plt.plot(months, kakariko)
plt.plot(months, gerudo)

#create your legend here
legend_labels = ["Hyrule", "Kakariko", "Gerudo Valley"]
plt.legend(legend_labels, loc=8)
plt.show()

import codecademylib
from matplotlib import pyplot as plt

month_names = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep","Oct", "Nov", "Dec"]

months = range(12)
conversion = [0.05, 0.08, 0.18, 0.28, 0.4, 0.66, 0.74, 0.78, 0.8, 0.81, 0.85, 0.85]

plt.xlabel("Months")
plt.ylabel("Conversion")

plt.plot(months, conversion)

# Your work here

ax = plt.subplot()
ax.set_xticks(months)
ax.set_xticklabels(month_names)
ax.set_yticks([0.10, 0.25, 0.5, 0.75])
ax.set_yticklabels(['10%', '25%', '50%', '75%'])

plt.show()

import codecademylib
from matplotlib import pyplot as plt

word_length = [8, 11, 12, 11, 13, 12, 9, 9, 7, 9]
power_generated = [753.9, 768.8, 780.1, 763.7, 788.5, 782, 787.2, 806.4, 806.2, 798.9]
years = [2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009]

plt.close('all')

plt.figure()
plt.plot(years, word_length)
plt.savefig('winning_word_lengths.png')
plt.figure(figsize=(7,3))
plt.plot(years, power_generated)
plt.savefig('power_generated.png')

import codecademylib
from matplotlib import pyplot as plt

x = [1,2,3,4,5,6]
y1 = [0,6,7,8,9,10]
y2 = [10,9,8,7,6,5]

plt.plot(x, y1, color='pink', marker="o")
plt.plot(x, y2, color='gray', marker="o")
plt.title("Two Lines on One Graph")
plt.xlabel("Amazing X-axis")
plt.ylabel("Incredible Y-axis")
graph_legend = ["y1","y2"]
plt.legend(graph_legend, loc=4)
plt.show()






















# Project: Sublime Limes' Line Graphs

import codecademylib
from matplotlib import pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

visits_per_month = [9695, 7909, 10831, 12942, 12495, 16794, 14161, 12762, 12777, 12439, 10309, 8724]

# numbers of limes of different species sold each month
key_limes_per_month = [92.0, 109.0, 124.0, 70.0, 101.0, 79.0, 106.0, 101.0, 103.0, 90.0, 102.0, 106.0]
persian_limes_per_month = [67.0, 51.0, 57.0, 54.0, 83.0, 90.0, 52.0, 63.0, 51.0, 44.0, 64.0, 78.0]
blood_limes_per_month = [75.0, 75.0, 76.0, 71.0, 74.0, 77.0, 69.0, 80.0, 63.0, 69.0, 73.0, 82.0]


# create your figure here

plt.figure(figsize=(12,8))

# Left plot
plt.subplot(1, 2, 1)
ax1 = plt.subplot(1, 2, 1)
x_values = range(len(months))
ax1.plot(x_values, visits_per_month,color="purple")
ax1.set_xticks(x_values)
ax1.set_xticklabels(months)
plt.xlabel("Months")
plt.ylabel("Visits per Month")
plt.title("Website Monthly Visits")

# Right plot
plt.subplot(1, 2, 2)
ax2 = plt.subplot(1, 2, 2)
ax2.plot(x_values, key_limes_per_month, color = "green")
ax2.plot(x_values, persian_limes_per_month, color = "blue")
ax2.plot(x_values, blood_limes_per_month, color = "orange")
legend_names = ["Key Limes","Perisian Limes", "Blood Limes"]
plt.legend(legend_names, loc=1)
ax2.set_xticks(x_values)
ax2.set_xticklabels(months)
plt.xlabel("Months")
plt.title("Monthly Sales by Lime Type")


# Pull it all together
plt.subplots_adjust(bottom=0.2,
                   wspace=0.35)
plt.show()
plt.savefig('descriptive_file_name.png')






















# Lesson
# Different Plot Types


import codecademylib
from matplotlib import pyplot as plt

drinks = ["cappuccino", "latte", "chai", "americano", "mocha", "espresso"]
sales =  [91, 76, 56, 66, 52, 27]

heights = [88, 225, 365, 687, 4333, 10756, 30687, 60190, 90553]
x_values = range(len(heights))

days_in_year = [88, 225, 365, 687, 4333, 10756, 30687, 60190, 90553]

plt.bar(range(len(sales)), sales)
plt.show()

import codecademylib
from matplotlib import pyplot as plt

drinks = ["cappuccino", "latte", "chai", "americano", "mocha", "espresso"]
sales =  [91, 76, 56, 66, 52, 27]

plt.bar(range(len(drinks)), sales)

#create your ax object here

ax = plt.subplot()

ax.set_xticks([0, 1, 2, 3, 4, 5])

ax.set_xticklabels(drinks,
                  rotation=30) # degrees

plt.xlabel("Drinks")
plt.ylabel("Sales")

plt.show()

import codecademylib
from matplotlib import pyplot as plt

drinks = ["cappuccino", "latte", "chai", "americano", "mocha", "espresso"]
sales1 =  [91, 76, 56, 66, 52, 27]
sales2 = [65, 82, 36, 68, 38, 40]

n = 1  # This is our first dataset (out of 2)
t = 2 # Number of datasets
d = 6 # Number of sets of bars
w = 0.8 # Width of each bar
store1_x = [t*element + w*n for element
             in range(d)]

plt.bar(store1_x, sales1)

n = 2  # This is our second dataset (out of 2)
t = 2 # Number of datasets
d = 6 # Number of sets of bars
w = 0.8 # Width of each bar
store2_x = [t*element + w*n for element
             in range(d)]

plt.bar(store2_x, sales2)

plt.show()


import codecademylib
from matplotlib import pyplot as plt

drinks = ["cappuccino", "latte", "chai", "americano", "mocha", "espresso"]
sales1 =  [91, 76, 56, 66, 52, 27]
sales2 = [65, 82, 36, 68, 38, 40]

plt.bar(range(len(drinks)),sales1)
plt.bar(range(len(drinks)),sales2,
       bottom=sales1)

legend_names = ["Location 1","Location 2"]
plt.legend(legend_names, loc=1)

plt.show()


import codecademylib
from matplotlib import pyplot as plt

drinks = ["cappuccino", "latte", "chai", "americano", "mocha", "espresso"]
ounces_of_milk = [6, 9, 4, 0, 9, 0]
error = [0.6, 0.9, 0.4, 0, 0.9, 0]

# Plot the bar graph here

plt.bar(range(len(drinks)),ounces_of_milk
       ,yerr=error, capsize=5)

plt.show()


import codecademylib
from matplotlib import pyplot as plt

months = range(12)
month_names = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
revenue = [16000, 14000, 17500, 19500, 21500, 21500, 22000, 23000, 20000, 19500, 18000, 16500]

#your work here

plt.plot(months, revenue)

ax = plt.subplot()
ax.set_xticks(months)
ax.set_xticklabels(month_names) 

y_lower = [0.9 * i for i in revenue]
y_upper = [1.1 * i for i in revenue]

plt.fill_between(months, y_lower, y_upper,
                alpha=0.2)


import codecademylib
from matplotlib import pyplot as plt
import numpy as np

payment_method_names = ["Card Swipe", "Cash", "Apple Pay", "Other"]
payment_method_freqs = [270, 77, 32, 11]

#make your pie chart here

plt.pie(payment_method_freqs)
plt.axis('equal')

plt.show()


import codecademylib
from matplotlib import pyplot as plt

payment_method_names = ["Card Swipe", "Cash", "Apple Pay", "Other"]
payment_method_freqs = [270, 77, 32, 11]

#plt.pie(payment_method_freqs)
plt.axis('equal')

#option 1
#plt.legend(payment_method_names)
#option 2
#plt.pie(payment_method_freqs, labels=payment_method_names)

plt.pie(payment_method_freqs, 
       labels = payment_method_names,
       autopct = '%0.1f%%')

#other options
# '%0.2f'   = 2 decimal places, like 4.08
# '%d%%'    = rounded to the nearest integer and with a percent sign, like 4%

plt.show()


import codecademylib
from matplotlib import pyplot as plt
from script import sales_times

#create the histogram here

plt.hist(sales_times,
        bins=20)
#defaults to ten bins

plt.show()


import codecademylib
from matplotlib import pyplot as plt
from script import sales_times1
from script import sales_times2

#plt.hist(sales_times1, bins=20)
#plot your other histogram here

#alpha can be a value between 0 and 1
#alpha sets the transparency of the histogram
#alpha=1 makes things opaque

#to just draw outline, use histtype='step'

#normed=True divides the height of each column by a constant so that the total shaded area of histograms sums to 1

plt.hist(sales_times1, bins=20, alpha=0.4,normed=True)
plt.hist(sales_times2, bins=20, alpha=0.4,normed=True)

plt.show()









# Project: Recreate Graphs using Matplotlib
# Optional


