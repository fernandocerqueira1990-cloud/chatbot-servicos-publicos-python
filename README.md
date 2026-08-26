# Chatbot de Serviços Públicos em Python

Chatbot baseado em regras desenvolvido em Python com a biblioteca NLTK para simular um atendimento básico de serviços públicos.

O projeto foi criado como parte dos estudos e da prática em Python e Processamento de Linguagem Natural (PLN), com foco na estruturação de diálogos, no reconhecimento de padrões e no tratamento das entradas do usuário.

## Funcionalidades

- Responde a perguntas previamente definidas
- Simula orientações sobre renovação de documentos
- Informa os documentos necessários
- Reconhece mensagens de agradecimento e despedida
- Exibe uma resposta padrão quando não reconhece a pergunta
- Encerra o atendimento com o comando `sair`

## Tecnologias utilizadas

- Python 3
- NLTK
- Expressões regulares
- Google Colab

## Como executar

### No Google Colab

1. Acesse [Google Colab](https://colab.research.google.com/).
2. Crie um notebook.
3. Copie o conteúdo de `chatbot.py` para uma célula.
4. Execute a célula e interaja com o chatbot.

### No computador

```bash
git clone https://github.com/fernandocerqueira1990-cloud/chatbot-servicos-publicos-python.git
cd chatbot-servicos-publicos-python
python -m pip install -r requirements.txt
python chatbot.py
```

## Exemplos de mensagens

```text
olá
como faço para renovar meu documento?
quais documentos eu preciso?
obrigado
tchau
sair
```

## Conceitos praticados

- Importação e utilização de bibliotecas
- Estruturas condicionais e de repetição
- Funções, entrada e saída de dados
- Reconhecimento de padrões
- Estruturação de diálogos
- Fluxo de interação entre usuário e sistema

## Limitações

Este é um chatbot baseado em regras. As respostas dependem dos padrões programados e não utilizam um modelo generativo de inteligência artificial.

## Possíveis melhorias

- Reconhecer diferentes maneiras de formular a mesma pergunta
- Ampliar a base de serviços e respostas
- Tratar variações de acentuação e escrita
- Criar uma interface gráfica ou aplicação web
- Registrar o histórico dos atendimentos
- Integrar o chatbot a uma API de serviços públicos

## Autor

**Fernando Cerqueira**

Projeto desenvolvido para estudo e aprimoramento de conhecimentos em Python, Ciência de Dados e Processamento de Linguagem Natural.
