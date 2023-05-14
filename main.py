import os
import threading
import datetime
jars = ['待测jar包1.jar', '待测jar包2.jar', '待测jar包3.jar']  #存放待测的jar包
max = 1                             #测试的次数
instructions_num = 10000             #每个测试点的指令数

def runTest(n:int):
    
    dir = 'test' + str(n)
    if not os.path.exists(dir):
        os.mkdir(dir)
    for file in os.listdir(dir):
        os.remove(os.path.join(dir, file))
    
    dataPath = os.path.join('./' + dir, 'data')    
    os.system('python generator.py ' + instructions_num.__str__() + ' >' + dataPath)     #30000代表每个数据集的指令数量
    for jar in jars:
        start = datetime.datetime.now()
        os.system('Reader.exe ' + dataPath + ' | java -jar ' + jar + '>' + os.path.join(dir, jar + '.out'))
        print(jar + ' in test ' + str(n) + ' finished! time:' + str((datetime.datetime.now() - start).total_seconds()))

    outputs = []
    fileName = []
    for file in os.listdir(dir):
        if file.endswith('out'):
            outputs.append(open(os.path.join(dir, file)).readlines())
            fileName.append(file)
    dataLines = open(dataPath).readlines()

    for i in range(0, len(outputs[0])):
        std = outputs[0][i]
        for j in range(0, len(outputs)):
            if outputs[j][i] != std:
                print('something wrong at ' + str(i + 1) + ' line in test ' + str(n))
                print('The instruction is ' + dataLines[i].strip())
                for k in range(0, len(outputs)):
                    print(fileName[k] + ':\t' + outputs[k][i].strip())
                print('')
                break
    
    print(dir + ' finished!')

thread_num = 8
n = 1
lock = threading.Lock()
def runThread():
    global n
    while True:
        lock.acquire()
        if n > max:
            lock.release()
            break
        num = n
        n += 1
        lock.release()
        runTest(num)

for i in range(thread_num):
    t = threading.Thread(target=runThread)
    t.start()