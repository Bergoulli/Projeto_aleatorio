from instabot import Bot

Nome = 'teste1'
Senha = 'testeteste'
Alvo = 'teste2'
imagem =''

bot=Bot()
bot.login(username=Nome, password=Senha)
bot.follow(Alvo) #segue uma pessoa especifica
bot.unfollow(Alvo) #para de seguir uma pessoa especifica
bot.upload_photo(imagem, caption='alguma coisa como upload') #faz upload de imagem no insta
bot.send_message('alguma coisa enviada', Alvo)
