import csv
import datetime

def log_task_completion():
    section = input("Enter the section/task (e.g., boysBath, upHallDry, gym1Wet): ")
    taskNumber = int(input("Enter the task number: "))
    date = input("Enter the date completed in YYYY-MM-DD format: ")
    size = int(input("Enter the square footage of the section cleaned: "))
    duration = input("Enter time to complete task in Hours:Minutes:Seconds format: ")
    dirtLevel = int(input("Enter 'dirtyness' level from 1-10, 10 being the dirtiest: "))
    gloves = int(input("How many pairs of gloves did you go through?: "))
    weatherTemp = int(input("What was the temperature outside in Fahrenheit?: "))
    weatherCond = input("What were weather conditions like? (e.g. sunny, cloudy, rain, snow): ")
    moonPhase = input("By illumination percentage, what is the moon phase?: ")
    
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
            'Task Number': taskNumber,
            'Size': size,
            'Duration': str(duration),
            'Dirt Level': dirtLevel,
            'Gloves': gloves,
            'Weather Temp': weatherTemp,
            'Weather Conditions': weatherCond,
            'Moon Phase': moonPhase,
        })

# Example usage
log_task_completion()
