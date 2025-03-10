// CommonJS, every file is module (by default)
// Modules - Encapsulated Code (only share minimum)

const john = 'John'
const peter = 'Peter'

const sayHi = (name) => {
    console.log(`Hello there ${name}`)
}


sayHi('Susan')
sayHi(john)
sayHi(peter)