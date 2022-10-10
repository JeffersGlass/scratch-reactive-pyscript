from js import createObject, pyscriptReady, console, window, Map
from pyodide.ffi import create_proxy, to_js

from asyncio import sleep
from datetime import datetime
import sys
from watchpoints import watch

print(datetime.now())

createObject(create_proxy(globals()), "pythonGlobals")
createObject(create_proxy(id), "pyID")

previous_globals = list()

sys.intern('call')

def update_globals(*args, **kwargs):
    if args[1] == 'call':
        prev_trace = sys._getframe().f_trace
        prev_sys_trace = sys.gettrace()
        sys._getframe().f_trace = None
        sys.settrace(None)

        global updatesCalled
        updatesCalled += 1

        current_globals = [obj for obj in globals().items() if obj[0] not in INITIAL_GLOBALS]
        global previous_globals

        if any(current != previous for current, previous in zip(sorted(current_globals), sorted(previous_globals))):
            #console.log("Found difference, updating")
            window.Alpine.store('pythonGlobals', to_js(current_globals))
            previous_globals = current_globals

        previous_globals = current_globals

        sys._getframe().f_trace = prev_trace
        sys.settrace(prev_sys_trace)
        return update_globals


INITIAL_GLOBALS = set(globals())
updatesCalled = 0 
#watch(x, callback=update_globals)

document.dispatchEvent(pyscriptReady)

sys._getframe().f_trace = update_globals
sys.settrace(update_globals)

MY_FIRST_VARIABLE = "Hello mama"
MY_NEW_VARIABLE = 2394723874329