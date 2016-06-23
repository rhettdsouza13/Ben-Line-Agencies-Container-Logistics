function switchForm(){
  // Switches the Icon  
  $('.form').animate({
    height: "toggle",
    'padding-top': 'toggle',
    'padding-bottom': 'toggle',
    opacity: "toggle"
  }, "slow");
};

$('.nav-btn-form').click(function() {
	if(!$(this).hasClass('active')) {
		switchForm();
		$(this).siblings().removeClass('active');
		$(this).addClass('active');
		  $("#change").html("<h1>Welcome</h1>");
	}
});