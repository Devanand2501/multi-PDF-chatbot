css = '''
<style>
.chat-message {
    padding: 1.5rem; border-radius: 0.5rem; margin-bottom: 1rem; display: flex
}
.chat-message.user {
    background-color: #2b313e
}
.chat-message.bot {
    background-color: #475063
}
.chat-message .avatar {
  width: 20%;
}
.chat-message .avatar img {
  max-width: 78px;
  max-height: 78px;
  border-radius: 50%;
  object-fit: cover;
}
.chat-message .message {
  width: 80%;
  padding: 0 1.5rem;
  color: #fff;
}
'''

bot_template = '''
<div class="chat-message bot">
    <div class="avatar">
        <img src="https://static.vecteezy.com/system/resources/previews/021/640/068/non_2x/3d-bot-icon-isolated-on-white-background-3d-chatbot-business-and-technology-concept-cartoon-minimal-style-3d-chatbot-icon-render-illustration-vector.jpg" style="max-height: 78px; max-width: 78px; border-radius: 50%; object-fit: cover;">
    </div>
    <div class="message">{{MSG}}</div>
</div>
'''

user_template = '''
<div class="chat-message user">
    <div class="avatar">
        <img src="https://img.freepik.com/free-vector/businessman-working-laptop-computer-office-3d-character-isolated-white-background_40876-3756.jpg?w=900&t=st=1705064708~exp=1705065308~hmac=37b0bb7355829a2c1d6875d7ce22b18d2c68aac84df8b06c7c2666c28eba25b5">
    </div>    
    <div class="message">{{MSG}}</div>
</div>
'''