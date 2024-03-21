const chatbtn = document.getElementById('chat-btn')
const msg_container = document.getElementById('messages-container')

chatbtn.addEventListener('click', () => {
    msg_container.classList.toggle('hidden')
    if (msg_container.classList.contains('hidden') == true) {
        chatbtn.innerHTML = 'Chat with Owner'
        chatbtn.style.backgroundColor = '#109EFF'
        localStorage.setItem('chatisopen',false)
    } else {
        chatbtn.innerHTML = 'Close Chat'
        chatbtn.style.backgroundColor = '#f58080'
        localStorage.setItem('chatisopen',true)
    }
})

window.onload = () => {
    isopen = localStorage.getItem('chatisopen') === 'true'
    if(isopen){
        msg_container.classList.toggle('hidden')
        chatbtn.innerHTML = 'Close Chat'
        chatbtn.style.backgroundColor = '#f58080'
    }
}