import sqlite3
db_file = "tasks.db"

def init_of_database():
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS tasks(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    completed INTEGER DEFAULT 0
    )
    """)
    conn.commit()
    conn.close()
def f():
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    cursor.execute("SELECT id , title, completed FROM tasks")
    tasks=cursor.fetchall()
    conn.close()
    return tasks
def insert(title):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO tasks (title, completed) VALUES (?, ?)", (title, 0))
    conn.commit()
    conn.close()
def update(task_id):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    cursor.execute("""
    UPDATE tasks
    SET completed = CASE
    WHEN completed = 0 THEN 1
    ELSE 0
    END
    WHERE id =?
    """,(task_id,))
    if cursor.rowcount == 0:  
        print("Task not found! You entered wrong task id!")
    else:
        print("Task status updated!")

    conn.commit()
    conn.close()
def delete(task_id):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM tasks WHERE id = ?",(task_id,))
    conn.commit()
    conn.close()
def display():
    tasks = f()
    if not tasks:
        print("\n Your To_do list is empty.")
    else:
        print("******** Your to do list *******")
        for task in tasks:
            if task[2]==1:
                status = "Done Boss"
            else:
               status = "Not done"
            print(f"{task[0]}. {task[1]} - {status}")
def add():
    y = int(input("Enter how many task you want to add? "))
    for i in range(y):
        title= input(f"Enter your task {i+1}: ").strip()
        if title:
            insert(title)
            print(f"Task: {title} added!")
        else:
            print("Its empty")
def update_task():
    display()
    try:
        task_id = int(input("Enter the task id to update: "))
        update(task_id)
        print("Task status updated!")
    except Exception as p :
        print(p)
def dell():
    display()
    try:
        task_id = input("Enter the task id to delete: ")
        delete(task_id)
        print("Task deleted")
    except Exception as r:
        print(r)
def main():
    init_of_database()
    while True:
        print("\n--------- TO-DO LIST MENU ---------")
        print("Here are your choices :)")
        print("1. View To-Do List.")
        print("2. Add as many tasks you want.")
        print("3. Update Task Status by task id.")
        print("4. Delete a Task by task id.")
        print("5. Exit.")
        choice = input("Enter your choice (1-5): ").strip()
        if choice=='1':
            display()
        elif choice=='2':
            add()
        elif choice=='3':
            update_task()
        elif choice=='4':
            dell()
        elif choice=='5':
            print("\n Goodbye!")
            print("\n Have a nice day :)")
            break
        else:
            print("Invalid choice , you are free to try again")

if __name__ == "__main__":
    main()

