# Downloader de Vídeos

Este projeto é uma aplicação Python com interface gráfica que permite baixar vídeos da internet utilizando links fornecidos pelo usuário. Ele suporta múltiplos downloads simultâneos e exibe o progresso de cada download em tempo real.

## Funcionalidades

- **Baixar vídeos de diversos sites**: Suporte para YouTube e outras plataformas através da biblioteca `yt-dlp`.
- **Múltiplos downloads simultâneos**: Gerencie vários downloads ao mesmo tempo.
- **Progresso em tempo real**: Acompanhe o status de cada download diretamente na interface gráfica.

## Tecnologias utilizadas

- **Python**: Linguagem principal do projeto.
- **Tkinter**: Para criar a interface gráfica.
- **yt-dlp**: Biblioteca para baixar vídeos de diferentes plataformas.

## Pré-requisitos

Certifique-se de ter as seguintes ferramentas instaladas:

- Python 3.6 ou superior
- Biblioteca `yt-dlp`
- FFmpeg (necessário para processamento de vídeos em alguns casos)

### Instalação das dependências

1. Instale a biblioteca `yt-dlp`:
   ```bash
   pip install yt-dlp
   ```

2. Certifique-se de que o FFmpeg está instalado no seu sistema:
   - [Instruções de instalação do FFmpeg](https://ffmpeg.org/download.html)

## Como executar

1. Baixe ou clone este repositório.
2. Navegue até o diretório do projeto.
3. Execute o script principal:
   ```bash
   python video_downloader.py
   ```

## Como usar

1. Insira o link do vídeo na caixa de texto correspondente.
2. Selecione o diretório onde o vídeo será salvo clicando em "Procurar".
3. Clique no botão "Baixar" para iniciar o download.
4. Acompanhe o progresso de cada download na lista de progresso.

## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou pull requests.
