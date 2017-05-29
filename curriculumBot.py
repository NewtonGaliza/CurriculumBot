import telebot

bot = telebot.TeleBot(<TOKEN>)

@bot.message_handler(commands=['start'])
def welcome(message):
    bot.reply_to(message,
    """
    Bem vindo a versão Bot do meu curriculum
    Os comandos disponíveis são:
    /contato
    /formacao
    /experiencia
    /github
    """)

@bot.message_handler(commands=['contato'])
def contact(message):
    bot.reply_to(message,
    """
    Telefone: (83)991470725
    Email: newtonjgaliza@gmail.com
    Telegram: @NewtonGaliza
    """)

@bot.message_handler(commands=['formacao'])
def formatioc(message):
    bot.reply_to(message, 'Estácio IDEZ - Análise e Desenvolvimento de Sistemas')

@bot.message_handler(commands=['experiencia'])
def experience(message):
    bot.reply_to(message,
    """
    #Prestador de Serviço - PMJP - SECITEC
    Instrutor de Estação DIgital
    1 ano e 6 meses
    #Prestador de Serviço - PMJP - SEDES
    Entrevistador Bolsa Fampilia
    [Operador do Cadastro Único e SIBEC]
    2 anos e 1 mês
    #Host Dime
    Atendimento nível 1
    1 mês
    """)

@bot.message_handler(commands=['github'])
def github(message):
    bot.reply_to(message, "https://github.com/NewtonGaliza")

bot.polling()
