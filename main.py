import random

respostas = [
    "Olá! Como posso ajudar você hoje?",
    "Estou aqui para conversar!",
    "Interessante… continue!",
    "Pode falar mais sobre isso!",
    "Entendi. E o que você acha disso?",
    "Hmmm… estou pensando."
]

print("🤖 Chatbot IA simples\nDigite 'sair' para encerrar.\n")

while True:
    user = input("Você: ").strip().lower()

    if user == "sair":
        print("IA: Até mais! 👋")
        break

    resposta = random.choice(respostas)
    print("IA:", resposta)
