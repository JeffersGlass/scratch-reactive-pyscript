import Alpine from 'alpinejs'

window.Alpine = Alpine

Alpine.store('todos', {})

document.addEventListener('pyscriptReady', () => {
    console.warn('Pyscript has run')
    Alpine.start()
    console.warn('Alpine has started')
})
