def print_menu():
    # This function prints the menu
  print('\nTodo List Menu:')
  print('1. View Tasks')
  print('2. Add a Task')
  print('3. Remove a Task')
  print('4. Exit')
  

def get_choice():
    # This function gets the user's choice and returns it
  while True:
    choice = input('Enter your choice: ')
    valid_choices = ('1', '2', '3', '4')
    if choice not in valid_choices:
      print('Invalid choice')
      continue
    else:
      return choice


def display_tasks(tasks):
    # This function displays the tasks in the list
  if not tasks:
    print('No tasks in the list.')
    return
  
  for index, task in enumerate(tasks, start=1):
    print(f'{index}. {task}')


def add_task(tasks):
  # This function adds a new task to the list
  while True:
    task = input('Enter a new task: ').strip()
    if len(task) != 0:
      tasks.append(task)
      break
    else:
      print('Invalid task!')


def remove_task(tasks):
    # This function removes a task from the list
  display_tasks(tasks)

  while True:
    try:
      task_number = int(input('Enter the task number: '))
      if 1 <= task_number <= len(tasks):
        tasks.pop(task_number - 1)
        break
      else:
        raise ValueError
    except ValueError:
      print('Invalid task number')

def main():
  # This is the main function
  tasks = []

  while True:
    print_menu()

    choice = get_choice()

    if choice == '1':
      display_tasks(tasks)
    elif choice == '2':
      add_task(tasks)
    elif choice == '3':
      remove_task(tasks)
    else:
      break
  

if __name__ == '__main__':
  main()