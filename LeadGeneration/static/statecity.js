$(document).ready(function(){
    $.getJSON("http://localhost:8000/api/statelist",function(data){
     
        data.map((item)=>{
        $('#state').append($('<option>').text(item.statename).val(item.stateid))

        }) 
     
    })
$('#state').change(function(){

    $.getJSON("http://localhost:8000/api/citylist",{"stateid":$('#state').val()},function(data){
    $('#city').empty()
    $('#city').append($('<option>').text('Choose City...'))
    data.map((item)=>{
    $('#city').append($('<option>').text(item.cityname).val(item.cityid))

    }) 
 
})
}) 
$.getJSON("http://localhost:8000/api/managerlist",function(data){
     
        data.map((item)=>{
        $('#managerid').append($('<option>').text(item.managerid).val(item.managerid))

        }) 
     
    })
})