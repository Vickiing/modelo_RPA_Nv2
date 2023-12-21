import pyautogui as pt

filais = {
            19:1, 27:2, 35:3, 43:4, 51:5, 60:6, 78:7, 86:8, 94:9, 108:10, 116:11, 124:12, 132:13, 140:14,
            159:15, 167:16, 175:17, 183:18, 191:19, 205:20, 213:21, 221:22, 230:23, 248:24, 256:25, 264:26,
            272:27, 280:28, 299:29, 302:30, 310:31, 329:32, 337:33, 345:34, 353:35, 361:36, 370:37, 388:38, 396:39, 400:40,
            418:41, 426:42, 434:43, 442:44, 450:45, 469:46, 477:47, 485:48, 7005:700, 7013:701, 7021:702
        }

class Filial:
    

    def __init__(self, loja, data, agenda):
        self.loja = loja
        self.data = data
        self.agenda = agenda
    
        
    def seleciona_loja(self):
        #campo loja
        pt.doubleClick(420,184, interval=0.2)
        pt.typewrite(str(self.loja), interval=0.3)
        #campo data
        pt.click(1159,183, interval=0.2)
        pt.typewrite(str(self.data), interval=0.2)
        #campo agenda
        pt.click(408,223, interval=0.2)
        pt.typewrite(str(self.agenda), interval=0.2)


# entrada = int(input("Digite a loja com digito: "))

# if  entrada in filais:
#     print(filais[entrada])


#numero_loja = print(filais[19])