// Operating System (OS) Module

const { log } = require('console')
const os = require('os')

// Info on current user
const user = os.userInfo()
// console.log(user);


// Method returns the system uptime in seconds
console.log(`The system uptime is ${os.uptime()} seconds`);

const currOs = {
    name: os.type(),
    release: os.release(),
    totalMem: os.totalmem(),
    freeMem: os.freemem(),
}

console.log(currOs);
