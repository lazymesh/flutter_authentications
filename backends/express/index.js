const express = require('express')
const dotenv = require('dotenv')
const app = express()
const port = 8080 || process.env.PORT
const cors = require('cors')
const bodyParser = require('body-parser')
const mongoose = require('mongoose')


dotenv.config()
const dbUser = process.env.MONGODB_USER
const dbPassword = process.env.MONGODB_PASSWORD
const dbUri = process.env.MONGODB_URI
const dbCluster = process.env.MONGODB_CLUSTER
const db = process.env.MONGODB_DATABASE
const uri = `mongodb+srv://${dbUser}:${dbPassword}@${dbUri}/${db}?appName=${dbCluster}`;
const clientOptions = { useNewUrlParser: true, useUnifiedTopology: true };

mongoose.connect(uri, clientOptions)

app.use(cors())
app.use(bodyParser.urlencoded({extended:true}))
app.use(bodyParser.json())
app.use('/',require('./routes/user.route'))
app.listen(port,()=>{
    console.log('port running on '+port)
})