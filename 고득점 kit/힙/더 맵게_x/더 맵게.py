import heapq as hq
def solution(scoville, K):
    hq.heapify(scoville)
    cnt=0
    while scoville[0]<K and len(scoville)>1:
        cnt+=1
        a = hq.heappop(scoville)
        b = hq.heappop(scoville)
        c = a+(b*2)
        hq.heappush(scoville,c)
    
    return cnt if scoville[0]>=K else -1
