from js import console, document, Event
console.log("PyScript loaded")

pyscriptReady = Event.new('pyscriptReady')

document.dispatchEvent(pyscriptReady);