function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrftoken = getCookie('csrftoken');


jQuery(document).ready(function() {

    $(".chat-list a").click(function() {
        $(".chatbox").addClass('showbox');
        return false;
    });

    $(".chat-icon").click(function() {
        $(".chatbox").removeClass('showbox');
    });


});




(function($) {
    $(document).ready(function() {
        var $chatbox = $('.chatbox'),
            $chatboxTitle = $('.chatbox__title'),
            $chatboxTitleClose = $('.chatbox__title__close'),
            $chatboxCredentials = $('.chatbox__credentials');
        $chatboxTitle.on('click', function() {
            $chatbox.toggleClass('chatbox--tray');
        });
        $chatboxTitleClose.on('click', function(e) {
            e.stopPropagation();
            $chatbox.addClass('chatbox--closed');
        });
        $chatbox.on('transitionend', function() {
            if ($chatbox.hasClass('chatbox--closed')) $chatbox.remove();
        });
        
    });
})(jQuery);



var msg_count = parseInt(document.getElementById('initial-msg-count').value);

function createChatMessageBox(message, isSent) {
    let chatMessageBox = document.createElement("div");
    chatMessageBox.classList.add("chat-bubble", "text-box", isSent ? "chat-bubble--right" : "chat-bubble--left");
    chatMessageBox.innerText = message;
    return chatMessageBox;
}

var chatform = document.getElementById("chatform");

chatform.addEventListener("submit", sendMessage);

function sendMessage(e) {
    e.preventDefault();

    let chatMessage = document.getElementById("message").value;
    var absoluteUrl = document.getElementById('absolute-url-input').value;
    let msg_url = absoluteUrl;

    async function postJSON(data) {
        try {
            const response = await fetch(msg_url, {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                    "X-CSRFToken": csrftoken,
                },
                body: JSON.stringify(data),
            });

            const result = await response.json();
            let chatMessageBox = createChatMessageBox(result, true);

            let newChatBox = document.createElement("div");
            newChatBox.classList.add("col-md-6", "offset-md-6");
            newChatBox.appendChild(chatMessageBox);

            let chatPanel = document.getElementById("chat-panel");
            chatPanel.appendChild(newChatBox);

            document.getElementById('message').value = '';
            msg_count += 1;
        } catch (error) {
            console.error("Error:", error);
        }
    }

    const data = { msg: chatMessage };
    postJSON(data);
}

setInterval(receiveMessage, 3000);

function receiveMessage() {
    var rece_absoluteUrl = document.getElementById('rece-absolute-url-input').value;
    let rece_msg_url = rece_absoluteUrl;

    async function getJSON() {
        try {
            const response = await fetch(rece_msg_url);
            const result = await response.json();
            
            if (result.length > msg_count) {
                let lastmsg = result[result.length - 1];
                let chatMessageBoxrRece = createChatMessageBox(lastmsg, false);

                let newChatBoxREce = document.createElement("div");
                newChatBoxREce.classList.add("col-md-6");
                newChatBoxREce.appendChild(chatMessageBoxrRece);

                let chatPanel = document.getElementById("chat-panel");
                chatPanel.appendChild(newChatBoxREce);

                msg_count = result.length;
            }
        } catch (error) {
            console.error("Error:", error);
        }
    }

    getJSON();
}


function getNotifications(){

    var absoluteUrl_not = document.getElementById('notification').value;
    let not_url = absoluteUrl_not;

    fetch(not_url)
    .then(res=> res.json())
    .then(data=>{
        console.log(data)
    })
    .catch(error=> console.log(error))
    
}