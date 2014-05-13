populate = function() {
    $.ajax({
       url: "http://us.battle.net/api/wow/character/winterhoof/Eilee?fields=achievements&jsonp=foo",
       dataType: 'jsonp',
       type: 'GET',
       crossDomain: true,
       success: function foo(data) { 
          $.each(data, function(index, object) {
             console.log(object);
          });
       }
    });
    //$.getJSON("http://us.battle.net/api/wow/data/character/dunemaul/Fountain", function(stuff) {
       //$.each(stuff, function() { 
          //console.log(stuff.name)
          //console.log(stuff.achievementPoints)
       //});
    //});

    //for (var i=1; i < 11; i++) {
        //var cell = document.getElementById("topic"+i.toString());
        //cell.innerHTML = i;
        //jQuery.get("cgi-bin/access.py");
        

           //$.getJSON('http://www.reddit.com/', function(data) {
               //var parsed = JSON.parse(data);
               //alert(json["title"]);
           //});
    //}
    //var newh1 = document.createElement('h1')
    //newh1.innerHTML = 'Hello World!'
    //document.getElementById("temp1").appendChild(newh1)
    //document.body.appendChild(newh1)
}

myCounter = 0
factors = function() {
    //var newList = document.createElement('ul')
    //var newp = document.getElementById("count");
    //myCounter = myCounter +1;    
    //var myVal = document.getElementById("myInt").value;
    //newItem.innerHTML = myVal;
    //newItem.style.fontSize = "25px";
    //newItem.style.color="red";
    //var ele = document.getElementById("count");
    //if (ele) {
        //while (ele.firstChild) {
	    //ele.removeChild(ele.firstChild);
	//}
    //}
	
    //var start = 2;
    //var lastInt = 0;
    //while (myVal > 1) {
        //while (myVal % start == 0) {      
	    //var newItem = document.createElement('li')
            //document.getElementById("count").appendChild(newItem)
            //myVal /= start;
            //newItem.innerHTML = start;
            //if (start != lastInt) {
                //insertItem(start, "item"+start);
            //}
           //lastInt = start;
        //}
	//start = start + 1;
    //}
}

insertItem = function(value, newListItem) {
   //var ul = document.getElementById("count");
   //var li = document.createElement("li");
   //li.innerHTML = value;
   //ul.appendChild(li);
}
