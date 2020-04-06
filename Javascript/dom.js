window.onload= function() {
var clickmebutton = document.getElementById("clickme");
clickmebutton.onclick= example;
}

function runtheexample() {
alert("running the example");
}


function example() {
 var myelement= document.getElementById("second");

 var mynodename=myelement.nodeName;
	alert(mynodename);

	if(myelement != null)
	alert(myelement.innerHTML);

	document.getElementById("second").innerHTML="see how test looks";


	var listofpara=document.getElementsByTagName("p");

	alert(listofpara.length);

	var secondpara=listofpara[1];
     alert(secondpara.innerHTML); 

	myelement1=document.getElementById("second");
	alert(myelement1.parentNode.nodeName);

	alert(myelement1.childNodes[0]);
	myelement1.firstChild;
	myelement1.lastChild;

	myelement1.previousSibling;
	myelement1.nextSibling;

	var anchor=document.getElementById("anchor");
	var anchordest=anchor.href;
	alert(anchordest);

	anchor.href = "http://www.google.com" ;

	anchor.setAttribute("href","http://www.quora.com");
	 var x=anchor.getAttribute("href");
	alert(x);

	}


	