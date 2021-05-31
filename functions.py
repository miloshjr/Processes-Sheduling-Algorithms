import numpy as np
import pylab as plt
import os
from Process import Process

def assignment(list=[],array=[]):                                                   # funkcja ta przepisuje obiekty jednej listy do drugiej (argumentami listy: wzór, kopia. 
    i=0                                                                             # funkcja ta działa na liście -> nic nie zwraca
    while i < len(list):
        array.append(list[i])
        array[i].name=list[i].name
        i+=1                    

def FCFS(list=[]):                                                                  # funkcja ta szereguje listę według algorytmu FCFS 
    list.sort(key=lambda process: process.a)                                        # sortuję listę po process.a
    return list                                                                     # zwraca posortowaną listę    

def SJF(list=[]):                                                                   # funkcja ta tworzy listę posortowaną według algorytmu SJF
                                                       
    list.sort(key=lambda process: process.a)                                        # sortuję listę po process.a
    j=0
    time=0                                                                          # tworzę zmienną symulującą czas
    array1=[]                                                                       # tworzę dwie pomocnicze listy
    array2=[]
    while (len(list)!=0):                                                           # sprawdzam za pomocą funkcji len(list) czy lista ma jeszcze w sobie obiekty
        array2.clear()                                                              # "czyszczę" listę
        i=0
        while i < len(list):
            if list[i].a <= time:                                                   # znajduję takie procesy w liscie, które spełniają warunek, że przybyły przed lub w aktualnym czasie
                array2.append(list[i])                                              # zapisuję je do listy pomocniczej
                i+=1
            else:
                i+=1
        array2.sort(key=lambda process: process.s)                                  # sortuję je tu według czasu wykonywania
        array1.append(array2[0])                                                    # najkrótszy z nich dodaję do drugiej listy pomocniczy
        list.remove(array2[0])                                                      # oraz usuwam go z listy (początkowej)
        while j < len(array1):                                                      # ta pętla służy do zliczania akutalnego (ofc symulowanego) czasu
            time=time+array1[j].s
            j+=1
    return array1                                                                   # zwracam drugą listę pomocniczą
   
def LCFS(list=[]):                                                                  # funkcja ta tworzy listę posortowaną według LCFS
    
    list.sort(key=lambda process: process.a)                                        # sortuję listę po process.a
    j=0
    time=0                                                                          # tworzę zmienną symulującą czas
    array1=[]                                                                       # tworzę dwie pomocnicze listy
    array2=[]
    while (len(list)!=0):                                                           # sprawdzam za pomocą funkcji len(list) czy lista ma jeszcze w sobie obiekty
        array2.clear()                                                              # "czyszczę" listę
        i=0
        while i < len(list):
            if list[i].a <= time:                                                   # znajduję takie procesy w liscie, które spełniają warunek, że przybyły przed lub w aktualnym czasie
                array2.append(list[i])                                              # zapisuję je do listy pomocniczej
                i+=1
            else:
                i+=1
        array2.sort(key=lambda process: process.a, reverse = True)                  # sortuję je według czasu przyjścia malejąco
        array1.append(array2[0])                                                    # ten z największym czasem przybycia (last come) dodaję do drugiej listy pomocniczej
        list.remove(array2[0])                                                      # oraz usuwam go z listy (początowej)
        while j < len(array1):                                                      # ta pętla służy do zliczania akutalnego (ofc symulowanego) czasu
            time=time+array1[j].s
            j+=1
    return array1                                                                   # zwracam drugą listę pomocniczą

def arrayexecutiontime(array=[]):                                                   # funkcja zliczająca czas wykonywania procesów znajdujących się w liście
    time=0
    i=0
    while(i<len(array)):                                                            # dopuki i jest krótsze od długości listy
        time+=array[i].s                                                            # zwieksza czas od 0 poprzez kolejne dodawanie wartości process.s
        i+=1
    return time                                                                     # funkcja zwraca czas wykonywania procesów znajdujących się w liście
   
