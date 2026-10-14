
import streamlit as st
import openai
from dotenv import load_dotenv, find_dotenv
from moviepy.video.io.VideoFileClip import VideoFileClip

_ = load_dotenv(find_dotenv())

folder_temp = "temp"
file_audio_temp = f"{folder_temp}/audio.mp3"
file_video_temp = f"{folder_temp}/video.mp4"

openai = openai.Client()

def transcreve_audio(file_audio, prompt=None):
    """Função para transcrever o áudio usando a API da OpenAI"""
    if file_audio:
        transcription = openai.audio.transcriptions.create(
            model="whisper-1",
            language="pt",
            response_format="text",
            file=file_audio,
            prompt=prompt
        )
        return transcription
    return None

def transcreve_video(file_video, prompt=None):
    """Função para transcrever áudio a partir de um vídeo"""
    if file_video:
        with open(file_video_temp, "wb") as f_video:
            f_video.write(file_video.read())
        video_convert = VideoFileClip(file_video_temp)
        video_convert.audio.write_audiofile(file_audio_temp)
        with open(file_audio_temp, "rb") as file_audio:
            transcription = openai.audio.transcriptions.create(
                model="whisper-1",
                language="pt",
                response_format="text",
                file=file_audio,
                prompt=prompt
            )
            return transcription

def main():
    """Função principal da aplicação"""
    st.header("APP Transcript", divider=True)
    st.subheader("Transcreva áudios e vídeos")
    tabs = ["Vídeo", "Áudio"]
    tab_video, tab_audio = st.tabs(tabs)
    with tab_video:
        st.markdown("Teste em vídeo")
        prompt_video = st.text_input("Digite o seu prompt", key="video_prompt")
        file_video = st.file_uploader("Adicione um arquivo de video .mp4", type=["mp4"])
        if file_video:
            transcricao_video = transcreve_video(file_video, prompt_video)
            if transcricao_video:
                st.write(transcricao_video)
            else:
                st.error("Erro ao transcrever o áudio")
    with tab_audio:
        st.markdown("Teste em áudio")
        prompt_audio = st.text_input("Digite o seu prompt")
        file_audio = st.file_uploader("Adicione um arquivo de áudio .mp3", type=["mp3"])
        if file_audio:
            transcricao_audio = transcreve_audio(file_audio, prompt_audio)
            if transcricao_audio:
                st.write(transcricao_audio)
            else:
                st.error("Erro ao transcrever o áudio")

if __name__ == "__main__":
    main()
