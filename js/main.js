$(document).ready(function(){

	//fancybox.js init
	$('.fancybox').fancybox({
		openEffect : 'none',
		closeEffect : 'none',
		prevEffect : 'none',
		nextEffect : 'none',

		arrows : false,
		helpers : {
			media : {},
			buttons : {}
		}
	});

//client.js
	$('.message').fadeIn().delay(3000).fadeOut();
	$('.message2').fadeIn().delay(3000).fadeOut();

	// Pop-up the Delete window alert

	$('.buttonX').click(function () {
		return windows.confirm(this.title || 'Do you want to delete this client?');

	});

	//Toggles Add form based on button clicks

	$('.addclient').click(function () {

		$('#contactform').toggle();

	});
	//wow.js init
	wow = new WOW(
	    {
		  animateClass: 'animated',
		  mobile: false,
		  offset: 100
		}
	);
	wow.init();

});

