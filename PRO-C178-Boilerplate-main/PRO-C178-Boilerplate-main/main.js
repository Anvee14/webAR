let latitude = 22.7868542
let longitude = 88.3643296
//initializing mapbox
mapboxgl.accessToken = "pk.eyJ1IjoiYW52dmVlc2hhcm1hIiwiYSI6ImNsMTdlMTZiczEzZnczYnF6MWtpdTJsbXYifQ.XY5wZlnWuAys0ax-etA0xQ";
var map = new mapboxgl.Map({
    container: 'map',
    style: 'mapbox://styles/mapbox/streets-v11',
    center:[longitude,latitude],
    zoom : 16
})
map.addControl(
    new mapboxgl.GeolocateControl({
        positionOptions : { 
            enableHighAccuracy : true,
        },
        trackUserLocation : true
    })
)
map.addControl(
    new MapboxDirections({
        accessToken:mapboxgl.accessToken
    }),
    "top-right"
)
