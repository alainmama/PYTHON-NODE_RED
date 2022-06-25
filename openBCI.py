import sys
num = sys.stdin.readline() # read the stdin from the inject node
estatura = float(num[0:4])
dis_h2l = float(num[5:9])
dis_h2r = float(num[10:14])
#Inputs
print("Altura del Paciente: ", estatura,"mts")
print("Distancia del Corazón a la Extremidad Izquierda: ", dis_h2l,"mts")
print("Distancia del Corazón a la Extremidad Derecha: ", dis_h2r,"mts")
#Outputs
tppgl = 0.35
print("Tiempo entre máximo principal y máximo de nodo dicrótico canal izquierdo:", tppgl,"seg")
tppgr = 0.32
print("Tiempo entre máximo principal y máximo de nodo dicrótico canal derecho:", tppgr,"seg")
sil = 5.46
print("Indice de rigidez extremidad izquierda:", sil,"m/s")
sir = 5.44
print("Indice de rigidez extremidad derecha:", sir,"m/s")
hr = 78
print("Frecuencia Cardíaca:",hr,"ppm")
tppg2ecgl = 0.38
print("Tiempo entre máximos PPG y ECG canal izquierdo:",tppg2ecgl,"seg")
vopl = dis_h2l/tppg2ecgl
print("Velocidad de onda de pulso extremidad izquierda:",vopl,"m/s")
tppg2ecgr = 0.37
print("Tiempo entre máximos PPG y ECG canal derecho:",tppg2ecgl,"seg")
vopr = dis_h2r/tppg2ecgr
print("Velocidad de onda de pulso extremidad derecha:",vopr,"m/s")