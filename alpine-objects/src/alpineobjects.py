from js import console, document, Event, Alpine
import sys
console.log("PyScript loaded")

def setRefresh():
    console.log(dir(sys._getframe()))
    sys._getframe().f_trace = Alpine.store('pythonGlobals').refresh
    sys.settrace(Alpine.store('pythonGlobals').refresh)
    console.warn("System Traces set in python")

console.log("Sending pyscriptReady event")
pyscriptReady = Event.new('pyscriptReady')
document.dispatchEvent(pyscriptReady);