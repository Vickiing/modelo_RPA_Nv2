import pyautogui as pg

botao = 'botaofim2.png'
def teste_de_imagem():
    while True:
        try:
            localizar = pg.locateOnScreen(botao, confidence=0.6, minSearchTime=0.6)
            pg.click(localizar)
        except pg.ImageNotFoundException:
            break


