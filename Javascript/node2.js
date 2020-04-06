var http=require("http");

var server=http.createServer(function (request,response) {
	response.writeHead(200,{"content-Type":"text/plain"});
	resonse.end("hello worlds\n");

});

server.listen(7000);