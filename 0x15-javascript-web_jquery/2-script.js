// jQuery script that changes the color of the header tag to red
// when you click the DIV tag of class red_header

$('DIV#red_header').click(function (){
        $('header').css('color', '#FF0000');
});