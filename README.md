# Compressor de Vídeo em Python

Esse projeto tem como objetivo auxiliar **QAs/Testers** em suas evidências gravadas proporcionando uma compressão que reduza consideravelmente os vídeos sem perder muita qualidade.

**OBS:** Este algoritmo pode possuir erros ou falhas não mapeadas ainda, portanto seu teste e utilização é muito importante, assim como sinalizar qualquer inconsistência, além disso, procure experimentar as **funcionalidades em teste** acessando a branch *testing*, lá poderá utilizar recursos novos implementados, porém, atente-se que poderão ocorrer erros críticos.

## Como Usar:

1. Clone o projeto na sua área de trabalho.
2. Coloque na pasta "input" todos os vídeos ou pastas com vídeos que deseja comprimir.
3. Execute o arquivo main.py.
4. Retire seus vídeos comprimidos na pasta "output".

> Para executar o arquivo main.py você pode:
> 
> Clicar nele duas vezes ou
> 
> Abrir um terminal na mesma pasta e digitar (uma das opções):
> > python3 main.py
>
> > python main.py
> 
> > py main.py

---

### Cuidados:
Python 3 instalado na máquina.  
No caso de sistemas operacionais Linux é necessário instalar o software FFMPEG:  
> sudo apt install ffmpeg  
> 
A compressão atualmente suporta apenas arquivos **MP4** ou **MKV**.  
Os vídeos originais a serem comprimidos não serão eliminados, apenas uma cópia comprimida será gerada em "output".

+ **Atenção!** Qualquer vídeo já comprimido ainda presente em "output" será ignorado no processo de compressão se ainda estiver presente em "input".

---

### Contato:
+ raisson.souza@voalle.com.br

---

#### V0.1.
Versão base.

#### V0.2.
Adição de Logs.

#### V0.3.
Compressão disponível para arquivos .mkv

#### V0.4.
Validação de vídeos já comprimidos.

#### V0.5.
A compressão agora recria qualquer pasta com vídeos dentro de "input", o que significa que se você prefere organizar seus vídeos dentro de pastas com até mais pastas com vídeos dentro, essa mesma arquitetura com os vídeos comprimidos será gerada em "output", preservando a sua organização.

#### V0.6.
Ajuste dos logs.