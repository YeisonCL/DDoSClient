import threading, os, time, getopt, sys

controlFlagThreads = True

def exitStress():
    print("Cerrando todos los hilos...");
    global controlFlagThreads
    controlFlagThreads = False
    
def stress(pClient, pUrlDirection, pThreadNumber):
    while(controlFlagThreads):
        if(pClient[-1] == "c"):
            os.system("./httpclient -u " + pUrlDirection)
            time.sleep(0.5)
        else:
            os.system("python ../ClientsHTTP/" + pClient + " -u " + pUrlDirection)
            time.sleep(0.5)
    print("Cerrando hilo " + str(pThreadNumber) + "...")

def initializeStress(pThreads, pClient, pUrlDirection):
    threads = list()
    for i in range(int(pThreads)):
        thread = threading.Thread(target=stress, args=(pClient, pUrlDirection, i,))
        threads.append(thread)
        thread.start()
    exitCondition = ""
    while(exitCondition != "exit"):
        exitCondition = input()
    exitStress()
    
def main():
    try:
        controlFlag = False
        opts, args = getopt.getopt(sys.argv[1:], "n:c:u:h", ["threads=","client=","url=", "help"])
    except getopt.GetoptError as err:
        print(err)
        sys.exit(2)
    for o, a in opts:
        controlFlag = True
        if o in("-h", "--help"):
            print("\nUso: stressCMD -n [THREADS] -c [CLIENT] -u [URL]\n\n")
            print("Argumentos:\n\n")
            print("-n \t THREADS \t Cantidad de threads que seran usados para realizar las peticiones")
            print("-c \t CLIENT \t Cliente que sera usado para realizar las peticiones")
            print("-u \t URL \t Direccion a la cual se haran las consultas")
            sys.exit(1)
        elif o in("-n", "--threads"):
            threads = a
        elif o in("-c", "--client"):
            client = a
        elif o in("-u", "--url"):
            urlDirection = a
        else:
            assert False, "Opcion invalida"
    if(controlFlag == True):
        print("Iniciando ataque DDoS...")
        if(client[-1] == "c"):
            os.system("gcc -Wall -std=c99 ../ClientsHTTP/httpclient.c -o httpclient")
        initializeStress(threads, client, urlDirection)
    else:
        print("Por favor digite los parametros de configuracion, utilice la opcion -h para mayor informacion.")        

if __name__ == "__main__":
    main()
