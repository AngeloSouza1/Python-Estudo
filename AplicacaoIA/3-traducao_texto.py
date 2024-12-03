from deep_translator import GoogleTranslator

# 1 - Idiomas Disponíveis
langs_dict = GoogleTranslator().get_supported_languages(as_dict=True)
print(langs_dict)

# 2 - Tradução Pt para En
text = 'Estamos estudando Processamento de Linguagem Natural'
translated = GoogleTranslator(
    source = 'pt',
    target = 'el'
).translate(text=text)
print(translated)

# 3 - Tradução em itens de uma lista
texts = [
    "Estou aprendendo automação com Python",
    "Estou gostando muito",
    "Quero aprender a desenvolver sistemas em Python"
]
translated_itens = GoogleTranslator(
    source = 'pt',
    target = 'en'
).translate_batch(texts)
print(translated_itens)