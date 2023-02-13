import numpy as np
import cv2


class Contours():

    #retorna somente os contornos que são moedas
	def circle_contours(self, contours, hierarchy):
		indexes = []
		new_countours = []
		#o 0 porque so tem 1 elemento
		#o 3 é o que diz o elemento pai
		for x in range(len(contours)):
			#verifica se existe contornos dentro de contornos
			#caso não exista ele adiciona
			#adiciona o indice da figura com o donut para depois ser removido
			if hierarchy[0][x][3]!= -1:
				indexes.append(hierarchy[0][x][3])
				indexes.append(x)
				print(hierarchy[0][x][3])

		#cria uma lista sem a forma geometrica do indice
		for x in range(len(contours)):
			if x not in indexes:
				new_countours.append(contours[x])

		return new_countours

	#retorna somente os contornos discriminados com um dado tamanho
    #passado como argumento
	def discriminant_contours(self, new_contours, size):
		contour_list = []
		for contour in new_contours:
			radius = cv2.minEnclosingCircle(contour)[1]
			#para calcular de forma a que apanhe somente a moeda e não apanhar também outras coisas (background ou outro)
			if(abs(np.pi*(radius**2)-cv2.contourArea(contour)) < size):
				contour_list.append(contour)

		return contour_list

        	
    
    


