def RR(array=[]):                                                                   # funkcja tworzy listę z procesami według Round-Robin
    q=3                                                                             # wyznaczyłem kwant równy 3
    array.sort(key=lambda process: process.a)                                       # sortuję listę po process.a rosnąco
    list=array.copy()                                                               # tworzę kopię listy    
    i=0
    array1=[]                                                                       # tworzę listę pomocniczą
    while arrayexecutiontime(list) !=0:                                             # za pomocą funkcji arrayexecuiontime sprawdzam czy procesy w liście się już "wykonały" czy suma process[i].s jest różna od zera
        if ((list[i].s) >= q):                                                      # sprawdzam czy czas wykonywania kolejnych procesów jest wiekszy lub równy kwantowi
            x=Process(list[i].name,list[i].a,q)                                     # jeśli tak tworze nowy proces o prametrach takich jak proces sprawdzany poza process.s, które zamieniam na długość kwantu
            array1.append(x)                                                        # taki utworzony proces dodaję do listy pomocniczej
            list[i].s-=q                                                            # zmniejszam process.s w orginalnej liście o kwant
            i=(i+1)%len(list)                                                       # zwiekszam iterator w modulo długość listy początkowej (będzie po niej chodził aż wszystko się wyzeruje)       
        elif (list[i].s == 0):                                                      # w przypadku gdy process.s jest równe 0
            i=(i+1)%len(list)                                                       # tylko zwiekszam iterator
        else:                                                                       # w innym przypadku czyli process.s w przedziale (0,q)
            x=Process(list[i].name,list[i].a,list[i].s)                             # tworze proces o parametrach procesu sprawdzanego
            array1.append(x)                                                        # dodaję go do listy pomocniczej
            list[i].s=0                                                             # zeruję process.s procesu z listy początkowej
            i=(i+1)%len(list)                                                       # zwiększam iterator
    return array1                                                                   # zwracam listę pomocniczą
    
def printarray(list=[]):                                                            # funkcja printuje w kolejnych liniach nazwe każdego procesu z kolei
    i=0
    while i < len(list):
        
       # print(f"\n Name: \n") 
        print(list[i].name)
        #print(f"\n Arrival Time: \n")
        #print(list[i].a)
        #print(f"\n Execution Time: \n") 
        #print(list[i].s)
        i+=1
   
def turnaround_time(list=[], name=str):                                             # funkcja ta zlicza czas od przybycia do wykonania procesu
    i=0
    x=int
    while i < len(list):                                                            # najpierw szuka w liście wybranego procesu po nazwie
        if list[i].name == name :
            x=i                                                                     # iterator odpowiadający jego miejscu w liscie zapisuje w zmiennej x
            i+=1                                                      
        else:
            i+=1
    time=counttime(list,x) - list[x].a                                              # za pomocą funkcji counttime oblicza czas od początku kolejki do wykonania wybranego procesu i odejmuje czas przybycia
                                                                     
    return time                                                                     # zwraca wyżej policzoną wartość

def waiting_time(list=[], execution_time=int, arrival_time=int, name=str):          # funkcja wyliczająca czas oczekiwania wybranego procesu
    i=0                                                
    x=int
    while i < len(list):                                                            # przeszukuje listę pokolei
        if list[i].name == name :                                                   # szuka procesu o wybranej nazwie
            x=i                                                                     # iterator odpowiadający położeniu w liści zapisuje w zmiennej x
            i+=1
        else:
            i+=1
    time=counttime_without(list, x, name)-arrival_time                              # za pomocą funkcji counttime_without zlicza czas od początku kolejki do momentu w którym zaczyna wykonywać się wybrany proces i odejmuje jego czas przybycia
    return time                                                                     # zwraca wyżej wyliczoną wartość

def counttime(list=[], max=int):                                                    # funkcja zliczająca czas od startu kolejki do wykonania wybranego procesu, którego położenie w liście opisane jest w int max
    i=0
    time=0
    while i <= max:
        time+=list[i].s
        i+=1
    return time                                                                     # zwraca wyżej wyliczony czas

def counttime_without(list=[], max=int, name=str):                                  # funkcja działa jak counttime z wyjątkiem że nie dodaje długości wykonywania procesu którego iterator i imie podaliśmy
    i=0                                                                             
    time=0
    while i <= max:
        if list[i].name != name:                                                    # na wypadek gdyby nazwa się powtórzyła w liście (RR) nie zlicza czasu gdy inny proces nazywa się tak samo
            time+=list[i].s
            i+=1
        else:
            i+=1
    return time                                                                     # zwraca czas wyżej wyliczony

def average_turnaround_time(list=[],array=[]):                                      # funkcja wyliczająca średni czas przetwarzania procesu
    i=0
    time=0
    while i < len(array):
        time+=turnaround_time(list,array[i].name)                                   # wykorzystując funkcję turnaroun_time sumuje wartość zwracaną przez tę funkcję dla każdego procesu w liście
        i+=1
    av_time=time/len(array)                                                         # sumę wszystkich procesów dzieli przez ich ilość     
    return av_time                                                                  # zwraca średni czas przetwarzania procesu

