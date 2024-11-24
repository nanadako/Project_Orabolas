# Acessar a biblioteca de grafico
import numpy as np
import matplotlib.pyplot as plt
 
# Colocar o robô em campo com posição X e Y
robox = float(input("Coloque a posição X do Robô:"))
roboy = float(input("Coloque a posição Y do Robô:"))
 
# Percorrer colunas de trajetoria e acessando o arquivo 
with open('trajetoria.csv', 'r') as f:
  num_colunas = 3
  linhas = []
 # Acessando as linhas e colunas atraves da matriz
  for linha in f:
    valores = [float(v) for v in linha.strip().split(';')]
    linhas.append(valores)
    matriz = np.array(linhas)
 
 # Calculando ponto de interceptação dividindo a distancia da velocidade do robô
def calcular_ponto_interceptacao(distancia, bolax, bolay, velocidade_robo):
    # Calcular o tempo de interceptação com base na distância e na velocidade do personagem
    tempo_interceptacao = distancia / velocidade_robo
 
    # Calcular as coordenadas do ponto de interceptação
    ponto_interceptacao_x = bolax
    ponto_interceptacao_y = bolay
    return ponto_interceptacao_x, ponto_interceptacao_y, tempo_interceptacao
 
 
# Calculo em laço da bola percorrendo a trajetória com ela andando
tempo = 0 
while tempo <= 1000:
      bolax = matriz[tempo][1]
      bola_tempo = matriz[tempo][0]
      print("A bola 'x' está em: {:.2f} m/s".format (bolax))
 
      bolay = matriz[tempo][2]
      print("A bola 'y' está em: {:.2f} m/s".format (bolay))
 
      # Calcula distancia entre a bola e o robô
      distancia = ((bolax - robox)**2 + (bolay - roboy)**2)**0.5
 
      # Interceptação entre a bola e o robô ao vivo
      intercept_x, intercept_y, tempo_interceptacao = calcular_ponto_interceptacao(distancia, bolax, bolay, 2.8)
 
      # Prints sobre a interceptação e a distancia final
      tempo += 1
      if distancia <=bolax and distancia <= bolay:
        print("A distancia mais proxima foi de: {:.2f} m/s".format(distancia))
        print("Ponto de Interceptção Final: {:.2f} x {:.2f} y ".format(intercept_x,intercept_y))
        print("Tempo de Interceptação Final: {:.2f} s".format(tempo_interceptacao))
        print()
      
        
        #Conta feita fora do programa
        # 3 forças(impulso,superficie,peso gravitacional)
        #            0,784    2,8       2,8
        print("Aprofundamento: ")
        print(" A bola tem uma força Resultante de FR = 32,1786 ")
        print("E o Robô tem uma força Resultante de FR = 6,384.")
        break
      else:
        print("Rodando...")
 
 
# Cálculo da distância percorrida pelo objeto
distancia = ((matriz[1][1] - matriz[0][1])**2 + (matriz[1][2] - matriz[0][2])**2)**0.5
print("A distancia percorrida pela bola foi de : {:.2f} m/s".format(distancia))
 
# Cálculo da velocidade do objeto
velocidade = distancia / (matriz[1][0] - matriz[0][0])
print("A velocidade do objeto foi de: {:.2f} m/s".format(velocidade))
 
# Dados da trajetória da bola e do robô
t = np.linspace(bolax,bolay,20)  # Tempo
x_bola = bolax * t  # Posição x da bola
y_bola = bolay * t  # Posição y da bola
x_robo = robox * t  # Posição x do robô
y_robo = roboy * t  # Posição y do robô

vx_bola = bolax * np.ones_like(t)  # Velocidade vx da bola (constante)
vy_bola = bolay * np.ones_like(t)  # Velocidade vy da bola (constante)
vx_robo = robox * np.ones_like(t)  # Velocidade vx do robô (constante)
vy_robo = roboy * np.ones_like(t)  # Velocidade vy do robô (constante)
ax_bola = 2.8 * np.ones_like(t)  # Aceleração ax da bola (zero)
ay_bola = 2.8*np.ones_like(t)  # Aceleração ay da bola (zero)
ax_robo = 2.8* np.ones_like(t)  # Aceleração ax do robô (zero)
ay_robo = 2.8*np.ones_like(t)  # Aceleração ay do robô (zero)
d = np.sqrt((x_bola - x_robo) ** 2 + (y_bola - y_robo) ** 2)  # Distância relativa

#Definindo pontos importantes da bola para o cálculo

px_bola = x_bola[1]
pfx_bola = x_bola[19]
py_bola = y_bola[1]
pfy_bola = y_bola[19]


#Definindo pontos importantes do robô para o cálculo posterior
px_robo = x_robo[1]
pfx_robo = x_robo[19]
py_robo =y_robo[1]
pfy_robo = y_robo[19]


#Cálculo para saber a Diferença do ponto inicial para o Ponto Final 

pxfinalbolax = pfx_bola -px_bola
pmyfinalbolay = -pfy_bola +py_bola


pxfinalrobox = pfx_robo -px_robo
pmyfinalroboy = pfy_robo -py_robo







 
# Gráfico das trajetórias da bola e do robô em um plano xy
plt.figure()
plt.plot([pmyfinalbolay,pxfinalbolax], label='Bola')

plt.plot([pmyfinalroboy,pxfinalrobox],label='Robô')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Trajetórias da bola e do robô')
plt.legend()
 
# Gráfico das coordenadas x e y da posição da bola e do robô em função do tempo
plt.figure()
plt.subplot(2, 1,2)
plt.plot(t, x_bola, label='Bola')
plt.plot(t,x_robo, label='Robô')
plt.xlabel('tempo t(s)')
plt.ylabel('posição x(t)')
plt.title('Posição em função do tempo')
plt.legend()
 
# Gráfico das componentes vx e vy da velocidade da bola e do robô em função do tempo
plt.figure()
plt.subplot(2, 1, 1)
plt.plot(t, vx_bola, label='Bola')
plt.plot(t, vx_robo, label='Robô')
plt.ylabel('vx')
plt.title('Velocidade em função do tempo')
plt.legend()
plt.subplot(2, 1, 2)
plt.plot(t, vy_bola, label='Bola')
plt.plot(t, vy_robo, label='Robô')
plt.xlabel('Tempo')
plt.ylabel('vy')
plt.legend()
 
# Gráfico das componentes ax e ay da aceleração da bola e do robô em função do tempo
plt.figure()
plt.subplot(2, 1, 1)
plt.plot(t, ax_bola, label='Bola')
plt.plot(t, ax_robo, label='Robô')
plt.ylabel('ax')
plt.title('Aceleração em função do tempo')
plt.legend()
plt.subplot(2, 1, 2)
plt.plot(t, ay_bola, label='Bola')
plt.plot(t, ay_robo, label='Robô')
plt.xlabel('Tempo')
plt.ylabel('ay')
plt.legend()

# Gráfico da distância relativa d entre o robô e a bola como função do tempo
plt.figure()
plt.plot(d),(t)

plt.xlabel('Tempo')
plt.ylabel('Distância')
plt.title('Distância relativa entre o robô e a bola')
 
# Exibir os gráficos
plt.show()
