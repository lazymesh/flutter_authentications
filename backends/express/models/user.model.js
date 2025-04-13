const mongoose = require('mongoose')
const Schema = mongoose.Schema

const newSchema = new Schema({
    email:String,
    password:String
})
console.log(mongoose.connections)
module.exports = mongoose.model('express', newSchema)