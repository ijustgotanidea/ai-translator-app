import streamlit as st
from deep_translator import GoogleTranslator

st.title("🌍 Tradutor Multilíngue com Deep Translator")

# Seleção de idiomas
linguas = {
    "Português": "pt",
    "Inglês": "en",
    "Espanhol": "es",
    "Francês": "fr",
    "Alemão": "de",
    "Italiano": "it",
    "Chinês (Simplificado)": "zh-CN",
    "Japonês": "ja",
    "Russo": "ru",
    "Koreano": "ko",
}

# Seleção de idioma de origem
idioma_origem = st.selectbox("Idioma de origem:", list(linguas.keys()), index=0)
codigo_origem = linguas[idioma_origem]

#Área de textos
texto = st.text_area(f"Digite sua frase em {idioma_origem.lower()}:", 
                     "Olá! Estou aprendendo a programar em Python e a usar modelos de inteligência artificial.",
                     max_chars=1000)

if len(texto) > 0:
    st.caption(f"Caracteres: {len(texto)}/1000")

idiomas_escolhidos = st.multiselect("Selecione os idiomas de destino:", list(linguas.keys()), ["Inglês", "Espanhol"])

#traduzir
if st.button("Traduzir"):
    if texto.strip() == "":
        st.warning("Digite uma frase para traduzir!")
    elif not idiomas_escolhidos:
        st.warning("Selecione pelo menos um idioma de destino!")
    else:
        progress_bar = st.progress(0)
        total = len(idiomas_escolhidos)
        
        for i, nome in enumerate(idiomas_escolhidos):
            try:
                with st.spinner(f'Traduzindo para {nome}...'):
                    codigo = linguas[nome]
                    if codigo == codigo_origem:
                        st.info(f"⚠️ Idioma de origem e destino são iguais para {nome}")
                        continue
                    traducao = GoogleTranslator(source=codigo_origem, target=codigo).translate(texto)
                    st.subheader(f'➡ Tradução para {nome} ({codigo})')
                    st.write(f'**Original ({idioma_origem}):** {texto}')
                    st.write(f'**Traduzido:** {traducao}')
                    st.write("---")
            except Exception as e:
                st.error(f"❌ Erro ao traduzir para {nome}: {str(e)}")
            
            progress_bar.progress((i + 1) / total)
        
        st.success("✅ Tradução concluída!")
