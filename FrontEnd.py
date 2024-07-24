import customtkinter as tk
from Main import ActiveTasks

tk.set_appearance_mode("dark")
tk.set_default_color_theme("dark-blue")

root = tk.CTk()
root.grid_rowconfigure(0, weight=1)  # configure grid system
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
                      text=todo["Duration"],
                      font=TextFont
                )
                DoBy = tk.CTkLabel(
                      master=ParentFrame,
                      text=todo["Do by"],
                      font=TextFont
                )
                Title.pack()
                Description.pack()
                Duration.pack()
                DoBy.pack()
                MasterFrame.grid_forget()
                OpenedToDoFrame.pack()
                break

            else:
                continue
                  

def FillListFrame(TaskList: list, ParentFrame): # TaskList is the desired list of "active", "completed" and "archived" while ParentFrame is the frame to put it in
        for todo in TaskList:
            button = tk.CTkButton(
                master=ParentFrame,
                font=TextFont,
                text=todo["Title"],
                width=10,
                height=10,
                command=lambda: OpenToDo(TaskList,OpenedToDoFrame,button._text)
            )
            button.pack(
                  pady=(10),
                  fill="x"
            )
      
FillListFrame(ActiveTasks, ActiveFrame)
ActiveFrame.pack()
MasterFrame.grid(row=0, column=0)
root.mainloop()