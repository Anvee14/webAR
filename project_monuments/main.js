let latitude = 22.7868542
let longitude = 88.3643296
//initializing mapbox
mapboxgl.accessToken = "pk.eyJ1IjoiYW52dmVlc2hhcm1hIiwiYSI6ImNsMTdlMTZiczEzZnczYnF6MWtpdTJsbXYifQ.XY5wZlnWuAys0ax-etA0xQ";
var map = new mapboxgl.Map({
    container: 'map',
    style: 'mapbox://styles/mapbox/streets-v11',
    center:[longitude,latitude],
    zoom : 4
})
map.addControl(
	new MapboxGeocoder({
		accessToken: mapboxgl.accessToken,
		mapboxgl: mapboxgl
	})
);


var img1 = document.querySelector("#qm")
var marker1 = new mapboxgl.Marker({
	element: img1
})
	.setLngLat([77.1855, 28.5245])
	.addTo(map);

var img2 = document.querySelector("#goi")
var marker2 = new mapboxgl.Marker({
	element: img2
})
	.setLngLat([72.835163, 18.920180])
	.addTo(map);