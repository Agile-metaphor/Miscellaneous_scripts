import random
import time
import matplotlib.pyplot as plt
import numpy as np

# List of people and room numbers
people = ['Dav', 'Tep', 'Tes', 'Geo', 'Dum', 'Jos', 'Dai']
rooms = list(range(1, 8))

# Dictionary to hold tally results
tally = {name: [0] * 7 for name in people}

# Function to perform assignments and update tallies
def assign_and_tally():
    random.shuffle(people)
    for person, room in zip(people, rooms):
        tally[person][room - 1] += 1

# Function to update the bar chart
def update_chart():
    plt.clf()  # Clear the current figure
    x = np.arange(len(rooms))  # the label locations
    width = 0.1  # the width of the bars

    for i, person in enumerate(people):
        plt.bar(x + i*width, tally[person], width, label=person)

    plt.xlabel('Rooms')
    plt.ylabel('Number of Assignments')
    plt.title('Room Assignments Tally')
    plt.xticks(x + width * 3, rooms)
    plt.legend()
    plt.pause(0.1)  # Pause to update the plot

# Main execution loop
plt.ion()  # Turn on interactive plotting
fig, ax = plt.subplots()
for i in range(301):
    assign_and_tally()
    if i % 20 == 0:
        update_chart()
        time.sleep(1)  # Sleep to visually see the update

plt.ioff()  # Turn off interactive plotting
plt.show()