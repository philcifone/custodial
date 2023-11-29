import csv

def log_task_completion(date, weather_temp, weather_conditions, moon_phase):
    section = input("Enter the section/task (e.g., boysBath, upHallDry, gym1Wet): ")
    task_number = int(input("Enter the task number: "))
    size = int(input("Enter the square footage of the section cleaned: "))
    duration = int(input("Enter time to complete task in Hours:Minutes:Seconds format: "))
    dirt_level = int(input("Enter 'dirtiness' level from 1-10, 10 being the dirtiest: "))
    gloves = int(input("How many pairs of gloves did you go through?: "))
    
    with open('task_completion_log.csv', 'a', newline='') as csvfile:
        fieldnames = [
            'Date', 
            'Section', 
            'Task Number', 
            'Size', 
            'Duration', 
            'Dirt Level', 
            'Gloves', 
            'Weather Temp', 
            'Weather Conditions', 
            'Moon Phase',
        ]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        if csvfile.tell() == 0:  # Write header only if the file is empty
            writer.writeheader()
        writer.writerow({
            'Date': date,
            'Section': section,
            'Task Number': task_number,
            'Size': size,
            'Duration': str(duration),
            'Dirt Level': dirt_level,
            'Gloves': gloves,
            'Weather Temp': weather_temp,
            'Weather Conditions': weather_conditions,
            'Moon Phase': moon_phase,
        })

# Get common inputs for the day
date = input("Enter the date in YYYY-MM-DD format: ")
weather_temp = int(input("Enter the temperature outside in Fahrenheit: "))
weather_conditions = input("Enter the weather conditions (e.g., sunny, cloudy, rain, snow): ")
moon_phase = input("Enter the moon phase by illumination percentage: ")

# Log task completion for each section/task
num_sections = 28  # You can change this number based on your actual requirement

for _ in range(num_sections):
    log_task_completion(date, weather_temp, weather_conditions, moon_phase)
