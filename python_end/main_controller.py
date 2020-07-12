import obs,parenty,socket_controller,threading

def callObs():
    obs.main()

socket_controller.init_comm_file()
t = threading.Thread(target = callObs, args=())
t.start()
