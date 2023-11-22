# Compressor de Vídeo em Python

Esse projeto tem como objetivo auxiliar **QAs/Testers** em suas evidências gravadas proporcionando uma compressão que reduza consideravelmente os vídeos sem perder muita qualidade.

**OBS:** Este algoritmo pode possuir erros ou falhas não mapeadas ainda, portanto seu teste e utilização é muito importante, assim como sinalizar qualquer inconsistência, além disso, procure experimentar as **funcionalidades em teste** acessando a branch *testing*, lá poderá utilizar novos recursos implementados (que apresentam implementações mais ágeis e fáceis para o usuário), porém atente-se, poderão ocorrer erros críticos.

## Como Usar:

1. **Clone o projeto** ou **baixe a release** desejada na aba Releases.
    + Veja a aba *Como instalar o Algoritmo* abaixo.
2. Coloque na pasta "input" todos os vídeos ou pastas com vídeos que deseja comprimir.
3. Execute o arquivo main.py.
4. Retire seus vídeos comprimidos na pasta "output".

## Como instalar o algoritmo:

+ **USANDO GIT:**
+ 1. Abra um terminal na sua área de trabalho;
+ 2. Digite:
+ > git clone https://github.com/RaissonSS/video_compressor_python.git

---

+ **INSTALANDO A RELEASE:**
+ 1. Selecione uma release desejada na aba Releases no repositório do GitHub (ou a última);
+ 2. Instale da aba *Assets* o arquivo *Source Code* com a extensão **ZIP**.

## Como executar o algoritmo:

+ Clique no arquivo main.py duas vezes  
**Ou**
+ Abra um terminal na mesma pasta e digite uma das seguintes opções:
> python3 main.py  
> python main.py  
> py main.py

---

### Cuidados:
**Python 3** instalado na máquina.  
No caso de sistemas operacionais **Linux** é necessário instalar o software **FFMPEG**.    
Você pode validar a existência do FFMEPG digitando "ffmpeg" em qualquer terminal, se instruções do software aparecerem, você tem, caso o comando não seja reconhecido, você pode **instalar** ele assim:  
> sudo apt install ffmpeg  
> 
A compressão atualmente suporta apenas arquivos **MP4** ou **MKV**.  
Os vídeos originais a serem comprimidos **não serão excluídos**, apenas uma cópia comprimida será gerada em "output".

+ **Atenção!** Qualquer vídeo já comprimido ainda presente em "output" será **ignorado** no processo de compressão se ainda estiver presente em "input".

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