"""
O(V^2)
# 입력되는 데이터가 많다고 가정
# input() 동작을 더 빠르게 하는 sts.std.realine()으로 치환
# 모든 리스트는 (노드의 개수 + 1) 크기로 할당
"""
import sys
input = sys.stdin.readline
# 10억 ~ 무한을 의미
INF = int(1e9)


#1. 출발 노드 설정
n, m = map(int, input().split())
start = int(input())

# 리스트 만들기
#1) 각 노드에 연결되어 있는 노드 정보를 담는 리스트
graph = [ [] for i in range(n+1) ]
#2) 모든 간선 정보 입력 담는 리스트
for _ in range(m):
    # Node: a, b, Cost: c (a to b)
    a, b, c = map(int, input().split())
    # 각 행(Node a)을 기준으로 첫번째 원소(Node b)와의 비용(Cost c)을 리스트 형태의 튜플로 표현
    graph[a].append((b,c))
#3) 방문 유무 체크 리스트
visited = [False] * (n+1)

#2. 최단 거리 테이블 초기화
distance = [INF] * (n+1)

#3. 방문하지 않은 노드 중 최단 거리 노드의 번호를 반환    
def get_smallest_node():
    min_value = INF
    index = 0
    for i in range(1, n+1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index

def dijkstra(start):
    #1. 출발 노드(start=Node a) 초기화
    distance[start] = 0
    visited[start] = True
    #2. 최단 거리 테이블 초기화
    for j in graph[start]:
        #j[0] Node b, j[1] Cost c
        distance[j[0]] = j[1]
    #시작 노드를 제외한 전체 n-1개의 노드에 대해 반복
    for i in range(n-1):
        #3. 방문하지 않은 노드 중 최단 거리 노드를 꺼내어 방문 처리
        now = get_smallest_node()
        visited[now] = True
        
        for j in graph[now]:
            #4. 현재 노드와 연결된 다른 노드를 비용 확인
            cost = distance[now] + j[1]
            # 현재 노드를 거쳐 다른 노ㄷ로 이동하는 거리가 더 짧은 경우
            if cost < distance[j[0]]:
                #5. 최단 거리 테이블 갱신
                distance[j[0]] = cost
            
dijkstra(start)

# 각 노드에 대한 최단 거리 출력
for i in range(1, n+1):
        if distance[i] == INF:
            print("INFINITY")
        else:
            print(distance[i])
