//objects
var batwing = {
	status:"ready",    //, operator seperator one properties from another
	rescuebatman: function() {
	document.write("loading his transponder.....initiaing launch...");
	}
		}
	
	if(batwing.status==="ready");                 //.operator is used to access the member
	batwing.rescuebatman();

	var utilities={
	printallmembers:function(targetobject) {
  	for(var i in targetobject) {
	document.write(targetobject[i]);
	}
	}
	}

	utilities.printallmembers(batwing);
	
	var empty={ };
	
	utilities.printallmembers(empty);

	var planet={
	id: 34,
	name: "sanskar",
	faction: {
                    factionid:3,
			name:"adi",
			notification: function() {
		document.write("unite");
	
}
},
	cities: [
	{ locationid: 15,name:"sam"},
	{ locationid: 16,name:"hrishab"},
	{ locationid: 17,name:"divyansh"}
	]
}

planet.faction.notification();
document.write(planet.cities[1].name);

document.write("<br/>"+planet.name);
planet.name="vultus";

document.write(planet.name);

var z=planet;

document.write(z.name);
document.write(z.cities);

if(typeof planet.defense==="undefined") {
	planet.defense="iron canon";
}

planet.temp="4000";
document.write(planet.defense);
var member;   //instead of member i,j,k..... anything can be used
for(member in planet)
document.write("<br/>"+ member+ " "+ planet[member]);

function car(make,model,year) {
    this.make=make;
	this.model=model;
	this.year=year;
}

var mycar=new car("eagle","talon tsi",1993);
var myothercar=new car("wagonr","vxi",2009);

alert(mycar.model);
alert(myothercar.year);

