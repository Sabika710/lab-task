class To_do_list:
    def __init__(self, filename):
        self.task=[]
        self.filename=filename
    
        
    def display(self):
        for i in range(len(self.task)):
            print(self.task[i])
            
    def add_task(self):
        num_of_task=int(input("How many task you want to enter? "))
        for task in range(num_of_task):
            task=input("Enter Task: ")
            self.task.append(task)    
        self.save_file()
        
    def Remove_task(self, task):
        if task in self.task:
            self.task.remove(task)
        self.save_file()
        
    def save_file(self):
        with open(self.filename, 'w')as file:
            for task in self.task:
                file.write(task + "\n")
                
    def load_file(self):
        try:
            with open(self.filename, 'r')as file:
                self.task = [line.strip() for line in file.readlines()]
        except FileNotFoundError:
            pass
        
            
def main():
    filename = "To_do_list"
    todolist=To_do_list(filename)
    
    while True:
        print("1:Display Task")
        print("2:Delete Task")
        print("3:Add Task")
        print("4:Exit")
    
        choice=int(input("Enter a choice 1 to 4: "))
        if choice == 1:
            todolist.display()
        
        elif choice == 2:
            task=input("Enter task to delete: ")
            todolist.Remove_task(task)
        
        elif choice == 3:
            todolist.add_task()
        
        elif choice== 4:
            break
        
        else: 
            print("Invalid option")
            
if __name__=='__main__':
    main()

        