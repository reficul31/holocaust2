var formdata=[];

$(document).ready(function() {
	$('#adduser').click(function() {
			$(".wrapper").toggle();
	});

	$( "#registerform" ).submit(function( event ) {
		var obj = {}
	  	$.each($( this ).serializeArray() , function(k,v){ 	
	  	obj[v.name]=v.value;
	  });

		event.preventDefault();
		formdata=JSON.stringify(obj);
		document.getElementById('sender').value= formdata;
		$("#senderform").submit();
	});
});
