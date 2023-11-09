# Compressor de Vídeo em Python

Esse projeto tem como objetivo auxiliar **QAs/Testers** em suas evidências gravadas proporcionando uma compressão que reduza consideravelmente os vídeos sem perder muita qualidade.

## Como Usar:

1. Clone o projeto na sua área de trabalho.
2. Coloque na pasta "input" todos os vídeos que deseja comprimir.
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

### Cuidados:
+ Python 3 instalado na máquina.
+ A compressão atualmente só suporta arquivos:
+ + .mp4
+ + .mkv
+ **Atenção!** Qualquer vídeo já comprimido ainda presente em "output" será ignorado no processo de compressão se ainda estiver presente em "input".

### Contato:
+ raisson.souza@voalle.com.br

#### V0.1.
Versão base.

#### V0.2.
Adição de Logs.

#### V0.3.
Compressão disponível para arquivos .mkv

#### V0.4.
Validação de vídeos já comprimidos.