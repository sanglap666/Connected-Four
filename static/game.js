var loc = window.location
console.log(loc)
var conn = document.getElementById("connect")
console.log(conn)


var endpoint = "ws://" + loc.host + loc.pathname

var socket = new WebSocket(endpoint)

socket.onmessage = function(e) {
    console.log("message", e)
    var data = JSON.parse(e.data)

}



socket.onopen = function(e) {
    console.log("open", e)


}

socket.onclose = function(e) {
    console.log("close", e)
}

socket.onerror = function(e) {
    console.log("error", e)
}