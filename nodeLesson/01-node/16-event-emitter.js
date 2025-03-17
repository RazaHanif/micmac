// Events 
// on - listen for an event
// emit - emit an event

const EventEimmiter = require('events')

const customerEmitter = new EventEimmiter()

customerEmitter.on('response', () => {
    console.log(`data recived `);
    
})

customerEmitter.emit('response')