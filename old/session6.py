import tkinter as tk

root = tk.Tk()
root.title("my app")
root.geometry("400x300")
root.resizable(False, False)

python_var = tk.IntVar()
django_var = tk.IntVar()
docker_var = tk.IntVar()


tk.Label(root, text="مهارت های شما").pack()
tk.Checkbutton(root, text="پایتون", variable=python_var).pack(anchor="e", padx=30)
tk.Checkbutton(root, text="جنگو", variable=django_var).pack(anchor="e", padx=30)
tk.Checkbutton(root, text="داکر", variable=docker_var).pack(anchor="e", padx=30)


def show_selected():
    skills = []
    if python_var.get():
        skills.append("python")
    if django_var.get():
        skills.append("django")
    if docker_var.get():
        skills.append("docker")

    print(skills)


tk.Button(root, text="نمایش", command=show_selected).pack()
root.mainloop()
