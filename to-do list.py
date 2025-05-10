from tkinter import *
import tkinter.messagebox

def entertask():
    input_text = ""

    def add():
        input_text = entry_task.get(1.0, "end-1c")

        if input_text == "":
            tkinter.messagebox.showwarning(title="Warning!", message="Please enter a task")
        else:
            listbox_task.insert(END, input_text)
            #close the root1 window
            root1.destroy()
    
    root1=Tk()  #A new window to pop up to take input
    root1.title("Add task")
    entry_task = Text(root1, width=40, height=4)
    entry_task.pack()
    button_temp = Button(root1, text="Add task", command=add)
    button_temp.pack()
    root1.mainloop()

#function to delete task from the listbox
def deletetask():
    #select the selected item and then delete it
    selected = listbox_task.curselection()
    listbox_task.delete(selected[0])

#function to mark task as completed
def markcompleted():
    marked = listbox_task.curselection()
    temp = marked[0]
    #store the text of selected item in a string
    temp_marked = listbox_task.get(marked)
    #update it
    temp_marked = temp_marked + " ✔"
    #delete it then insert it
    listbox_task.delete(temp)
    listbox_task.insert(temp, temp_marked)


window = Tk()  #creating window for app
window.title("My To-Do List")  #title of app at the top

#frame widget to hold multiple widgets like listbox and scrollbar
frame_task = Frame(window)
frame_task.pack()  #organizes the widget properly

#hold items in listbox
listbox_task = Listbox(frame_task, bg="black", fg="white", height=15, width=60, font="Helvetica")
listbox_task.pack(side=tkinter.LEFT)

#scrolldown in case total list exceeds the size given of the window
scrollbar_task = Scrollbar(frame_task)
scrollbar_task.pack(side=tkinter.RIGHT, fill=tkinter.Y)
listbox_task.config(yscrollcommand = scrollbar_task.set)
scrollbar_task.config(command = listbox_task.yview)

#button widget
entry_button = Button(window, text="Add task", width=50, command=entertask)
entry_button.pack(pady = 3)

delete_button = Button(window, text="Delete selected task", width=50, command=deletetask)
delete_button.pack(pady = 3)

mark_button = Button(window, text="Mark as completed", width=50, command=markcompleted)
mark_button.pack(pady = 3)

window.mainloop()  #runs Tkinter event loop, runs and displays everything written in the code





