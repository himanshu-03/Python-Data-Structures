class Q:
    queue = []
    MaxSize = 0
    currSize = 0

    def createQueue(self, size):
        Q.MaxSize = size
        Q.currSize = 0
        for i in range(0, Q.MaxSize):
            Q.queue.append(0)
        print('\nQueue created of size: ', len(Q.queue))
        print(Q.queue)

    def enqueue(self, e):
        Q.currSize += 1
        Q.queue[Q.currSize-1] = e
        Q.shiftUp(Q.currSize-1)
        print(e, 'enqueued in Queue')
        print('')

    def dequeue(self):
        temp = Q.queue[0]
        Q.currSize -= 1
        Q.queue[0] = Q.queue[Q.currSize]
        Q.shiftDown(0)
        print(temp, 'dequeued from Queue')
        print('')

    def isFull(self):
        if Q.currSize == Q.MaxSize:
            return True
        else:
            return False

    def isEmpty(self):
        if Q.currSize == 0:
            return True
        else:
            return False

    def printQueue(self):
        print('Position', '\tData')
        for i in range(Q.currSize):
            print(i+1,'\t\t',Q.queue[i])
    
    def shiftUp(i) : 
        parent = (i - 1) // 2
        while (i > 0 and Q.queue[parent] < Q.queue[i]) :
            
            # Swap parent and current node 
            (Q.queue[i], Q.queue[parent]) = (Q.queue[parent], Q.queue[i]) # swap
        
            # Update i to parent of i 
            i = parent
            parent = (i - 1) // 2
    
    def shiftDown(i):
        largest = i # Initialize largest as root
        l = 2 * i + 1 # left = 2*i + 1
        r = 2 * i + 2 # right = 2*i + 2

        # See if left child of root exists and is
        # greater than root

        if l < Q.currSize and Q.queue[i] < Q.queue[l]:
            largest = l

        # See if right child of root exists and is
        # greater than root

        if r < Q.currSize and Q.queue[largest] < Q.queue[r]:
            largest = r

        # Change root, if needed

        if largest != i:
            (Q.queue[i], Q.queue[largest]) = (Q.queue[largest], Q.queue[i]) # swap
            Q.shiftDown(largest)



# Main Code:

o = Q()
o.createQueue(int(input('Enter size of the queue: ')))

while True:
    print('------------')
    print('1.Enqueue\n2.Dequeue\n3.Print\n0.Exit')
    print('------------')

    ch = int(input('\nEnter your choice: '))

    if ch == 1:
        if o.isFull() != True:
            data = int(input('\nEnter data to be enqueued: '))
            o.enqueue(data)
        else:
            print('\nQueue is full..\n')

    elif ch == 2:
        if o.isEmpty() != True:
            o.dequeue()
        else:
            print('\nQueue is empty..\n')

    elif ch == 3:
        if o.isEmpty() != True:
            o.printQueue()
        else:
            print('\nQueue is empty..\n')

    elif ch == 0:
        break

    else:
        print('\nWrong Input..\nEnter the correct choice..!!\n')