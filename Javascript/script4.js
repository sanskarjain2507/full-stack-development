$(function() {


	$("#success").hide();
	$("#startover").addClass("hoverout");
	var score=0;
	$("#bobhead").click(function() {
	score++;
	$("#score").text(score);
	$("#success").show("fast").fadeOut(2000);
});

	$("#startover").hover(function() {
	score=0;
	$("#score").text(score);
	$("#startover").addClass("hoverin").removeClass("hoverout");
	}, function() {
	$("#startover").addClass("hoverout").removeClass("hoverin");
	
	
	
	});
	
});