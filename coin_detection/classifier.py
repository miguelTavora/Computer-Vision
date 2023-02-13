import numpy as np
import cv2


class Classifier():

    #classifica as moedas baseado na distância entre os valores nas médias e valor obtido na imagem
    #distância ao centróide  pelas médias de todas as imagens
	def classify(self, coin):
		medias = np.array([17617.5,13683.0,15235.916666666666,12221.57142857143,9032.857142857143,10653.0,8052.5,5332.5])
		coins = [2.0,1.0,0.50,0.20,0.10,0.05,0.02,0.01]
		distance = np.abs(coin-medias)
		return np.round(coins[np.argmin(distance)],2)


	#poe o texto do dinheiro individualmente em cada moeda
	def put_text_on_coin(self, img, posX, posY, radius, coin):
		coin_text=""
		if(coin<1.0):
			coin_text=str(int(coin*100))+" centimos"
			#print(str(int(coin*100))+" centimos")
		else:
			coin_text=str(int(coin))+" euros"
			#print(str(int(coin))+" euros")
		cv2.putText(img,coin_text,(int(posX)-int(radius),int(posY)),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,255),2)

    
    


















