$(function() {

	$("#title").text("now h1 changes immediately");
	
	$("#first").html("<h2>great looks</h2>");
	
	// append prepend works INSIDE the given selection
	$("#first").prepend("<h2>great quotes</h2>"); //prepend writes something BEFORE

	$("#first").append("<h3>hello</h3>");
	// before,after,insertBefore,insertAfter work OUTSIDE the given selection

	$("#first").after("<h3>hii</h3>");

	$("#myanchor").attr("href","http://www.bing.com");

	$("#title").addClass("standout");
	});
	
	