import cv2
import numpy as np
import matplotlib.pyplot as plt

pathFile = "treino/"

fileName = "P1000697s.jpg"

#vai buscar a imagem no formato -> linhas, colunas, planos de cor
img = cv2.imread(pathFile+fileName)

#a partir da imagem, plano de cor, máscaras, tamanho do histograma, range
#valores usados para criar o histograma 
red=cv2.calcHist([img],[2],None,[256],[0,256])

green=cv2.calcHist([img],[1],None,[256],[0,256])

blue=cv2.calcHist([img],[0],None,[256],[0,256])

grayScale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

gray =cv2.calcHist([grayScale],[0],None,[256],[0,256])




#indices para depois representar os valores
indexes = np.arange(len(red))

plt.figure(figsize=(15,5))

#limiares de otsu
thres,bin_img = cv2.threshold(img[2],127,255,cv2.THRESH_OTSU)
print(thres)

#faz plot dos indices em x e os valores em y
plt.subplot(141)

#criar uma barra para exibir o aparecimento das cores na imagem e mostrar os eixos
plt.bar(indexes,red.ravel(), color='r'),plt.ylabel("Numero de pixeis"),plt.xlabel("Pixeis")

#criar a barra com o valor do limiar
plt.bar(thres,20000,color='black')

#mostrar o titulo
plt.title("Pixeis vermelhos")

#limiares de otsu
thres,bin_img = cv2.threshold(img[1],127,255,cv2.THRESH_OTSU)
print(thres)

plt.subplot(142)
plt.bar(indexes,green.ravel(),color='g'),plt.xlabel("Pixeis")
plt.bar(np.arange(thres,thres+3,1),20000,color='black')
plt.title("Pixeis verdes")

#limiares de otsu
thres,bin_img = cv2.threshold(img[0],127,255,cv2.THRESH_OTSU)
print(thres)

plt.subplot(143)
plt.bar(indexes,blue.ravel(),color='b'),plt.xlabel("Pixeis")
plt.bar(np.arange(thres,thres+2,1),20000,color='black')
plt.title("Pixeis azuis")

#limiares de otsu
thres,bin_img = cv2.threshold(grayScale,127,255,cv2.THRESH_OTSU)
print(thres)

plt.subplot(144)
plt.bar(indexes,blue.ravel(),color='grey'),plt.xlabel("Pixeis")
plt.bar(thres,20000,color='black')
plt.title("Pixeis cinzentos")
plt.show()