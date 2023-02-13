import cv2
import numpy as np
from classifier import Classifier
from contours import Contours

classification = Classifier()
obj_contours = Contours()
path="treino/"

files = np.array(["P1000697s.jpg","P1000698s.jpg","P1000699s.jpg","P1000703s.jpg","P1000705s.jpg","P1000706s.jpg","P1000709s.jpg","P1000710s.jpg","P1000713s.jpg"])


    
for x in range(files.size):  
    img=cv2.imread(path+files[x])

    # ------ vai buscar o plano vermelho -------
    img1=img[:,:,2]
    
    # ------ aumentar exposição da imagem (nunca passa de 255, não faz overflow)-------
    img1 = cv2.add(img1,np.array([127.0]))

    # ------ binarização (criar um limiar de otsu, o valor é decicido pelo algoritmo e o 127 é ignorado)-------
    thresh,bin_img=cv2.threshold(img1,127,255,cv2.THRESH_OTSU)

    # ------ núcleo do elemento morfológico (estrutura que será aplicada no elemento morfológico) -------
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(35,35))

    # ------ aplicação do elemento morfológico (erosão, para separar as duas moedas juntas)-------
    img2 = cv2.morphologyEx(bin_img,cv2.MORPH_ERODE,kernel)

    # ------ encontrar os contornos na imagem (contornos são as moedas e as outras formas) -------
    contours,hierarchy=cv2.findContours(img2, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # ------ encontrar só os contornos que são moedas -------
    new_contours = obj_contours.circle_contours(contours,hierarchy)

    # ------ encontrar os contornos somente superiores ao valor passado no segundo argumento -------
    contour_list = obj_contours.discriminant_contours(new_contours,1000)

    money = 0
    for c in contour_list:
        #vai buscar o circulo em volta do contorno
        (cX,cY),radius = cv2.minEnclosingCircle(c)

        #desenha o circulo na imagem
        cv2.circle(img, (int(cX), int(cY)), int(radius)+10, (0, 0, 255), 5)
        
        #print(cv2.contourArea(c))
        # ------ classificação da moeda -------
        coin = classification.classify(cv2.contourArea(c))

        # ------ poe texto do dinheiro de cada moeda individualmente -------
        classification.put_text_on_coin(img,cX,cY,radius,coin)

        # ------ incrementa a quantidade dinheiro -------
        money+=coin

    # ------ desenho do total em dinheiro da moeda -------
    cv2.putText(img,"Total: "+str(round(money,2))+" euros",(20,700),cv2.FONT_HERSHEY_SIMPLEX,2,(0,0,255),2)

    #print("--------------------------")
    cv2.imshow("Image:"+str(files[x]),img)
    


cv2.waitKey(0)
cv2.destroyAllWindows()













