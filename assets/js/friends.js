function friend_photo_selected(p_photo_id, p_friend_id, static_url, p_ig_photo_url) {
    
    //target = "#frienddatacontainer_100";
//alert("test1");
    //$(window).animate({scrollTop: $("#frienddatacontainer_100").offset().top}, 1000);
//alert("test2"); 
      
    //alert("test");
    id = "#fivethumbscontainer_";
    id = id.concat(p_friend_id);
    //alert(id);
    $(id).children().animate({ opacity: 0 }, duration=800);
    
    newhtml = "<img src='"
    newhtml = newhtml.concat(p_ig_photo_url);
    newhtml = newhtml.concat("'></img>");
    $(id).html(newhtml);
    $(id).children().animate({ opacity: 100 });
    

};

	$(function() {
	  $('a[href*=#]:not([href=#])').click(function() {
	    if (location.pathname.replace(/^\//,'') == this.pathname.replace(/^\//,'') && location.hostname == this.hostname) {

	      var target = $(this.hash);
	      target = target.length ? target : $('[name=' + this.hash.slice(1) +']');
	      if (target.length) {
	        $('html,body').animate({
	          scrollTop: target.offset().top
	        }, 1000);
	        return false;
	      }
	    }
	  });
	});