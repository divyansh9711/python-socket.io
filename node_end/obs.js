var fs = require("fs");
var child = require("./child")
initObs();
var data = {}
var connected = false;
function initObs() {
    fs.watchFile('../python_message.txt', (curr, prev) => {
        createRequest();
    });
}
function createRequest() {
    console.log("Reading request")
    fs.readFile('../python_message.txt', (err, res) => {
        var data = JSON.parse(res);
        switch (data.requestType) {
            case "init":
                child.init(data["nameSpace"]);
                connected = true;
                break;
            case "emit":
                checkConnection();
                child.emit(data.route, data.data);
                break;
            case "disconnect":
                checkConnection();
                child.emit(requestData.route, requestData.data);
                break;
            case "broadcast":
                checkConnection();
                child.broacast(data.data);
                break;
        }

    })
}

function checkConnection(){
    if(!connected){
        console.log("Connection not detected, Connecting to socket")
        child.init(data["nameSpace"]);
        connected = true;
    }
}