$(function() {
	
	//by id
	$("#first").addClass("highlight"); 
	
	// by element tag
	$("p").addClass("highlight");
	// by class
	$(".chosen").addClass("highlight");
	// combination
	$("#first,.chosen").addClass("highlight");
	//contains
	$("li:contains('three')").addClass("highlight");
	$("li:even").addClass("font1");
	
	//next,previous
	
	$("li:contains('three')").next().addClass("highlight");
	$("li:contains('three')").prev().addClass("highlight");

	//siblings,parents
	$("li:contains('three')").siblings().addClass("highlight");
	$("li:contains('three')").parent().addClass("highlight");

	$("li:nth-child(1)").addClass("font");
	// attributes
	$("p[name='mysecondpara']").addClass("font");
	
	$("p[name!='mysecondpara']").addClass("font1");
	// ANOTHER WAY FOR ABOVE IS:-
	$("p").not("[name]").addClass("font1");

	$(":header").addClass("font");
	$("p:empty").text("you seemed lonely");
	});