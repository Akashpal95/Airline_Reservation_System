$(function() {
    $('#search-btn').click(function() {
        console.log("working");
        $.ajax({
            url: '/test',
            data: $('form').serialize(),
            dataType: 'json',
            type: 'POST',
            success: function(response) {
                    console.log(response);
                 searchResults(response);
            },
            error: function(error) {
                console.log(error);
            }
        });
    });
});

function searchResults(result) {
    var str = '';
    for (i = 0; i < result.Flight_name.length; i++) {
    if(result.Flight_name[i][0]=='S'){    
    str += '<div class="searchCard"><span><img class="cardImg" src="../static/PICS/SpiceJet.jpg" align="left"><div class="cardContent"><span><p id="block">Flight: <span>';
    }
    if(result.Flight_name[i][0]=='A'){
         str += '<div class="searchCard"><span><img class="cardImg" src="../static/PICS/AirIndia.jpg" align="left"><div class="cardContent"><span><p id="block">Flight: <span>';
    }
    str += result.Flight_name[i];
    str += '</span></p><p id="wing">Departure: <span>' + result.Departure_time[i];
    str += '</span></p><p id="floor">Arrival: <span>' + result.Arrival_time[i];
    str += '</span></p><p id="roomNo">Price: <span>' + result.Price[i];
    var str2=result.Flight_name[i];
    str += '</span></p>	<button id="btn2" type="button" onclick="check(\'' + result.Flight_name[i] + '\')"';
    str += ' >Book Now</button></span><div id="timeline" class="available"><div id="myBar" class="booked"></div></div></div></span></div>';
};

document.getElementById("cards").innerHTML = str;

document.querySelectorAll(".searchCard")[0].style.borderTop = "0px solid white";
}
var Flight_id='';
function check(i){
    console.log("it's happening");
    Flight_id=i;
    console.log(Flight_id)
    $("#myModal").modal();
}
function retroom(){
    return Flight_id;
}