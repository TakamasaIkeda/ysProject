//TODO:http://pinoyuki.hatenablog.com/entry/2012/03/26/011922 を参考に動的な読み込みを行う
//TODO: 動的読み込み -> 動的読み込み&カスタムアイコン -> XML追記をpythonから
var map;
var lat_array = [];
var lng_array = [];
var status_array = [];
var marker_length = 0;
  
var icons = {
  icon_danger: "images/danger.png",
  icon_alert: "images/alert.png",
  icon_safe: "images/safety.png"
}

//Reading XML file by Ajax
$(function(){
  $.ajax({
    url:"data.xml",
    async: true,
    cache: false,
    dataType: "xml",
    error: function(){
      console.log('ERROR loading XML'); 
    }, 
    success: function(xml){
      $(xml).find('marker').each(function(i){
        marker_length++;      
         var lat = $(this).find('lat').text();  
         var lng = $(this).find('lng').text();  
         var safety = $(this).find('status').text();  
         lat_array.unshift(lat);
         lng_array.unshift(lng);
         status_array.unshift(safety);
      });  
      initMap(); 
    } 
  }); 
}); 

//google map
function initMap(data){
  var opts = {
    center: {lat: 35.5554176, lng: 139.6515138},
    zoom : 12
  }
  map = new google.maps.Map(document.getElementById('map'), opts); 
  setMarkers(map); 
}

//Marker Option
function setMarkers(map) {
  var image_safe = {
    url: icons.icon_safe,
    size: new google.maps.Size(200, 200),
    origin: new google.maps.Point(0, 0),
    anchor: new google.maps.Point(0, 32) 
  };
  var image_alert = {
    url: icons.icon_alert,
    size: new google.maps.Size(300, 200),
    origin: new google.maps.Point(0, 0),
    anchor: new google.maps.Point(0, 32) 
  };
  var image_danger = {
    url: icons.icon_danger,
    size: new google.maps.Size(300,200),
    origin: new google.maps.Point(0, 0),
    anchor: new google.maps.Point(0, 32) 
  };
  var shape = {
    coords: [1, 1, 1, 20, 18, 20, 18, 1],
    type: 'poly'
  };

  var image;
  for(var i=0; i<=marker_length; i++) {
    switch(status_array[i]){
      case '0':
        image = image_safe;
        break;
      case '1':
        image = image_alert;
        break;
      case '2':
        image = image_danger;
        break;
    } 

    console.log("image:" + image); 

    latlng = {lat: Number(lat_array[i]), lng: Number(lng_array[i])}
    var marker = new google.maps.Marker({
      position: latlng,
      map: map,
      icon: image,
      shape: shape,
      title: status_array[i]
    }); 
  } 
}


//  console.log("status_aaray:" + status_array); 
//  var latlng;
//  var image;
//  //iconとxmlの<status>タグの紐付け
//  for(var i = 0; i <= marker_length; i++){
//    if (status_array = "danger"){
//     image = icons.icon_danger; 
//     console.log("image danger" + status_array); 
//    }else if(status_array[i] = "alert"){
//     image = icons.icon_alert;
//     console.log("image alert" + status_array); 
//    }else if(status_array[i] = "safe"){
//     image = icons.icon_safe;
//     console.log("image safe" + status_array); 
//    } else {
//     console.log("ICON:Nothing is correct"); 
//    } 
//    
//    //var image = {
//    //  url: ,
//    //  size: new google.maps.Size(20, 32), 
//    //}
//    
//    latlng = {lat: Number(lat_array[i]), lng: Number(lng_array[i])}
//
//    //var marker = new google.maps.Marker({
//    //  position: latlng,
//    //  map: map,
//    //  title: 'EarthQuaker',
//    //});
//  }
//} 

