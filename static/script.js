console.log("script loaded");
function sendMessage() {
    let input = document.getElementById("userInput");
    let message = input.value.trim();

    if (message === "") return;

    let chatArea = document.getElementById("chatArea");

    // USER MESSAGE (bubble style)
    let userDiv = document.createElement("div");
    userDiv.className = "message user";
    userDiv.innerText = message;
    chatArea.appendChild(userDiv);

    input.value = "";

    // SEND TO FLASK
    fetch("/chat", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ message: message })
    })
    .then(res => res.json())
    .then(data => {

    let typingDiv = document.createElement("div");
    typingDiv.className = "message bot";
    typingDiv.innerHTML =
        '<img src="/static/bot.png" class="typing-logo"> ...'

    chatArea.appendChild(typingDiv);
    chatArea.scrollTop = chatArea.scrollHeight;

    setTimeout(() => {

        typingDiv.innerText = data.reply;

        chatArea.scrollTop = chatArea.scrollHeight;

    }, 1500);

});
}