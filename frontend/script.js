
var xmlHttp = new XMLHttpRequest();
xmlHttp.open( "POST", "http://127.0.0.1:5000"); // false for synchronous request
xmlHttp.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
xmlHttp.addEventListener("load", () => {
    document.querySelector("#text").innerHTML = xmlHttp.responseText
})
xmlHttp.send(JSON.stringify({"data": "Time"}));


