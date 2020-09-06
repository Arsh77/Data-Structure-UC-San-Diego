# python3

from collections import namedtuple

AssignedJob = namedtuple("AssignedJob", ["worker", "started_at"])

def parent(i):
    if(i%2==1):
        return i//2
    elif i>0 and i%2==0:
        return (i//2)
    else:
        return 0
def left(i):
    return 2*i+1
def right(i):
    return 2*(i+1)

"""
def heapify(data,i):
    s=i
    if left(i)<len(data) and data[left(i)][1]<data[i][1]:
        s=left(i)
    elif left(i)<len(data) and data[left(i)][1]==data[i][1] and data[left(i)][0]<data[i][1]:
        s=left(i)
    if right(i)<len(data) and data[right(i)][1]<data[s][1]:
        s=right(i)
    elif right(i)<len(data) and data[right(i)][1]==data[i][1] and data[right(i)][0]<data[i][1]:
        s=right(i)
    if s!=i:
        data[s],data[i]=data[i],data[s]
        heapify(data,s)"""
class worker:
    def __init__(self,key,job):
        self.key=key
        self.job=job

    def __lt__(self,other):
        if self.job==other.job:
            return self.key<other.key
        return self.job<other.job
    
    def __gt__(self,other):
        if self.job==other.job:
            return self.key>other.key
        return self.job>other.job

def heapify(data,i):
    l=left(i)
    r=right(i)
    s=i
    if l<len(data) and data[l]<data[i]:
        s=l
    if r<len(data) and data[r]<data[s]:
        s=r
    if s!=i:
        data[i],data[s]=data[s],data[i]
        heapify(data,s)
        
    
def assign_jobs(n_workers, jobs):
    # TODO: replace this code with a faster algorithm.
    pll = []
    for i in range(n_workers):
        pll.append(worker(i,0))
    result = []
    for job in jobs:
        result.append([pll[0].key,pll[0].job])
        pll[0].job+=job
        heapify(pll,0) 
    return result


def main():
    n_workers, n_jobs = map(int, input().split())
    jobs = list(map(int, input().split()))
    assert len(jobs) == n_jobs

    assigned_jobs = assign_jobs(n_workers, jobs)

    for job in assigned_jobs:
        print(job[0], job[1])


if __name__ == "__main__":
    main()
