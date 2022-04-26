import thread, time, random
def molesta(missatge):
  while True:
    time.sleep(random.randint(1, 3))
    print(missatge)
    
    thread.start_new_thread(molesta, ('Booh !!',))
    
    x = 0
    while True:
      print(x)
      x += 1
      time.sleep(1)
                                      
