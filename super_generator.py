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
    id = getRandPersonId(0)
    name = getRandStr()
    age = random.randint(0, 201)
    return ' '.join(['ap', id, ''.join(name), age.__str__()])

def getAr()->str:
    return ' '.join(['ar', getRandPersonId(1), getRandPersonId(1), str(random.randint(1,101))])

def getQlm():
    return ' '.join(['qlm', getRandPersonId(1)])
            
def superQlm():
    for i in range(2000):
        print(getAp())
    for i in range(4000):
        print(getAr())
    for i in range(4000):
        print(getQlm())

    