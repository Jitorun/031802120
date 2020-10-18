import time
class QNode(object):#定义队列的数据结构
    def __init__(self, elem, next=None):
        self.elem = elem
        self.next = next

class Queue(object):  # 队列
    def __init__(self):
        self.head = None
        self.rear = None

    def is_empty(self):#判断队列是否为空
        return self.head is None

    def enqueue(self, elem):  # 往队列中添加一个elem元素
        p = QNode(elem)
        if self.is_empty():
            self.head = p
            self.rear = p
        else:
            self.rear.next = p
            self.rear = p

    def dequeue(self):  # 从队列的头部删除一个元素
        result = self.head.elem
        self.head = self.head.next
        return result

    def Search(self,elem):#搜索队列中是否有与elem相同的元素
        temp = self.head
        while temp is not None:
            if elem[:9] == temp.elem[:9]:
                return False
            temp = temp.next
        return True

def jugde(open,closed,temp,i,creatpoint):#判断是否重复
    if open.Search(temp) and closed.Search(temp):
        temp.append(operato[i])
        Open.enqueue(temp)
        creatpoint += 1
    return creatpoint

def  Jugde(sample):#判断有无解
    flag = 0
    for i in sample[::-1]:
        if i != '0':
            this = sample.index(i)
            for x in sample[:this]:
                if x > i:
                    flag += 1
    if flag % 2 ==0 :
        return 0
    return 1

if __name__ == '__main__':
    sample = list(input('请输入初始状态：').split())#存储8数码问题的初始状态
    goal = list(input('请输入目标状态：').split(' '))#存储8数码问题的目标状态
    m = Jugde(sample)
    n = Jugde(goal)
    if m != n:#通过求逆序数判断有无解
        print('无解！')
        exit()
    operato = ['up','down','left','right']
    k = creatpoint = 0 # k 为搜索的节点数 creatpoint 为生成节点数
    Open = Queue()#创建open表
    Closed = Queue()#创建closed表
    Open.enqueue(sample)
    Max = input("请输入最大搜索深度：")
    start = time.time()
    while(1):
        if(sample == goal ):
            print("起始节点为目标结点！")
            break
        if Open.is_empty():
            print("没有解！")
            break
        else:
            p = Open.dequeue()#从Open表中取出
            if len(p)-9 >= int(Max)+1:#判断是否超过设置的最大深度
                print('已达最大深度，未找到解！')
                exit()
            Closed.enqueue(p)#放入Closed表中
            if p[:9] == goal:#判断是否相等
                k += 1
                print('当前层次：{},已搜索节点数:{},已生成结点数{}\n查找成功！'.format(len(p)-9,k,creatpoint))
                print("空格的移动路径依次为：",end = '')
                for i in p[9:]:
                    print(i,end='->')
                end = time.time()
                print('完成\nRunning time:{} Seconds'.format(end - start))
                exit()
            k += 1
            flag = p.index('0')# 返回列表中0的索引  flag = p.index('0')
            if flag - 3 >= 0 :#空格向上移动
                temp = p.copy()
                temp[flag], temp[flag - 3] = temp[flag - 3], temp[flag]
                creatpoint = jugde(Open,Closed,temp,0,creatpoint)
            if flag + 3 <= 8:#空格向下移动
                temp = p.copy()
                temp[flag], temp[flag + 3] = temp[flag + 3], temp[flag]
                creatpoint = jugde(Open, Closed, temp, 1, creatpoint)
            if flag % 3 != 0 :#空格向左移动
                temp = p.copy()
                temp[flag], temp[flag - 1] = temp[flag - 1], temp[flag]
                creatpoint = jugde(Open, Closed, temp, 2, creatpoint)
            if (flag + 1) % 3 != 0:#空格向右移动
                temp = p.copy()
                temp[flag], temp[flag + 1] = temp[flag + 1], temp[flag]
                creatpoint = jugde(Open, Closed, temp, 3, creatpoint)
