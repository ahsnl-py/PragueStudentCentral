$(document).ready(function(){
    $(".btn1").click(function(){
    $(".input1").toggleClass("active").focus;
    $(this).toggleClass("animate");
    $(".input1").val("");
    });
  });
  
    