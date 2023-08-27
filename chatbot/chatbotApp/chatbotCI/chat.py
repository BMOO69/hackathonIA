from rivescript import RiveScript
bot=RiveScript()
bot.load_file('preguntas.rive')
bot.sort_replies()
while True:
    msg = input('Tu> ')
    if msg == '/salir':
        quit()
    reply = bot.reply("localuser", msg)
    print ('ChatBot> ' + str(reply))
