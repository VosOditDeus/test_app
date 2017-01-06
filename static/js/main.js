/**
 * Created by vosoditdeus on 1/5/17.
 */
$('#chat-form').on('submit', function (event) {
    event.preventDefault();

    $.ajax({
        url: '/post/',
        type: 'POST',
        data: {msgbox: $('#chat').val()},

        success: function (json) {
            $('#chat').val('');
            $('#message-list').append('<div class="panel panel-default text-right"><div class="panel-heading">' +
                json.user+'</div><div> ' + json.message + ' </div></div > ');
            var chatlist = document.getElementById('message-list-div');
            chatlist.scrollTop = chatlist.scrollHeight;
        }
    });
});

function getMessages() {
    if (!scrolling) {
        $.get('/messages/', function (messages) {
            $('#message-list').html(messages);
            var chatlist = document.getElementById('message-list-div');
            chatlist.scrollTop = chatlist.scrollHeight;
        });
    }
    scrolling = false;
}

var scrolling = false;
$(function () {
    $('#message-list-div').on('scroll', function () {
        scrolling = true;
    });
    refreshTimer = setInterval(getMessages, 5000);
});

$(document).ready(function () {
    $('#send').attr('disabled', 'disabled');
    $('#chat').keyup(function () {
        if ($(this).val() != '') {
            $('#send').removeAttr('disabled');
        }
        else {
            $('#send').attr('disabled', 'disabled');
        }
    });
});

// using jQuery
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
var csrftoken = getCookie('csrftoken');

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
$.ajaxSetup({
    beforeSend: function (xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});