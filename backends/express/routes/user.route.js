const express = require('express')
const User = require('../models/user.model')
const router = express.Router()


router.post('/signup',(req,res)=>{
    User.findOne({email:req.body.email},(err,user)=>{
        if(err){
            res.json(err)
        }else{
            if(user==null){
                
                const user = User({
                    email:req.body.email,
                    password:req.body.password
                })
                
                user.save()
                .then((data)=>{
                    if(!data){
                        res.json(err)
                    }else{
                        res.json(user)
                    }
                    
                })
            }else{
                res.json({
                    message:'email is not avilable'
                })   
            }
        }
    })
    
})

router.post('/signin',(req,res)=>{
    User.findOne({email:req.body.email,password:req.body.password},(err,user)=>{
        if(err){
            res.json(err)
        }else{
            res.json(user)   
        }
    })
})
module.exports = router