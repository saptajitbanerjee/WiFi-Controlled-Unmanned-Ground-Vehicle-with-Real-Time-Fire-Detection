const AWS = require("aws-sdk");

// AWS IoT Configurations
const iotData = new AWS.IotData({
    endpoint: "ahqreojupl1kh-ats.iot.ap-south-1.amazonaws.com",
    region: "ap-south-1", // Replace with your desired AWS region
    //apiVersion: '2015-05-28',
    credentials: {
        accessKeyId: "AKIATNYGUNULOGNRE4M6",
        secretAccessKey: "/NBkI/Djkcvs6IH+xXPv9fP8y5FDJ/hmEKooYaCt",
    },
});

// Publish a message to a MQTT topic
const publishMessage = (topic, message) => {
    const params = {
        topic,
        payload: JSON.stringify(message),
        qos: 0, // Change the Quality of Service (QoS) level if needed (0, 1, or 2)
    };

    iotData.publish(params, (err, data) => {
        if (err) {
            console.error("Error publishing message:", err);
        } else {
            console.log("Message published successfully:", data);
        }
    });
};

// Usage example:
const topic = "esp32/sub"; // Replace with your desired topic

document.onkeydown = checkKey;
let pressed_up = false;
let pressed_down = false;
let pressed_left = false;
let pressed_right = false;

function forward_event() {
    message = { message: "forward" };
    console.log("Forward")
    publishMessage(topic, message);
}

function reverse_event() {
    message = { message: "reverse" };
    publishMessage(topic, message);
}

function left_event() {
    message = { message: "left" };
    publishMessage(topic, message);
}

function right_event() {
    message = { message: "right" };
    publishMessage(topic, message);
}

function stop() {
    message = { message: "stop" };
    console.log("Stop")
    publishMessage(topic, message);
}

const forward = document.getElementById("forward");
forward.addEventListener("mousedown", forward_event);
forward.addEventListener("mouseup", stop);

const reverse = document.getElementById("reverse");
reverse.addEventListener("mousedown", reverse_event);
reverse.addEventListener("mouseup", stop)

const left = document.getElementById("left");
left.addEventListener("mousedown", left_event);
left.addEventListener("mouseup", stop);

const right = document.getElementById("right");
right.addEventListener("click", right_event);
right.addEventListener("mouseup", stop);

function checkKey(e) {
    e = e || window.event;
    if (e.keyCode == "38" && !pressed_up) {
        // up arrow
        console.log("Forward");
        pressed_up = true;
        pressed_down = false;
        pressed_left = false;
        pressed_right = false;
        //httpGetAsync('http://192.168.94.45:8010/forward', {})
        forward_event();
    } else if (e.keyCode == "40" && !pressed_down) {
        // down arrow
        console.log("Reverse");
        pressed_up = false;
        pressed_down = true;
        pressed_left = false;
        pressed_right = false;
        //httpGetAsync("http://192.168.94.45:8010/reverse", {});
        reverse_event();
    } else if (e.keyCode == "37" && !pressed_left) {
        // left arrow
        console.log("Left");
        pressed_up = false;
        pressed_down = false;
        pressed_left = true;
        pressed_right = false;
        //httpGetAsync("http://192.168.94.45:8010/left", {});
        left_event();
    } else if (e.keyCode == "39" && !pressed_right) {
        // right arrow
        console.log("Right");
        pressed_up = false;
        pressed_down = false;
        pressed_left = false;
        pressed_right = true;
        //httpGetAsync("http://192.168.94.45:8010/right", {});
        right_event();
    }
}
document.addEventListener("keyup", (event) => {
    console.log("Stop Event");
    pressed_up = false;
    pressed_down = false;
    pressed_left = false;
    pressed_right = false;
    //httpGetAsync("http://192.168.94.45:8010/stop", {});
    stop();
});

/*
function httpGetAsync(theUrl, callback) {
  var xmlHttp = new XMLHttpRequest();
  xmlHttp.onreadystatechange = function () {
    if (xmlHttp.readyState == 4 && xmlHttp.status == 200)
      callback(xmlHttp.responseText);
  };
  xmlHttp.open("GET", theUrl, true); // true for asynchronous
  xmlHttp.send(null);
  console.log("Successful");
}
*/
const socket = new WebSocket(
    "wss://bc8p09eijf.execute-api.ap-south-1.amazonaws.com/production"
); // Example:
("wss://3143544j.execute-api.us-east-1.amazonaws.com/production");
//function connectWebSocket() {

//const socket = new WebSocket('wss://bc8p09eijf.execute-api.ap-south-1.amazonaws.com/production') // Example:
("wss://3143544j.execute-api.us-east-1.amazonaws.com/production");
socket.addEventListener("open", (event) => {
    console.log("WebSocket is connected");
});

socket.addEventListener("close", (event) => {
    console.log("WebSocket is closed. Reconnecting...");
    socket.addEventListener("open", (event) => {
        console.log("WebSocket is connected");
    }); // Reconnect
});

socket.addEventListener("error", (event) => {
    console.error("WebSocket error:", event);
    socket.addEventListener("open", (event) => {
        console.log("WebSocket is connected");
    }); // Reconnect
    // Handle any errors that occur
});
socket.addEventListener("message", (event) => {
    let data = event.data;
    console.log("Incoming IoT Payload:"); // for JSON test event
    var IoT_Payload = JSON.parse(data);
    console.log("our json object", IoT_Payload);
    let { temperature, humidity, pressure, altitude } = IoT_Payload;
    $(document).ready(function() {
        $("#d1").text(temperature);
    });
    $(document).ready(function() {
        $("#d2").text(humidity);
    });
    $(document).ready(function() {
        $("#d3").text(pressure);
    });
    $(document).ready(function() {
        $("#d4").text(altitude);
    });
});