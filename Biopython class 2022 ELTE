###################################TASK TWO
import matplotlib.pyplot as plt

def sir_model(S, I, R, beta, gamma, t):
    S_next = S - beta * (S * I) / (S + I + R)
    I_next = I + beta * (S * I) / (S + I + R) - gamma * I
    R_next = R + gamma * I
    return S_next, I_next, R_next
#simulate_sir function implements the SIR model by calling sir_model in a loop
def simulate_sir(S, I, R, beta, gamma, t_max):
    t = 0
    S_list = [S]
    I_list = [I]
    R_list = [R]
    while t < t_max:
        S, I, R = sir_model(S, I, R, beta, gamma, t)
        S_list.append(S)
        I_list.append(I)
        R_list.append(R)
        t += 1
    return S_list, I_list, R_list

def plot_asterisks(data, t_max):
    for i in range(t_max):
        print("*" * int(data[i] / 20), end="\n")

S = 1000
I = 1
R = 0
beta = 0.2
gamma = 0.1
t_max = 50
#beta and gamma in the code above are arbitrary
S_list, I_list, R_list = simulate_sir(S, I, R, beta, gamma, t_max)

plot_asterisks(S_list, t_max)
plot_asterisks(R_list, t_max)
#divide each value in data by 20/100 * 100 to get the proportion of the population, and then convert it to an integer by using int
def plot_asterisks(data, t_max):
    for i in range(t_max):
        print("*" * int(data[i] / (20/100) * 100), end="\n")



######################################TASK THREE
import random

def generate_rna_sequence(length, gc_content):
    nucleotides = ['A', 'U', 'C', 'G']
    gc_nucleotides = ['C', 'G']
    au_nucleotides = ['A', 'U']
    gc_count = int(gc_content / 100 * length / 2)
    au_count = int((100 - gc_content) / 100 * length / 2)
    gc_sequence = random.choices(gc_nucleotides, k=gc_count)
    au_sequence = random.choices(au_nucleotides, k=au_count)
    sequence = gc_sequence + au_sequence
    random.shuffle(sequence)
    return ''.join(sequence)
print(generate_rna_sequence(length=10, gc_content=60))
#change values here
def generate_rna_sequence(length, percent_A, percent_C, percent_U, percent_G):
    nucleotides = ['A'] * int(length * percent_A / 100) + \
                  ['C'] * int(length * percent_C / 100) + \
                  ['U'] * int(length * percent_U / 100) + \
                  ['G'] * int(length * percent_G / 100)
    random.shuffle(nucleotides)
    return ''.join(nucleotides[:length])
print(generate_rna_sequence(length=10, percent_A=40, percent_C=20, percent_U=20, percent_G=20))
#change values here

################### TASK SIX
# Import the required libraries
from collections import defaultdict

# Define the prices for each type of pizza
prices = {"Margherita": 1000, "Salami": 1200, "Funghi": 1100, 
          "Quattro Formaggi": 1250, "Calzone": 1250, "Frutti di Mare": 1500, "Hawaii": 1250}

# Read the data from the file into a list of tuples
data = []
with open("Pizzaorder.txt", "r") as f:
    for line in f:
        hour, type_, distance, delivery_guy = line.strip().split("\t")
        data.append((hour, type_, int(distance), delivery_guy))

# Calculate the revenue for each order
revenue = 0
for hour, type_, distance, delivery_guy in data:
    revenue += prices[type_] * distance

# Task 6.1  What is the busiest hour during the day?
hours = defaultdict(int)
for hour, type_, distance, delivery_guy in data:
    hours[hour] += 1
busiest_hour = max(hours, key=hours.get)

# Task 6.2  What is your revenue if Margherite cost 1000, Salami 1200, Funghi 1100, 
# Quatro formaggi 1250, Calzone 1250, Frutti di Mare 1500, Hawaii 1250 ?
print("Revenue: ", revenue)

# Task 6.3  How many pizzas were ordered before noon?
before_noon = 0
for hour, type_, distance, delivery_guy in data:
    h, m = map(int, hour.split(":"))
    if h < 12:
        before_noon += 1

print("Pizzas ordered before noon: ", before_noon)


#6.4
from collections import defaultdict

pizza_counts = defaultdict(int)
with open("Pizzaorder.txt") as f:
    for line in f:
        pizza_type = line.strip().split("\t")[1]
        pizza_counts[pizza_type] += 1

most_ordered_pizza = max(pizza_counts, key=pizza_counts.get)
num_orders = pizza_counts[most_ordered_pizza]
print("The most ordered pizza is", most_ordered_pizza, "with", num_orders, "orders")

#6.5
from collections import defaultdict

delivery_distances = defaultdict(int)
with open("Pizzaorder.txt") as f:
    for line in f:
        delivery_person, distance = line.strip().split("\t")[3:]
        delivery_distances[delivery_person] += int(distance)

most_travelled_person = max(delivery_distances, key=delivery_distances.get)
total_distance = delivery_distances[most_travelled_person]
print("The delivery person who travelled the most is", most_travelled_person, "with a total distance of", total_distance, "km")

#6.6
# Create a dictionary to map pizza types to prices
pizza_prices = {}
with open("Pizzaprices.txt") as f:
    for line in f:
        pizza_type, price = line.strip().split("\t")
        pizza_prices[pizza_type] = float(price)

# Use the dictionary to calculate the revenue for each order
revenues = defaultdict(float)
with open("Pizzaorder.txt") as f:
    for line in f:
        hour, pizza_type, distance, delivery_person = line.strip().split("\t")
        price = pizza_prices[pizza_type]
        revenue = price * int(distance)
        revenues[hour] += revenue

# Calculate the hourly revenue
highest_revenue = max(revenues.values())
highest_revenue_hour = [hour for hour, revenue in revenues.items() if revenue == highest_revenue][0]
print("The hour with the highest revenue is", highest_revenue_hour, "with a revenue of", highest_revenue, "USD")


