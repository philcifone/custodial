import csv
import datetime

def log_task_completion():
    section = input("Enter the section (e.g., Boys Bathroom): ")
    task_number = int(input("Enter the task number: "))
    start_time = datetime.datetime.now()
    
    # Simulate cleaning task
    input("Press Enter when you've completed the cleaning task...")
    
    end_time = datetime.datetime.now()
    duration = end_time - start_time
    
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%s')
    
    with open('task_completion_log.csv', 'a', newline='') as csvfile:
        fieldnames = ['Timestamp', 'Section', 'Task Number', 'Start Time', 'End Time', 'Duration']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        if csvfile.tell() == 0:  # Write header only if the file is empty
            writer.writeheader()
        writer.writerow({
            'Timestamp': timestamp,
            'Section': section,
            'Task Number': task_number,
            'Start Time': start_time.strftime('%H:%M:%S'),
            'End Time': end_time.strftime('%H:%M:%S'),
            'Duration': str(duration)
        })

# Example usage
log_task_completion()
