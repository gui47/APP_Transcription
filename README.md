# APP Transcription 🎙️

Aplicação desenvolvida em Python para transcrição automática de arquivos de áudio e vídeo utilizando a API Whisper da OpenAI.

## 🚀 Funcionalidades

- Transcrição de arquivos de áudio no formato MP3.
- Transcrição de vídeos no formato MP4.
- Extração automática do áudio dos vídeos.
- Utilização de prompts personalizados para fornecer contexto e orientar as transcrições.
- Interface interativa desenvolvida com Streamlit.

## 🛠️ Tecnologias utilizadas

- **Python:** linguagem utilizada no desenvolvimento da aplicação.
- **OpenAI API (Whisper):** reconhecimento e transcrição de áudio.
- **Streamlit:** desenvolvimento da interface interativa.
- **MoviePy:** processamento de vídeos e extração de áudio.
- **Python-dotenv:** gerenciamento de variáveis de ambiente.

## ⚙️ Instalação e execução

**1. Clone o repositório:**

```bash
git clone https://github.com/gui47/app-transcription.git
```

**2. Acesse a pasta do projeto:**

```bash
cd app-transcription
```

**3. Instale as dependências:**

```bash
pip install -r requirements.txt
```

**4. Configure sua chave da API da OpenAI:**

Crie um arquivo `.env` na raiz do projeto e adicione sua chave:

```env
OPENAI_API_KEY=sua_chave_api
```

**5. Execute a aplicação:**

```bash
streamlit run app.py
```

## 📂 Estrutura do projeto

```text
app-transcription/
│
├── app.py
├── requirements.txt
├── .gitignore
├── README.md
└── temp/
```

## 🎯 Objetivo do projeto

O projeto foi desenvolvido com o objetivo de explorar o desenvolvimento de aplicações em Python, integração com APIs de Inteligência Artificial e processamento de arquivos multimídia, utilizando tecnologia de reconhecimento de voz para transformar áudio e vídeo em texto.

---

Desenvolvido por [Guilherme Reis Aguiar](https://github.com/gui47).