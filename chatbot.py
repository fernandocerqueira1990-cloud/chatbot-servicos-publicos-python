"""Chatbot baseado em regras para simular atendimento de serviços públicos."""

from nltk.chat.util import Chat, reflections

PAIRS = [
    [r"olá", ["Olá! Como posso ajudá-lo hoje?"]],
    [
        r"como faço para renovar meu documento\?",
        [
            "Você pode renovar seus documentos acessando o site do órgão "
            "responsável ou comparecendo a uma unidade próxima."
        ],
    ],
    [
        r"quais documentos eu preciso\?",
        [
            "Você precisará de um documento de identificação, "
            "comprovante de residência e CPF."
        ],
    ],
    [r"obrigado", ["De nada! Estou aqui para ajudar."]],
    [r"tchau", ["Até logo! Tenha um ótimo dia."]],
]


def iniciar_chatbot():
    """Inicia o fluxo de conversa no terminal."""
    chatbot = Chat(PAIRS, reflections)

    print("Bem-vindo ao Chatbot de Serviços Públicos!")
    print('Digite "sair" para encerrar o atendimento.')

    while True:
        user_input = input("Você: ").strip()

        if user_input.lower() == "sair":
            print("Chatbot: Até logo! Espero ter ajudado.")
            break

        response = chatbot.respond(user_input)

        if response:
            print(f"Chatbot: {response}")
        else:
            print(
                "Chatbot: Desculpe, não entendi sua pergunta. "
                "Por favor, tente novamente."
            )


if __name__ == "__main__":
    iniciar_chatbot()
