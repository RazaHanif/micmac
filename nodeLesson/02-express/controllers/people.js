let { people } = require('../data.js')

const getPeople = (req, res) => {
    res.status(200).json({
        success:true,
        data:people
    })
}

const createPerson = (req, res) => {
    const { name } = req.body

    if (!name) {
        return res.status(400).json({
            success:false,
            msg:'Name Not Found!'
        })
    }

    res.status(201).send({
        success: true,
        person: name
    })
}

const createPersonPostman = (req, res) => {
    const {name} = req.body

    if (!name) {
        return res.status(400).json({
            success:false,
             msg:'Name Not Found!'
         })
    }
    res.status(201).send({
        success:true,
        data: [...people, name] 
    })
}

const updatePerson = (req, res) => {
    const { id } = req.params
    const { name } = req.body

    const person = people.find((person) => person.id === Number(id))
    
    if (!person) {
        return res.status(404).json({
            success: false,
            msg: `No person with id ${id}`
        })
    }
    
    // Temp logic cuz no db
    if (!name) {
        return res.status(200).json(person)
    }
    person.name = name
    res.status(200).json(person)
}

const deletePerson = (req, res) => {
    const { id } = req.params

    const person = people.find((person) => person.id === Number(id))

    if (!person) {
        return res.status(404).json({
            success: false,
            msg: `No person with id ${id}`
        })
    }
    
    const newPeople = people.filter((person) => person.id !== Number(id))

    res.status(200).json({
        success: true,
        data: newPeople
    })
}

module.exports = {
    getPeople,
    createPerson,
    createPersonPostman,
    updatePerson,
    deletePerson
}