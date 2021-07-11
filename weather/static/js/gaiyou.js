$('#animation').css('visibility','hidden');
$(window).scroll(function(){
 var windowHeight = $(window).height(),
     topWindow = $(window).scrollTop();
 $('#animation').each(function(){
  var targetPosition = $(this).offset().top;
  if(topWindow > targetPosition - windowHeight + 100){
   $(this).addClass("fadeInDown");
  }
 });
});

/*$.ajax({
    url:"http://127.0.0.1:8000/weather/%E5%8C%97%E6%B5%B7%E9%81%93%E5%B0%8F%E6%A8%BD%E5%B8%82",
    type:"POST",
    data:{'temp_yn':'temp_y', 'wind_yn':'wind_y', 'wind_d_yn':'wind_d_n', 'clouds':'clouds_n', 'times':'5'},
    dataType:"json",
    success: function(data) {
        console.log(data);
    }
})*/