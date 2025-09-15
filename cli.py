from functions import get_todos, write_todos
import time

now=time.strftime("%b %m, %Y %H:%M:%S")
print("It is", now)


while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith('add'):
        todo = user_action[4:] + '\n'

        todos = get_todos()

        todos.append(todo)

        write_todos(todos)

    elif user_action == 'show':
        todos = get_todos()

        new_todos=[item.strip('\n') for item in todos]

        for index, item in enumerate(new_todos):
            print(f"{index + 1}-{item}")

    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            number = number - 1

            todos = get_todos()

            
            new_todo = input("Enter the new todo: ")
            todos[number] = new_todo + '\n'

            write_todos(todos)

        except ValueError:
            print("Your command is not valid.")
            continue

    elif user_action.startswith('complete'):
        try:    
            number = int(user_action[9:])

            todos = get_todos()

            todo_to_remove = todos[number - 1].strip('\n')
            todos.pop(number - 1)

            write_todos(todos)

            message = f"Todo {todo_to_remove} was removed from the list."  
            print(message)
        except IndexError:
            print("There is no item with that number.")
            continue 
    elif user_action == 'exit':
        break
    else:
        print("Command not valid.")

print("Bye!")
