from dataclasses import dataclass
import sys

from js import console, document, pyscriptReady, window
from pyodide.ffi import to_js

@dataclass
class TodoItem():
    id: int
    task: str
    complete: bool

    next_id = 0

    @classmethod
    def get_id(cls):
        cls.next_id += 1
        return cls.next_id

    def set_status(self, status: bool):
        self.complete = status
        console.log(f"Set status. Now {repr(self)}")

    def toggle_status(self):
        self.complete = not self.complete
        console.log(f"Toggled status. Now {repr(self)}")


todo_list = list()
#createObject(create_proxy(todo_list), "todos")

def update_list(frame, event, arg):
    if event == 'call':
        prev_trace = sys._getframe().f_trace
        prev_sys_trace = sys.gettrace()
        sys._getframe().f_trace = None
        sys.settrace(None)

        window.Alpine.store('todos', to_js(todo_list))

        sys._getframe().f_trace = prev_trace
        sys.settrace(prev_sys_trace)
        return update_list

def add_todo():
    value = document.getElementById("todos-input").value
    document.getElementById("todos-input").value = ""
    todo_list.append(TodoItem(id = TodoItem.get_id(), task=value, complete=False))

    console.log(f"Added {value} to todos. List is now {todo_list}")

def complete_all():
    for t in todo_list:
        t.complete=True

sys._getframe().f_trace = update_list
sys.settrace(update_list)

document.dispatchEvent(pyscriptReady);