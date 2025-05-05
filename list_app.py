import tkinter as tk


root = tk.Tk()
root.title("To-Do List App")
root.geometry("400x500")
root.configure(bg="lightgrey")

label = tk.Label(root, text="Welcome! What's your schedule?", font=("Arial", 14), bg="lightgrey")
label.pack(pady=5)


tasks = []


def add_task():
    task_text = entry.get()  
    if task_text:  
        listbox.insert(tk.END, task_text)  
        tasks.append(task_text)  
        entry.delete(0, tk.END)  


def delete_task():
    selected = listbox.curselection()
    if selected:
        index = selected[0]
        listbox.delete(index)
        tasks.pop(index)

#
entry = tk.Entry(root, width=25, font=("Arial", 14))
entry.pack(pady=10)


listbox = tk.Listbox(root, width=30, height=10, font=("Arial", 12))
listbox.pack(pady=10)


add_btn = tk.Button(root, text="Add Task", command=add_task)
add_btn.pack()


delete_btn = tk.Button(root, text="Delete Task", command=delete_task)
delete_btn.pack()


root.mainloop()