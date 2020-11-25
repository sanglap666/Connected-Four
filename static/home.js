var loc = window.location
console.log(loc)
var conn = document.getElementById("connect")
console.log(conn)

var endpoint = "ws://" + loc.host + loc.pathname

var socket = new WebSocket(endpoint)

socket.onmessage = function(e) {
    console.log("message", e)
}

socket.onopen = function(e) {
    console.log("open", e)
    conn.addEventListener("click", function(event) {
        var username = conn.getAttribute('value')
        socket.send(username)
    })

}

socket.onclose = function(e) {
    console.log("close", e)
}

socket.onerror = function(e) {
    console.log("error", e)
}