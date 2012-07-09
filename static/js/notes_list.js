$(function() {
    $('#Notes').on('click', 'a[data-action="delete"]', function(event) {
        event.preventDefault();
        var $this = $(this);
        var href = this.href
        $.getJSON(href, function(data) {
            if (data.result === 'success') {
                $this.parents('li').remove();
            } else {
                console.log(data.result);
            }
        });
    });
});