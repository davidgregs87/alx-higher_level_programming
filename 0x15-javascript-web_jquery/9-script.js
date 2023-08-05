// A jQuery script that fetches data from a URL and prints it out on the html page

$(() => {
    $.getJSON('https://fourtonfish.com/hellosalut/?lang=fr', (data, textStatus) => {
        if (textStatus === 'success') {
            $('DIV#hello').text(data.hello);
        }
    });
});