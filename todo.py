import pickle

class todoList:

    todos = []
    file = ""

    def __init__(self, file:str = "listPickle"):
        self.file = file
        self.todos = self.read_list()

    def read_list(self):
        try:
            with open(self.file, "rb") as openfile:
                todos = pickle.load(openfile)
        except:
            print(f"file {self.file} not found, initializing new todo list")
            todos = []
        return todos

    def update_task_nrs(self):
        for nr, task in enumerate(self.todos, start=1):
            task["number"] = nr

    def write_list(self):
        with open(self.file, "wb") as openfile:
            pickle.dump(self.todos, openfile)

    def add_task(self, task:str)->None:
        task_nr = len(self.todos) + 1
        full_task = {"number": task_nr,
                     "task": task,
                     "done": False}
        self.todos.append(full_task)

    def remove_task(self, task_nr: int):
        if (task_nr > 0) & (task_nr <= len(self.todos)):
            self.todos.pop(task_nr-1)
            self.update_task_nrs()

    def mark_task(self, task_nr):
        if (task_nr > 0) & (task_nr <= len(self.todos)):
            self.todos[task_nr-1]["done"] = not self.todos[task_nr-1]["done"]

    def print_todos(self):
        print("nr\tdone\ttask")
        for todo in self.todos:
            print(f"{todo.get("number")}\t{"☑" if todo.get("done", False) else "☐"}\t{todo.get("task", "")}")


def main():
    todos = todoList("inAPickle")
    todos.add_task("Make todo list app")
    todos.print_todos()
    todos.remove_task( 5)
    todos.remove_task(2)
    todos.mark_task(1)
    todos.print_todos()
    todos.write_list()

if __name__ == "__main__":
    main()