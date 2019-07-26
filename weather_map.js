var ourLoc;
var view;
var map;

// Step 3: We should initalize our variables!
function init() {
	// Initalize things here
	ourLoc = ol.proj.fromLonLat([41.043316, 28.862457]);

	view = new ol.View({
		center: ourLoc,
		zoom: 6 // Students can play around with the starting zoom.
	});

	map = new ol.Map({
		target: 'map', // The "Target" is our <div> name.
		layers: [
		  new ol.layer.Tile({
		    source: new ol.source.OSM() // Explain: this is a required variable.
		  })
		  // Explain: Open Layer offers different types of layers. Layers are like
		  // different brushes used to make the same image. They look different.
		  // Some might take more time than others.
		],
		// Note from the View Animation website:
		// Improve user experience by loading tiles while animating. Will make
		// animations stutter on mobile or slow devices.
		loadTilesWhileAnimating: true,
		view: view
	});
}

function panHome(){
  view.animate({center: ourLoc, duration: 2000});
}

function panToLocation(){
  var countryName = document.getElementById("country-name").value;

  if(countryName === ""){
    alert("You didn't enter a country name!!!");
    return;
  }

  var query = "https://restcountries.eu/rest/v2/name/" + countryName;

  query = query.replace(/ /g, "%20");
  // alert(query);


  var countryRequest = new XMLHttpRequest();
  countryRequest.open('GET', query, false);

  countryRequest.send();

  if(countryRequest.readyState != 4 || countryRequest.status != 200 || countryRequest.responseText === ""){
    window.console.error("Request had an error!")
  }

  var countryInformation = JSON.parse(countryRequest.responseText);

  // alert("Ready State" + countryRequest.readyState);
  // alert("Status" + countryRequest.status);
  // alert("Response" + countryRequest.reponseText);

  var lon = countryInformation[0].latlng[1];
  var lat = countryInformation[0].latlng[0];
  var location = ol.proj.fromLonLat([lon, lat]);

  view.animate({center: location, duration: 2000});
}

// Step 4: We can run the init function when the window loads.
window.onload = init;
