"""
전보 p 262
입력 조건:
1) 첫째 줄에 도시의 개수 N, 통로의 개수 M, 메시지를 보내고자하는 도시 C
   (1<= N <= 30,000, 1 <= M <= 200,000, 1 <= C <= N)
2) 둘째 줄부터 M+1번째 줄에 걸쳐서 통로에 대한 정보 X, Y, Z가 주어진다.
   이는 특정 도시 X에서 다른 특정 도시 Y로 이어지는 통로가 있으며, 메시지가 전달되는 시간이 Z
   (1 <= X, Y <= N, 1 <= Z <= 1,000)
출력 조건:
   첫째 줄에 도시 C에서 보낸 메시지를 받는 도시의 총 개수와 총 걸리는 시간을 공백으로 구분
"""

import heapq
import sys

#===========================================
#- INPUT
input = sys.stdin.readline
INF = int(1e9)

n, m, start = map(int, input().split())
graph = [[] for i in range(n + 1)]
distance = [INF] * (n + 1)

for _ in range (m):
    x, y, z = map(int, input().split())
    graph[x].append((y,z))
 
def dijkstra(start):
    q = []
    #출발 노드설정, 큐에 삽입
    heapq.heappush(q, (0, start))
    #시작 노드로 가기 위한 최단 경로는 0
    distance[start] = 0
    
    #큐가 비어있지 않다면
    while q:
        #최단 거리 정보 꺼내기, 최소 힙을 이용하는 경우 힙에서 원소를 꺼내면 가장 값이 작은 원소가 추출됨
        dist, now = heapq.heappop(q)
        #현재 간선이 최단 거리가 아니라면 무시
        if distance[now] < dist:
            continue
        #현재 노드와 연결된 다른 인접한 노드들 확인
        for i in graph[now]:
            cost = dist + i[1]
            #현재 노드를 거쳐 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[i[0]]:
                #최단 경로 갱신
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

#알고리즘 수행
dijkstra(start)

#도달할 수 있는 노드의 개수
cnt = 0
#도달할 수 있는 노드 중 가장 멀리 있는 노드와의 최단 거리
max_distance = 0
for i in distance:
    #도달할 수 있는 노드인 경우
    if i != INF:
        cnt+=1
        max_distance = max(max_distance, i)

#시작 노드는 제외해야 하므로 count-1 출력
print(cnt -1, max_distance)