let coordinates = {}
$(document).ready(function(){
    get_coordinates();
})
function get_coordinates(){
    var searchParam = new URLSearchParams(window.location.search)
    if(searchParam.has('source')&&searchParam.has('destination')){
        var source = searchParam.get('source')
        var destination = searchParam.get('destination')
        coordinates.source_lat = source.split(";")[0]
        coordinates.source_lon = source.split(";")[1]
        coordinates.destination_lat = destination.split(";")[0]
        coordinates.destination_lon = destination.split(";")[1]
    }else{
        alert("coordinates not selected")
        window.history.back()
    }
}