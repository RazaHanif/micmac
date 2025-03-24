const Job = require('../models/Job')
const { StatusCodes } = require('http-status-codes')
const { BadRequestError, NotFoundError } = require('../errors') 

const getAllJobs = async (req, res) => {
    res.json({msg: 'get All Jobs'});
    
}

const getThisJob = async (req, res) => {
    res.json({msg: 'get This Job'});
    
}

const createJob = async (req, res) => {
    req.body.createdBy = req.user.userId
    const job = await Job.create(req.body)
    res.status(StatusCodes.CREATED).json({job})
    
}

const updateJob = async (req, res) => {
    res.json({msg: 'update Job'});
    
}

const deleteJob = async (req, res) => {
    res.json({msg: 'delete Job'});
    
}


module.exports = {
    getAllJobs,
    getThisJob,
    createJob,
    updateJob,
    deleteJob
}