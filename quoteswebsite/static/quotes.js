(function quotes() {
    $.getJSON("/api/quote", function(quote){
            $("#quote").text(quote.quote);
            $("#author").text("- " + quote.author);
            $("#permalink_input").val("https://" + window.location.hostname + "/quote/" + quote.id);

            $("#permalink_button").click(function () {
                input = $("#permalink_input");
                input.select();
                document.execCommand("copy");
            });
    });
})();