import Alpine from 'alpinejs'

window.Alpine = Alpine

Alpine.store('pythonGlobals', {})

document.addEventListener('pyscriptReady', () => {
    console.warn('Pyscript has run')
    Alpine.start()
})
