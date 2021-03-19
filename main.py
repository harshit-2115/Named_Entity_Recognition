import streamlit as st
import wikipedia
import spacy

def ner(text):
    text = text[:100]
    nlp = spacy.load('en')
    doc = nlp(text)

    st.write(doc.ents)
        


def sel(text):
    try:
        k = wikipedia.summary(text)
    except wikipedia.DisambiguationError as e:
        k = wikipedia.summary(e.options[0])
        ner(k)
        


def main():
    st.title('Named Entity Recognition')
    st.subheader('Using Wikipedia content to perform NER')
    user_input = st.text_area("Enter Title of Wikipedia Page", "Type here")
    if st.button("Recognize"):
        sel(user_input)


if __name__ == '__main__':
    main()
