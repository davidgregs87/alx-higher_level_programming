// jQuery script that toggle's two classes to change the color
// of the text when clicked

$('DIV#toggle_header').click(function () {
    $('header').toggleClass('red green');
});