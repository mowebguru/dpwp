// A $( document ).ready() block.
$( document ).ready(function() {

    //Display the alert message for 5 seconds and fadeout
    $('.message').fadeIn().delay(5000).fadeOut();
    $('.message2').fadeIn().delay(5000).fadeOut();
// toggle the client form
    $('.addclient').click(function () {

        $('#contactform').toggle();


    });
$('#fname').focus()
//pop-up the delete alert

    $('.buttonx').click(function () {
        return window.confirm(this.title || 'Do you want to delete this client?');
    })

});
