document.addEventListener('DOMContentLoaded', () => {

    const submit = document.querySelector('#submit')
    const task = document.querySelector('#task')
    const list = document.querySelector('#tasks')
    
    submit.disabled = true
    task.onkeyup = () => {
        if (task.value.length > 0) {
            submit.disabled = false
        } else {
            submit.disabled = true
        }
    }

    document.querySelector('form').onsubmit = () => {
        const text = task.value
        const li = document.createElement('li')

        li.innerHTML = text        
        list.append(li)
        task.value = ''

        //stop form from submiting
        return false
    }
})