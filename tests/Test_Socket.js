$(document).ready(function(){
    //connect to the socket server.
    var socket = io.connect('http://' + document.domain + ':' + location.port + '');
    var numbers_received = [];

    //receive details from server
     socket.on('coinbasepro', function(msg) {
         console.log("Received number");
		 console.log(msg)
     });
});