def average_waiting_time(list=[],array=[]):                                         # funkcja licząca średni czas oczekiwania wszystkich procesów w liście
    i=0
    time=0
    while i < len(array):
        time+=waiting_time(list, array[i].s, array[i].a, array[i].name)             # wykorzystuje do tego funkcję waiting_time i sumuje zwracane przez nią czasy oczekiwania poszczególnych procesów
        i+=1
    wt_time=time/len(array)                                                         # sumę tą dzieli przez ilość procesów
    return wt_time                                                                  # zwraca średni czas oczekiwania procesów

def standard_deviation(list=[], array=[]):                                          # funkcja wylicza odchylenie standardowe czasu oczekiwania procesów
    i=0
    Var=0
    while i < len(array):
        x=waiting_time(list, array[i].s, array[i].a, array[i].name)                 # przypisuje do zmiennej x czas oczekiwania kolejnych procesów
        y=average_waiting_time(list,array)                                          # przypisuje do zmiennej y średni czas oczekiwania procesów
        z=(x-y)*(x-y)/len(array)                                                    # przypisuje do wartość kwadratu różnicy x i y podzieloną przez długość listy (il. procesów)
        Var+=z                                                                      # tworząc wariancję sumuje z dla każdego procesu
        i+=1                
    SD=np.sqrt(abs(Var))                                                            # odchylenie standardowe liczy pierwiastkiem z wariancji
    return SD                                                                       # zwraca odchylenie standardowe

def figures_of_wt(list=[], array=[], name=str, average=float, deviation=float, a=str):                                                  
    n=len(array)                                                                    # do zmiennej n przypisuje ilość procesów w liście
    x = range(0,n)
    y=[]
    w=[]
    vplus=[]
    vminus=[]
    i=0
    while i < len(array):                                                                 # dopasowanie, od każdego iteratora, czasu oczekiwania procesu
        y.append(waiting_time(list, array[i].s, array[i].a, array[i].name))
        sum=0
        av=0
        j=0
        var=0
        while j < len(y):
            sum+=y[j]
            av=sum/len(y)                                                                   # tworzenie funkcji stałej informującą o średnim czasie oczekiwania
            var+=(y[j]-av)*(y[j]-av)/len(y)
            j+=1
        w.append(av)
        dev=np.sqrt(var)
        vplus.append(w[i] + dev)                                           # tworzenie funkcji stałej informującą o odchyleniu standardowym
        vminus.append(w[i] - dev)
        i+=1
    plt.clf()                                                                       # usuwanie poprzedniego wykresu z pamięci
    plt.xlabel("process nr in queue")                                               # nazwanie OX
    plt.ylabel("time[ms]")                                                          # nazwanie OY
    plt.plot(x,y,'co', label='Each process waiting time')                          # przypisanie do wszystkich funkcji kolorów, kształtów oraz opisów co obrazują
    plt.plot(range(0, len(w)),w,'r-', linewidth=5, label='Average waiting time')
    plt.plot(x,vplus,'k-', linewidth=2, label='Standard deviation upper limit')
    plt.plot(x,vminus,'k-', linewidth=2, label='Standard deviation lower limit')
    plt.fill_between(x,vplus,vminus, color="skyblue", alpha=0.4)
    plt.title( a + " - Figure of waiting time for "+name[:3]+" Processes")   # nadanie nazwy wykresowi
    plt.grid(True)
    legend = plt.legend(loc=2, shadow=True, fontsize='x-small')                     # nadanie legendzie parametrów: lokalizacji, wielkości czcionki, oraz koloru 
    legend.get_frame().set_facecolor('#FBFFC0')
    plt.savefig(name)                                                               # zapisanie wykresu w wybranej ścieżce i o wybranej nazwie

def creation_50(queue=[], path=str):                                                          # funkcja tworząca listę 50-elementową

    file = open(path, 'r')                                         # pobiera dane z pliku o ścieżce podanej
    q=file.readlines()                                                              # zapisuje każdą linie jako element tablicy str
    for i in range(0,50):
        x=q[i].split(",")                                                           # w każdym ze str rozdziela przecinki czyli tworzy liste n elementową (w zależności od przecinków w linijce)
        y=Process(str(x[0]),int(x[1]),int(x[2]))                                    # tworzy proces o parametrach pobranych z list
        queue.append(y)                                                            # dodanie obiektu typu Process do listy
    printarray(queue)

def creation_100(queue=[], path=str):                                                          # funkcja działająca tak samo jak powyższa, tylko dla 100 elementów

    file = open(path, 'r')
    q=file.readlines()
    for i in range(0,100):
        x=q[i].split(",")
        y=Process(str(x[0]),int(x[1]),int(x[2]))
        queue.append(y) 
    printarray(queue)

