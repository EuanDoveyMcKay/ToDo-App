import customtkinter as tk
from BackEnd import ActiveTasks

tk.set_appearance_mode("dark")
tk.set_default_color_theme("dark-blue")

root = tk.CTk()
root.grid_rowconfigure(0, weight=1)  # configure grid system so that the correct column and row expands
root.grid_columnconfigure(0, weight=1)
TextFont = tk.CTkFont(family="Office", size=15)
TitleFont = tk.CTkFont(family="Office", weight="bold", underline=True, size=30)

MasterFrame = tk.CTkFrame(
    master=root,
    border_width=2,
    border_color="darkgrey",
    fg_color="grey10"
)

ActiveFrame = tk.CTkScrollableFrame(
    master=MasterFrame,
    width=450,
    fg_color="grey10"
)

CompletedFrame = tk.CTkScrollableFrame(
    master=MasterFrame,
    width=450,
    fg_color="grey10"
)

ArchivedFrame = tk.CTkScrollableFrame(
    master=MasterFrame,
    width=450,
    fg_color="grey10"
)

OpenedToDoFrame = tk.CTkScrollableFrame(
      master=root,
      width=450,
      fg_color="grey10"
)

OpenedToDoFrame.grid_rowconfigure(2, weight=1)
OpenedToDoFrame.grid_columnconfigure(1, weight=1)

def OpenToDo(TaskList, ParentFrame, ToDoTitle):
      OpenedToDoFrame.pack_forget()
      for todo in TaskList:
            if todo["Title"] == ToDoTitle:
                Title = tk.CTkLabel(
                        master=ParentFrame,
                        text=ToDoTitle,
                        font=TitleFont
                )
                Description = tk.CTkLabel(
                      master=ParentFrame,
                      text=todo["Description"],
                      font=TextFont
                )
                Duration = tk.CTkLabel(
                      master=ParentFrame,
                      text=todo["Duration"]+" hours",
                      font=TextFont
                )
                DoBy = tk.CTkLabel(
                      master=ParentFrame,
                      text=todo["Do by"],
                      font=TextFont
                )
                CloseButton = tk.CTkButton(
                    master=ParentFrame,
                    font=TextFont,
                    text="X",
                    width=50,
                    corner_radius=60,
                    command=CloseToDo
                )
                Title.grid(row=0, column=1, pady=(10,0))
                Duration.grid(row=0, column=0)
                DoBy.grid(row=1, column=1, pady=(0,20))
                Description.grid(row=2, column=1)
                CloseButton.grid(row=0, column=3)
                MasterFrame.grid_forget()
                OpenedToDoFrame.pack(expand=True, fill="both")
                break

            else:
                continue

def CloseToDo():
     OpenedToDoFrame.pack_forget()
     ActiveFrame.pack()
     MasterFrame.grid(row=0, column=0, sticky="nesw")

def FillListFrame(TaskList: list, ParentFrame: tk.CTkFrame): # TaskList is the desired list of "active", "completed" and "archived" while ParentFrame is the frame to put it in
        Title = tk.CTkLabel(
             master=ParentFrame,
             text="Tasks to complete",
             font=TitleFont
        )
        AddButton = tk.CTkButton(
             master=ParentFrame,
             font=TextFont,
             text="+",
             width=40,
             corner_radius=60
        )
        Title.pack(pady=10)
        for todo in TaskList:
            button = tk.CTkButton(
                master=ParentFrame,
                font=TextFont,
                text=todo["Title"],
                width=10,
                height=10,
                command=lambda: OpenToDo(TaskList,OpenedToDoFrame,button._text)
            )

            button.pack(pady=(10), fill="x")
        AddButton.pack(pady=(12,0))

def Main():
    FillListFrame(ActiveTasks, ActiveFrame)
    ActiveFrame.pack(expand=True, fill="both")
    MasterFrame.grid(row=0, column=0, sticky="nesw")
    root.mainloop()

Main()