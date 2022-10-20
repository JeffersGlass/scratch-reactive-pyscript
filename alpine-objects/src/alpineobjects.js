import Alpine from 'alpinejs'

window.Alpine = Alpine

document.addEventListener('pyscriptReady', () => {
    console.warn('Pyscript has Started')
    Alpine.store('pythonGlobals', {
        globals: pyscript.runtime.globals, 
        id: 0,
        refresh() {
            //Must set the object to point to something else, then back to globals, to get it to refresh
            this.globals = {}
            this.globals = pyscript.runtime.globals
        }})
    Alpine.start()
    console.warn('Alpine has started')
})

document.getElementById('btn-store').addEventListener("click", () => {
    console.log(pyscript.runtime.globals.toJs())
    Alpine.store('pythonGlobals').refresh()
})