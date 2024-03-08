tasks = {}

def add_task(time, task):
    tasks[time] = task
    print(f"Task added at {time}: {task}")

def main():
    add_task('09:00', 'Breakfast')
    print(f"Today's tasks: {tasks}")

if __name__ == '__main__':
    main()
