$(function() {
    $('#Editor textarea').on('focus', function() {
        $('#Toolbar span').text('正在编写...');
    });
    
    $("#Toolbar ul").on('click', 'a', function(event) {
        event.preventDefault();
        var target = event.target;
        var action = $(target).attr('data-action');
        var href = target.href;
        
        switch (action) {
            case 'save':
                {
                    var $form = $('form');
                    var url = $form.attr('action');
                    var data = $form.serialize();
                    // console.log(data);
                    $.post(url, data, function(note) {
                        $('#Toolbar span').text('保存于 ' + note.fields.time);
                    //console.log(note.pk);
                    }, 'json');
                    break;
                }
            case 'update':
                {
                    console.log('update');
                    break;
                }
            case 'delete':
                {
                    console.log('delete');
                    break;
                }
            case 'share':
                {
                    console.log('share');
                    break;
                }
            default:
                {
                    // location.pathname = url;
                    location.href = href;
                    console.log('no action');
                }
        }
    });
});