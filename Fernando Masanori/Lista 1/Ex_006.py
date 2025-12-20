# 6) Calcule o tempo de uma viagem de carro. Pergunte a distância a percorrer e a velocidade média 
# esperada para a viagem.  

'''distancia = float(input("Qual foi a distancia que você percorreu? "))
   velocidade_media = float(input("Qual mais ou menos foi a sua velocidade média? "))

   tempo = distancia / velocidade_media

   print(f'O tempo de viagem foi de {tempo:.2f}')'''

distancia = float(input("Qual foi a distância percorrida (km)? "))
velocidade_media = float(input("Qual foi a velocidade média (km/h)? "))

tempo_horas = distancia / velocidade_media
horas = int(tempo_horas)
minutos = (tempo_horas - horas) * 60

print(f"Tempo de viagem: {horas}h e {minutos:.0f}min")
