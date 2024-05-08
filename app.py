import streamlit as st
from st_audiorec import st_audiorec

from nameder import init_model_ner, get_entity_labels
from speech2text import init_model_trans, transcribe
from translation import translate
from resources import audit_elapsedtime, set_start
import subprocess

def main ():
    print("------------------------------")
    print(f"Running main")

    #print(subprocess.Popen('pip freeze > requirements_hug.txt', shell=True))
    # original = "Tenho uma proposta para a Caixa Geral de Depositos, para 3 consultores Outsystems, 300 euros por dia e um periodo de seis meses."
    # st.write(f"Original: {original}")
    # traducao = get_translation(text_to_translate=text, languageCode="pt")
    # st.write(traducao)

    # translation = translate(original) 
    # st.write(f"Translation: {translation}")  
    print("Rendering UI...")
    start_render = set_start()
    wav_audio_data = st_audiorec()
    audit_elapsedtime(function="Rendering UI", start=start_render)

    if wav_audio_data is not None:
        start_loading = set_start()
        print("Audio:",wav_audio_data,type(wav_audio_data))
        s2t = init_model_trans()
        ner = init_model_ner()

        print("Loading data...")
        #st.audio(wav_audio_data, format='audio/wav')
        original = transcribe(wav_audio_data, s2t)
        st.write(f"Transcription: {original}")
        translation = translate(original)[0]['generated_text']
        st.write(f"Translation: {translation}")

        if translation is not None and ner is not None:
            st.write('Entities: ', get_entity_labels(model=ner, text=translation))
        loading_elapsedtime = audit_elapsedtime(function="Loading data", start=start_loading)

        st.write(f"Total elapsed time: {int(loading_elapsedtime/60)} minutes and {int(loading_elapsedtime%60)} seconds")


if __name__ == "__main__":
    print("IN __name__")
    main()