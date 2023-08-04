// jQuery script that append a new <li> element with text 'Item'
// to the Ul element with class my_list

$('DIV#add_item').click(function (){
    $('UL.my_list').append('<li>Item</li>');
});