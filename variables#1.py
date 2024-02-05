Fitness tracker: you're building a fitness tracker app. create variables to store daily steps, distane walked, and calories burned. write expressions to calculate average steps per week and total distance covered in a month.


average_distance = int(input("enter distance:"))
Days_in_month = 30
average_steps_per_week = (total_steps)
total_distane = (average_steps_per_week) * (average_distane) * (days_in_month)

print(total_distance)



use variable to store items names, quantity and prices. calculate the total cost f items and check if you have enough budget.


item1 =int(input("Enter a item name:"))
item_names = ("Bread", "cheese", "rice", "pasta")
price = [20.5, 40.4, 4.5, 200.5]
quantity = [5, 4, 1, 10]
budget = 40
total_cost = sum(quantity*price for quantity, price in zip (quantity, price))
if total_cost <= budget:

    print("your budget")
    else:
        print("out of your budget")



Design a recipe calulator that adjusts ingredient quantities based on the  number of serving.


num_servings = int(input("Enter number of serving"))
ingredient = ["meat", "chicken", "wheat", "tomatoes", "Eggs"]
amounts = [5, 3, 1, 4, 6,]

adjusted_quantities = [amoun* num_servings for amount in anoumts]

print(adjusted_quantities)



uese variables to store genre, rating and release year. write expressions to compare movies and suggest matches.


movies_name = int(input("enter a movie name"))
movies_name1 = "Bahubali"
movies_name2 = "Jadugar"
movies_name3 = "Dhamal"

store_genre = ["funny, "comedy, "drama","thriller"]
ratings = [ 7.5, 6.4, 4.5, 3.9]
release_year = [2007, 2010, 2011, 2013]

if movies_name == 'Bahubali':
print("fully recommended")
elif movies_name == 'Bahubali':
    print("if you are stronge than watch this because it is a comedy movie")
elif movies_name == 'Jadugar':
    print("recommended for you have good sense humour")
    else:
        print("not recommendrd movie")




tasks = ["coding", "reading", "exercise"]
durations = [2, 1, 0.5]  # in hours



# Calculate total time spent on each task
total_time_per_task = {task: duration for task, duration in zip(tasks, durations)}
print("Total time spent on each task:")
for task, duration in total_time_per_task.items():
    print(task, duration, "hours")

# Identify areas for improvement (assuming you want to maximize coding time)
max_time_task = max(total_time_per_task.values())
improvement_areas = [task for task, duration in total_time_per_task.items() if duration < max_time_task and task != "coding"]
print("Areas for improvement (to maximize coding time):")
for area in improvement_areas:
    print(area)

