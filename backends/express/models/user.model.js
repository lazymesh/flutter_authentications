const mongoose = require('mongoose')
const Schema = mongoose.Schema

const newSchema = new Schema({
    email:String,
    password:String
}, {collection: 'express_users'})

module.exports = mongoose.model('express', newSchema)