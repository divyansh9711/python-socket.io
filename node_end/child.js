
const io = require('socket.io-client')
var scoket = ""
const fs = require('fs');
res = {};



async function init(nameSpace){
    scoket = io.connect('http://localhost:3002');
    console.log("socket connection established"); 
    
    scoket.on('response',(data)=>{
        res["route"] = "response";
        res["data"] = data; 
        fs.writeFile("../node_message.json",JSON.stringify(res),()=>{});
    })
}
async function emit(location,data){
    scoket.emit(location,data);
}
async function broacast(data){
    console.log("all")
}
module.exports = {
    emit: emit,
    broacast: broacast,
    init:init
}