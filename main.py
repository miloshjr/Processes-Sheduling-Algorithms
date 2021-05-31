from functions import creation_50
from functions import creation_100
from functions import creation_500
from functions import algorithms

def main():

    queue_50=[]
    queue_100=[]
    queue_500=[]
    queue_50n=[]
    queue_100n=[]
    queue_500n=[]
   
    path1="Data\\Processes1.txt"
    path0="Data\\Processes0.txt"

    #wykonywanie programu dla procesów o różnym czasie przyjśćia

    creation_50(queue_50, path1)
    algorithms(queue_50, "_50_Processes_with_diverse_arrival_time")
    
    creation_100(queue_100, path1)
    algorithms(queue_100, "100_Processes_with_diverse_arrival_time")
    
    creation_500(queue_500, path1)
    algorithms(queue_500, "500_Processes_with_diverse_arrival_time")
    
    #wykonywanie programu dla procesów o tym samym czasie przyjśćia = 0

    creation_50(queue_50n, path0)
    algorithms(queue_50n, "_50_Processes_with equal_arrival_time")
    
    creation_100(queue_100n, path0)
    algorithms(queue_100n, "100_Processes_with_equal_arrival_time")
    
    creation_500(queue_500n, path0)
    algorithms(queue_500n, "500_Processes_with_equal_arrival_time")

if __name__ == "__main__":
    main()
