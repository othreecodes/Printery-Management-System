var ContactPage = function () {

    // Return
    return {

    	//Basic Map
      initMap: function () {
  			var map;
  			$(document).ready(function(){
  			  map = new GMaps({
    				div: '#map',
    				scrollwheel: false,
    				lat: 40.748866,
    				lng: -73.988366
  		    });

  			  var marker = map.addMarker({
    				lat: 40.748866,
    				lng: -73.988366,
            title: 'Company, Inc.'
          });
			 });
      },
      // End Basic Map

      // Panorama Map
      initPanorama: function () {
  	    var panorama;
  	    $(document).ready(function(){
  	      panorama = GMaps.createPanorama({
  	        el: '#panorama',
  	        lat : 40.748866,
  	        lng : -73.988366
  	      });
  	    });
  		}
      // End Panorama Map

    };
    // End Return

}();