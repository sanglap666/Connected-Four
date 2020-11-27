var loc = window.location
console.log(loc)
var conn = document.getElementById("connect")
console.log(conn)


var endpoint = "ws://" + loc.host + loc.pathname

var socket = new WebSocket(endpoint)

socket.onmessage = function(e) {
    console.log("message", e)
    var data = JSON.parse(e.data)

    if (data.fromuser != user) {
        if (data.message == "connect") {
            if (confirm(data.fromuser)) {

                var send_data = {
                    "username": data.fromuser,
                    "message": "accept"
                }
                socket.send(JSON.stringify(send_data))
                var url = "http://127.0.0.1:8000/profile/" + data.fromuser
                console.log(url)
                window.location = url

            } else {
                console.log("reject")
                var send_data = {
                    "username": data.fromuser,
                    "message": "reject"
                }

                socket.send(JSON.stringify(send_data))
            }
        } else if (data.message == "accept") {

            var url = "http://127.0.0.1:8000/profile/" + data.fromuser
            console.log(url)
            window.location = url
        } else {
            alert("rejected")
        }
    }
}



socket.onopen = function(e) {
    console.log("open", e)
    conn.addEventListener("click", function(event) {
        var username = conn.getAttribute('value')

        var send_data = {
            "username": username,
            "message": "connect"
        }

        socket.send(JSON.stringify(send_data))
    })


}

socket.onclose = function(e) {
    console.log("close", e)
}

socket.onerror = function(e) {
    console.log("error", e)
}