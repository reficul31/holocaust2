$(document).ready(function() {

	$('#create').on("click",function(){
	    var url= "/make/event"
	    $.ajax({
	      url: url,
	      success: function(data){
	           $('.container').html(data);
	      }
	    });
	});

	$('.verify').on("click",function() {
	    var url= "/verify/"+ this.id; 
	    $.ajax({
	      url: url,
	      success: function(data){
	           $('.container').html(data);
	      }
	    });
	});

	$('.view').on("click",function() {
	    var url= "/view/" + this.id;
	    $.ajax({
	      url: url,
	      success: function(data){
	           $('.container').html(data);
	      }
	    });
	});
});