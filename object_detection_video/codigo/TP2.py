import cv2
import numpy as np
from classificador import Classifier

#objeto classificador e desenhar rasto
classifier = Classifier()

#cap do video
cap=cv2.VideoCapture("camera1.mov")

#leirura das 2 primeiras frames
ret,frame1=cap.read()
ret,frame2=cap.read()

#array para armanzenar os pontos pra descrever a trajetoria de cada objeto
points=[]

#minimo tamanho da área
area = 330

while(cap.isOpened()):
    
    #Diferença entre as frams
    diff=cv2.absdiff(frame1,frame2)

    #Passar para o espaço vermelho
    gray= diff[:,:,2]

    #remoçao de ruido
    blur = cv2.medianBlur(gray,5)

    #threshold
    #otsu neste caso nao funciona
    #a partir de um thresh de 20 nao se consegue ver a diferença entre as imagens e fica impossivel detetar movimento
    thresh,bin_img = cv2.threshold(blur,12,255,cv2.THRESH_BINARY)
    
    #melhoramento da imagem
    bin_img1 = cv2.dilate(bin_img,None,iterations=5)

    #mostrar a imagem binarizada após o operador morfológico
    cv2.imshow("b",bin_img1)

    #encontrar os contornos na imagem
    contours,hierarchy=cv2.findContours(bin_img1, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)


    for c in contours:
        #verificar o tamanho do contorno para ser maior que um determinado limiar
        if(cv2.contourArea(c)>area):
            #vai buscar um quadrado em volta do contorno
            (x, y, w, h) = cv2.boundingRect(c)

            #calculo do aspect-ratio para classificar
            largura = x+w
            altura = y+h
            aspect_ratio = float(w)/h

            #classificação dos contornos pelo classificador
            classification = classifier.classify(aspect_ratio)
            
            #desenha a bouding box a volta do contorno feito a partir da classificação
            points = classifier.draw_bounding_box(points, classification, frame1, x, y, largura,altura,w,h)
                
    #colocaçao dos pontos na imagem
    for i in range(len(points)):
        classifier.draw_trace(points[i][0],points[i][1],points[i][2],frame1)
            

    #desenho da nova frame
    cv2.imshow("img",frame1)
    
    #atualizaçao das frames
    frame1 = frame2
    ret,frame2 = cap.read()
    #terminar clicar no ESC
    if cv2.waitKey(1) == 27:
        break
    #terminar quando acaba frames
    if not ret:
        break




