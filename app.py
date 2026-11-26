task = []

def add(task):
    tasks.append(task)
    print(f"added: {task}")

def show():
    for i, t in enumerate(task,1):
        print(i,t)

if _name_==="__main__":
    add("Learn git")
    show()
