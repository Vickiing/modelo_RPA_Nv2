import sys
import pandas as pd
import pyautogui as pg
from time import sleep
from codigos_do_RPA.filial import Filial
from codigos_do_RPA.teste_de_imagem_simplificado import teste_de_imagem

filiais = {
            19:1, 27:2, 35:3, 43:4, 51:5, 60:6, 78:7, 86:8, 94:9, 108:10, 116:11, 124:12, 132:13, 140:14,
            159:15, 167:16, 175:17, 183:18, 191:19, 205:20, 213:21, 221:22, 230:23, 248:24, 256:25, 264:26,
            272:27, 280:28, 299:29, 302:30, 310:31, 329:32, 337:33, 345:34, 353:35, 361:36, 370:37, 388:38, 396:39, 400:40,
            418:41, 426:42, 434:43, 442:44, 450:45, 469:46, 477:47, 485:48, 7005:700, 7013:701, 7021:702
        }

arquivo = r"C:\Users\vlsilva\Desktop/notas_lojas.txt"
df = pd.read_csv(arquivo, sep="|", encoding='latin1')

#entrada do usuario
data = input("informe a data:")
agenda = input("informe a agenda:")

#troca de tela
pg.hotkey('alt','tab')
sleep(0.5)
filiais_selecionadas = set()

#iteracao no TXT
for index, row in df.iterrows():
    cod_filial = row['FILIAL_COM_DIGITO']
    valor_segunda_coluna = row['NOTAFISCAL']

    if cod_filial not in filiais_selecionadas:
        if cod_filial in filiais:
            filial = Filial(cod_filial, data, agenda)  
            filial.seleciona_loja()
            filiais_selecionadas.add(cod_filial)
        else:
            print("Programa encerrado.")
            sys.exit()
    
    teste_de_imagem()
    pg.doubleClick(568, 264, interval=0.3)
    pg.typewrite(str(valor_segunda_coluna), interval=0.2)
    sleep(0.5)
    pg.hotkey('enter')
    teste_de_imagem()
    sleep(0.3)
    teste_de_imagem()
    sleep(4)
    pg.hotkey('enter')
    sleep(5)
#alerta de finalizacao
pg.alert("Importação de notas finalizada!", "Importador Recebimento")