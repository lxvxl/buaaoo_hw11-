import random
import sys

persons = set()
groups = set()
messages = set()
emojis = set()
maxPersonId = 10000
maxGroupId = 500
maxMessageId = 500
maxEmojiId = 500

def getRandPersonId(p:float=0.8)->str:
    '''
        生成一个随机的personId。有p的可能id是已经出现过的
    '''
    if len(persons) != 0 and random.randint(0, 100) < 100 * p:
        return random.choice(list(persons)).__str__()
    newPersonId = random.randint(-maxPersonId, maxPersonId)
    persons.add(newPersonId)
    return str(newPersonId)

def getRandGroupId(p:float=0.8)->str:
    '''
        生成一个随机的groupId。有p的可能id是已经出现过的
    '''
    if len(groups) != 0 and random.randint(0, 100) < 100 * p:
        return random.choice(list(groups)).__str__()
    newGroupId = random.randint(0, maxGroupId)
    groups.add(newGroupId)
    return str(newGroupId)

def getRandMessageId(p:float=0.8)->str:
    '''
        生成一个随机的messageId。有p的可能id是已经出现过的
    '''
    if len(messages) != 0 and random.randint(0, 100) < 100 * p:
        return random.choice(list(messages)).__str__()
    newMessageId = random.randint(0, maxMessageId)
    messages.add(newMessageId)
    return str(newMessageId)

def getRandStr():
    return ''.join([random.choice('kjhiuhkjsad8123askj') for i in range(random.randint(1, 10))])

def getRandEmojiId(p:float=0.8)->str:
    '''
        生成一个随机的emojiId。有p的可能id是已经出现过的
    '''
    if len(emojis) != 0 and random.randint(0, 100) < 100 * p:
        return random.choice(list(emojis)).__str__()
    newEmojiId = random.randint(0, maxEmojiId)
    emojis.add(newEmojiId)
    return str(newEmojiId)

def getAp()->str:
    id = getRandPersonId(0.2)
    name = getRandStr()
    age = random.randint(0, 201)
    persons.add(id)
    return ' '.join(['ap', id, ''.join(name), age.__str__()])

def getAr()->str:
    return ' '.join(['ar', getRandPersonId(0.8), getRandPersonId(0.8), str(random.randint(1,101))])

def getQv()->str:
    return ' '.join(['qv', getRandPersonId(0.8), getRandPersonId(0.8)])

def getQci()->str:
    return ' '.join(['qci', getRandPersonId(0.8), getRandPersonId(0.8)])

def getQbs():
    return 'qbs'

def getQts():
    return 'qts'

def getAg():
    id = getRandGroupId(0.2)
    groups.add(id)
    return ' '.join(['ag', id])

def getAtg():
    id1 = getRandPersonId(0.8)
    id2 = getRandGroupId(0.8)
    return ' '.join(['atg', id1, id2])

def getDfg():
    id1 = getRandPersonId(0.8)
    id2 = getRandGroupId(0.8)
    return ' '.join(['dfg', id1, id2])

def getQgvs():
    return ' '.join(['qgvs', getRandGroupId()])

def getQgav():
    return ' '.join(['qgav', getRandGroupId()])

def getMr():
    return ' '.join(['mr', getRandPersonId(0.8), getRandPersonId(0.8), str(random.randint(-100,101))])

def getQba():
    return ' '.join(['qba', getRandPersonId(0.8)])

def getQcs():
    return 'qcs'

def getAm():
    type = random.randint(0,1)
    if type == 0:
        return ' '.join(['am', getRandMessageId(0.2), str(random.randint(-1000, 1001)), str(type), getRandPersonId(1), getRandPersonId(1)])
    else :
        return ' '.join(['am', getRandMessageId(0.2), str(random.randint(-1000, 1001)), str(type), getRandPersonId(1), getRandGroupId(1)])

def getSm():
    return ' '.join(['sm', getRandMessageId()])

def getQsv():
    return ' '.join(['qsv', getRandPersonId()])

def getQrm():
    return ' '.join(['qrm', getRandPersonId()])

def getArem():
    type = random.randint(0,1)
    if type == 0:
        return ' '.join(['arem', getRandMessageId(0.2), str(random.randint(0, 1001)), str(type), getRandPersonId(1), getRandPersonId(1)])
    else :
        return ' '.join(['arem', getRandMessageId(0.2), str(random.randint(0, 1001)), str(type), getRandPersonId(1), getRandGroupId(1)])

def getAnm():
    type = random.randint(0,1)
    if type == 0:
        return ' '.join(['anm', getRandMessageId(0.2), getRandStr(), str(type), getRandPersonId(1), getRandPersonId(1)])
    else :
        return ' '.join(['anm', getRandMessageId(0.2), getRandStr(), str(type), getRandPersonId(1), getRandGroupId(1)])

def getCn():
    return ' '.join(['cn', getRandPersonId()])

def getAem():
    type = random.randint(0,1)
    if type == 0:
        return ' '.join(['aem', getRandMessageId(0.2), getRandEmojiId(), str(type), getRandPersonId(1), getRandPersonId(1)])
    else :
        return ' '.join(['aem', getRandMessageId(0.2), getRandEmojiId(), str(type), getRandPersonId(1), getRandGroupId(1)])

def getSei():
    return ' '.join(['sei', getRandEmojiId(0.2)])

def getQp():
    return ' '.join(['qp', getRandEmojiId()])

def getDce():
    return ' '.join(['dce', str(random.randint(0, 5))])

def getQm():
    return ' '.join(['qm', getRandPersonId()])

def getQlm():
    return ' '.join(['qlm', getRandPersonId()])

instructions = [getAp, getAr, getQv, getQci, getQbs, getQts, getAg, getAtg, getDfg, getQgvs, getQgav, getMr, getQba, getQcs, getAm, getSm, getQsv, getQrm,
               getArem, getAnm, getCn, getAem, getSei, getQp, getDce, getQm, getQlm]

if __name__ == '__main__':
    n = int(sys.argv[1])
    for i in range(n):
        inst = ''
        while inst == '':
            inst = random.choice(instructions)()
        print(inst)
    