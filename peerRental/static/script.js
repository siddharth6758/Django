const chatbtn = document.getElementById('chat-btn')
const msg_container = document.getElementById('messages-container')

chatbtn.addEventListener('click',()=>{
    msg_container.classList.toggle('hidden')
    if (msg_container.classList.contains('hidden') == true){
        chatbtn.innerHTML = 'Chat with Owner'
        chatbtn.style.backgroundColor = '#109EFF'
    }else{
        chatbtn.innerHTML = 'Close Chat'
        chatbtn.style.backgroundColor = '#f58080'
    }
})