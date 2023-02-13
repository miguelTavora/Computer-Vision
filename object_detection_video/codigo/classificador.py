import cv2
import numpy as np


class Classifier():

    def __init__(self):
        self.__points1 = 1
        self.__points2 = 2
        self.__points3 = 3

    #classificador que a partir da mediana calculam a distância ao centroide pela formula de Manhattan
    def classify(self, largura):
        media=np.array([0.4819277108433735,1.3157894736842106,0.7868852459016393])
        objeto=np.array([self.__points1,self.__points2,self.__points3])
        distancia=np.abs(largura-media)
        return objeto[np.argmin(distancia)]

    #função que desenha o rasto na imagem
    def draw_trace(self, points1, points2, points3, frame1):
        if(points1 == self.__points1):
            cv2.line(frame1,(points2,points3),(points2,points3),(0, 0, 255), 2)

        elif(points1 == self.__points2):
            cv2.line(frame1,(points2,points3),(points2,points3),(0, 255, 0), 2)

        elif(points1 == self.__points3):
            cv2.line(frame1,(points2,points3),(points2,points3),(255, 0, 0), 2)



    #função que desenha o quadrado (bounding box)
    def draw_bounding_box(self, points, classification, frame1, x, y, largura, altura, w, h):
        pos_x = int(x+w/2)
        pos_y = int(y+h/2)

        if(classification == self.__points1):
            cv2.rectangle(frame1, (x, y), (largura,altura), (0, 0, 255), 2)
            points.append((self.__points1, pos_x, pos_y))
            cv2.putText(frame1, "PESSOA" ,(x, y), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255))

        elif(classification == self.__points2):
            cv2.rectangle(frame1, (x, y), (largura,altura), (0, 255, 0), 2)
            points.append((self.__points2, pos_x, pos_y))
            cv2.putText(frame1, "CARRO" ,(x, y), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255))

        elif(classification == self.__points3):
            cv2.rectangle(frame1, (x, y), (largura,altura), (255.0, 0, 0), 2)
            points.append((self.__points3,pos_x, pos_y))
            cv2.putText(frame1, "OUTRA" ,(x, y), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255))

        return points
