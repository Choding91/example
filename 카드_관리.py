n, m = map(int, input().split())  # 잔액, 거래 횟수

reservation = []  # 대기 목록

for i in range(m):
    method, k = input().split()  # 거래 종류, 액수
    k = int(k)

    if method == "deposit":
        n += k
        if reservation:  # 대기 목록 확인
            if n >= reservation[0]:
                n -= reservation[0]
            else:
                continue

    elif method == "pay":
        if n >= k:
            n -= k
        else:
            continue

    elif method == "reservation":
        if n >= k:
            n -= k
        else:
            reservation.append(k)  # 대기 목록 추가

print(n)

'''
[ 입력 ]
0 6
deposit 10
reservation 20
pay 5
deposit 10
deposit 10
reservation 6
[ 출력 ]
5

[ 입력 ]
0 6
deposit 10
pay 5
reservation 5
reservation 5
pay 5
deposit 10
[ 출력 ]
5
'''