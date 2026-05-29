


def complete (to_do_list, completed_tasks):
    combined_tuple=()
    task_lookup=input("Which task should be marked as complete: ")
    for index in range (len(to_do_list)):
        if to_do_list[index]==task_lookup:
            store_value=to_do_list.pop(index)
            short_tuple=(store_value,)
            combined_tuple=completed_tasks+short_tuple
            return combined_tuple
    
    print ("Task does not exist")
    return completed_tasks
	       
	       
   


def main():
    my_list = []
    completed_tasks = ()
    start_manager=" "
    while start_manager!=5:
        start_manager = input(
            "\nWhat would you like to do for the to-do list:\n"
            "1.) Add Task\n"
            "2.) Remove Task\n"
            "3.) Display all Tasks\n"
            "4.) Complete Tasks\n"
            "5.) Display completed_tasks\n"
            "6.) Log Out \n"
        )
        if start_manager == "1":
            task = input('Enter the task to add: ')
            my_list.append(task)
        elif start_manager == "2":
            task = input('Enter the task to remove: ')
            if task in my_list:
                my_list.remove(task)
            else:
                print('Task does not exist.')
        elif start_manager == "3":
            if my_list:
                for index in range(len(my_list)): 
                    print(index+1,". " ,my_list[index])
            else:
                print('No tasks in the to-do list.')
        elif start_manager == "4":
            completed_tasks = complete(my_list, completed_tasks)
        elif start_manager== "5":
            print(completed_tasks)
        elif start_manager == "6":
            print('Goodbye')
            break
        else:
            print('Invalid option')


if __name__ == '__main__':
    main()
	