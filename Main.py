# Functions and the mainloop for my ToDo app project

# A list of all the "ToDo's", which themselves are dictionaries
ActiveTasks = [

    {"Title": "test",
     "Descripton": "Some Rando test",
     "Duration": "40", #in hours
     "Do by": "Enter Date here"},

     {"Title": "atest",
      "Descripton": "Some Rando test",
      "Duration": "40", #in hours
      "Do by": "Enter Date here"}
]

CompletedTasks = [

]

SortType = "Alphabetic Ascending"

def NewToDo(Title, Description, Duration, DoBy):
    ActiveTasks.append({"Title": Title,
                        "Description": Description,
                        "Duration": Duration,
                        "Do by": DoBy})
    # Insert the sort list function here

def DeleteToDo(Title):
    # Deletes the ToDo entry with the title of the parameter...
    for ToDo in ActiveTasks:
        if ToDo["Title"] == Title:
            ActiveTasks.remove(ToDo)
            break

def CompleteToDo(Title):
    # Moves the ToDo with the title of parameter to the "CompletedTasks" list
    for ToDo in ActiveTasks:
        if ToDo["Title"] == Title:
            CompletedTasks.append(ActiveTasks.pop(ActiveTasks.index(ToDo))) # No, "Active.remove(...)" won't work here, I tried
            break

def UncompleteToDo(Title):
    # Restores a ToDo back into active tasks in case of accidental deletion
    for ToDo in CompletedTasks:
        if ToDo["Title"] == Title:
            ActiveTasks.append(CompletedTasks.pop(CompletedTasks.index(ToDo)))
            break

def AlphabeticSortToggle(CurrentSortType):
    if CurrentSortType == "Alphabetic Ascending":
        return "Alphabetic Descending"
    
    else:
        return "Alphabetic Ascending"

def DoBySortToggle(CurrentSortType):
    if CurrentSortType == "DoBy Ascending":
        return "DoBy Descending"
    
    else:
        return "DoBy Ascending"

def DurationSortToggle(CurrentSortType):
    if CurrentSortType == "Duration Ascending":
        return "Duration Descending"
    
    else:
        return "Duration Ascending"

def SortList(CurrentSortType, ListToSort):
    # Takes a sort type and any list of dicts as input, and outputs the appropriate ordered version of it
    if CurrentSortType == "Alphabetic Ascending":
        return sorted(ListToSort, key=lambda x: x["Title"], reverse=False) # lambda is weird, so I can't explain it, but I'm sure you can figure out what it is doing here

    elif CurrentSortType == "Alphabetic Descending":
        return sorted(ListToSort, key=lambda x: x["Title"], reverse=True)

    elif CurrentSortType == "DoBy Ascending":
        return sorted(ListToSort, key=lambda x: x["Do by"], reverse=False)

    elif CurrentSortType == "DoBy Descending":
        return sorted(ListToSort, key=lambda x: x["Do by"], reverse=True)

    elif CurrentSortType == "Duration Ascending":
        return sorted(ListToSort, key=lambda x: x["Duration"], reverse=False)

    elif CurrentSortType == "Duration Descending":
        return sorted(ListToSort, key=lambda x: x["Duration"], reverse=True)

#print(str(ActiveTasks[0]),"\n",str(ActiveTasks[1]))
#ActiveTasks = SortList(SortType, ActiveTasks)          <---- Testing for this sort function if u wanna check it works (it does)
#print(str(ActiveTasks[0]),"\n",str(ActiveTasks[1]))