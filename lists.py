todo_file = open("todo.txt", "w+")
new_task = "y"
todo_dict = {}


while new_task != "n":
    task = raw_input("to do: ")

    done = raw_input("done? y/n:")
    if done == "y":
        todo_dict[task] = True
    else:
        todo_dict[task] = False
    new_task = raw_input("more things to do:  y/n: ")


todo_file.write("Done:\n")
for item in todo_dict:
    if todo_dict[item] == True:
        todo_file.write(item)
        todo_file.write("\n")

todo_file.write("Not Done:\n")
for item in todo_dict:
    if todo_dict[item] == False:
        todo_file.write(item)
        todo_file.write("\n")

todo_file.close()
