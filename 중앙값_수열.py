n = int(input())  # arr의 길이
arr = list(map(int, input().split()))  # 수열의 값들

list = []  # 배열
result = []  # 결과

for i in range(n):
    list.append(arr[i])
    list.sort()

    if len(list) % 2 == 0:  # 짝수 길이의 작은 중앙값
        result.append(list[int(len(list) / 2 - 1)])
    else:  # 홀수 길이의 중앙값
        result.append(list[int(len(list) / 2)])

print(*result)  # 언패킹

"""
[ 입력 ]
5
1 5 3 -1 3
[ 출력 ]
1 1 3 1 3

[ 입력 ]
5
0 -1 -2 -3 -4
[ 출력 ]
0 -1 -1 -2 -2
"""