def creation_500(queue=[], path=str):                                                         # funkcja działająca tak samo jak powyższa, tylko dla 500 elementów

    file = open(path, 'r')
    q=file.readlines()
    for i in range(0,500):
        x=q[i].split(",")
        y=Process(str(x[0]),int(x[1]),int(x[2]))
        queue.append(y) 
    printarray(queue)

def algorithms(queue=[],name=str, path=str, a=int):                                                  # funkcja porządkująca większość powyższych funkcji i tworząca pliki z danymi 

    queue1=[]                                                                       # tworze listy które będą kopią listy z przyjętymi z pliku danymi
    queue2=[]
    queue3=[]
    queue4=[]

    assignment(queue,queue1)                                                        
    assignment(queue,queue2)
    assignment(queue,queue3)
    assignment(queue,queue4)

    algLCFS=[]
    algFCFS=[]
    algSJF=[]
    algRR=[]

    os.makedirs(name)                                                               # stworzenie folderu o nazwie, w której będą zapisane pliki poniżej liczone i tworzone
    
    file=open(name+"\\LCFS.txt", "w")                                               # tworzy plik w folderze o nazwie wybranej w celu "w" - write

    file.write(f"\n After Last Come First Served algorithm sheduling: \n")          # zapisuje str wszystkie poniższe do tego pliku
    #print(f"\n After Last Come First Served algorithm sheduling: \n")    
    assignment(LCFS(queue1), algLCFS)
    #printarray(algLCFS)
    file.write(f"\n Average turnaround time: \n")
    file.write(str(average_turnaround_time(algLCFS,queue)))
    file.write(f"\n Average waiting time: \n")
    a_wt_LCFS=average_waiting_time(algLCFS,queue)
    file.write(str(a_wt_LCFS))
    file.write(f"\n Standard deviation is: \n") 
    s_d_LCFS=standard_deviation(algLCFS,queue)
    file.write(str(s_d_LCFS))
    figures_of_wt(algLCFS,queue, name+'\\LCFS',a_wt_LCFS, s_d_LCFS,"LCFS")
   
    file.close()                                                                    # zamyka plik, brak możliwości zapisu czego kolwiek do niego 

    file=open(name+"\\FCFS.txt", "w")
 
    file.write(f"\n After First Come First Served algorithm sheduling: \n")    
    #print(f"\n After First Come First Served algorithm sheduling: \n")    
    assignment(FCFS(queue2), algFCFS)
    #printarray(algFCFS)
    file.write(f"\n Average turnaround time: \n") 
    file.write(str(average_turnaround_time(algFCFS,queue)))
    file.write(f"\n Average waiting time: \n")  
    a_wt_FCFS=average_waiting_time(algFCFS,queue)
    file.write(str(a_wt_FCFS))
    file.write(f"\n Standard deviation is: \n") 
    s_d_FCFS=standard_deviation(algFCFS,queue)
    file.write(str(s_d_FCFS))
    figures_of_wt(algFCFS,queue, name+'\\FCFS',a_wt_FCFS, s_d_FCFS,"FCFS")

    file.close()

    file=open(name+"\\SJF.txt", "w")

    file.write(f"\n After Shortest Job First algorithm sheduling: \n") 
    #print(f"\n After Shortest Job First algorithm sheduling: \n") 
    assignment(SJF(queue3), algSJF)
    #printarray(algSJF)
    file.write(f"\n Average turnaround time: \n") 
    file.write(str(average_turnaround_time(algSJF,queue)))
    file.write(f"\n Average waiting time: \n")  
    a_wt_SJF=average_waiting_time(algSJF,queue)
    file.write(str(a_wt_SJF))
    file.write(f"\n Standard deviation is: \n") 
    s_d_SJF=standard_deviation(algSJF,queue)
    file.write(str(s_d_SJF))
    figures_of_wt(algSJF,queue, name+'\\SJF',a_wt_SJF, s_d_SJF,"SJF")

    file.close()

    file=open(name+"\\RR.txt", "w")

    file.write(f"\n After Round Robin algorithm sheduling: \n")
    #print(f"\n After Round Robin algorithm sheduling: \n")
    assignment(RR(queue4), algRR)
    #printarray(algRR)
    file.write(f"\n Average turnaround time: \n") 
    file.write(str(average_turnaround_time(algRR,queue)))
    file.write(f"\n Average waiting time: \n")  
    a_wt_RR=average_waiting_time(algRR, queue)
    file.write(str(a_wt_RR))
    file.write(f"\n Standard deviation is: \n") 
    s_d_RR=standard_deviation(algRR,queue)
    file.write(str(s_d_RR))
    figures_of_wt(algRR,queue, name+'\\RR',a_wt_RR, s_d_RR,"RR")
   
    file.close()