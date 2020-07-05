from flask import Flask, request
import requests
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)


@app.route('/bot', methods=['POST'])
def bot():
    incoming_msg = request.values.get('Body', '')
    resp = MessagingResponse()
    msg = resp.message()
    responded = False
    # if 'quote' in incoming_msg:
    #     # return a quote
    #     r = requests.get('https://api.quotable.io/random')
    #     if r.status_code == 200:
    #         data = r.json()
    #         quote = f'{data["content"]} ({data["author"]})'
    #     else:
    #         quote = 'I could not retrieve a quote at this time, sorry.'
    #     msg.body(quote)
    #     responded = True
    # if 'cat' in incoming_msg:
    #     # return a cat pic
    #     msg.media('https://cataas.com/cat')
    #     responded = True
    if 'iniciar' in incoming_msg:
        # return a cat pic
        msg.body('Olá, bem-vindo ao atendimento Melibot!\n\nEsse atendimento é voltado para clientes que precisam devolver ou trocar uma mercadoria comprada através do Mercado Livre, então farei algumas perguntas para poder te ajudar melhor, tudo bem?\n\n1) Primeiro de tudo, qual o código da sua compra no mercado livre?')
        responded = True
    if 'ML26964631096007124' in incoming_msg:
        msg.body('Estamos checando sua encomenda, aguarde um momento')
        responded = True
    if not responded:
        msg.body('Comando não reconhecido. Comandos disponíveis:\n- iniciar\n')
    return str(resp)


if __name__ == '__main__':
    app.run()