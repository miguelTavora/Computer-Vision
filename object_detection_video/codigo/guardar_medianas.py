import cv2
import numpy as np
import pickle
#cap do video
cap=cv2.VideoCapture("camera1.mov")

#leirura das 2 primeiras frames
ret,frame1=cap.read()
ret,frame2=cap.read()
c_m=0
w_m=0
i=0
prima=[]
#2700
#700
while(cap.isOpened()):
    if(i>2700):
        if(i>2950):
            break
        #Diferença entre as frams
        diff=cv2.absdiff(frame2,frame1)

    #Passar para o espaço gray
        gray=cv2.cvtColor(diff,cv2.COLOR_BGR2GRAY)

    #remoçao de ruidp
        blur=cv2.medianBlur(gray,5)

    #threshhold
    #otsu neste caso nao funciona
    #a partir de um thresh de 20 nao se consegue ver a diferença entre as imagens e fica impossivel detetar movimento
        thresh,bin_img=cv2.threshold(blur,12,255,cv2.THRESH_BINARY)
    
    #melhoramento da imagem
        bin_img1=cv2.dilate(bin_img,None,iterations=5)
        cv2.imshow("b",bin_img1)
    #contours

        contours,hierarchy=cv2.findContours(bin_img1, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        #cv2.drawContours(frame1,contours,-1,(0,255,0),3)
        for c in contours:
            if(cv2.contourArea(c)>600):
                (x, y, w, h) = cv2.boundingRect(c)

              #uncoment para ver as larguras
                c_m+=1
                aspect_ratio = float(w)/h
                prima.append(aspect_ratio)
               # w_m+=aspect_ratio
                #print(w_m,"w")
                #print(c_m,"c")

                largura = x+w
            
                altura = y+h

                cv2.rectangle(frame1, (x, y), (largura,altura), (255, 0, 0), 2)
        #cv2.putText(frame1, "Pessoa" ,(x, y), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255),)
        
    #atualizaçao das frames
        cv2.imshow("img",frame1)
        frame1=frame2
        ret,frame2=cap.read()
        if cv2.waitKey(1) == 27:
            break
        if not ret:
            break
        i=i+1
        print(i)       
    else:
        frame1=frame2
        ret,frame2=cap.read()
        i=i+1
        print(i)
        
    
p={"outro":prima}       
pickle.dump(p,open('outro.p','wb'))       
