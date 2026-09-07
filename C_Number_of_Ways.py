n = int(input())
a = list(map(int, input().split()))

total = sum(a)

if total % 3 != 0:
    print(0)
else:
    target = total // 3
    ans = 0
    prefix = 0
    cnt = 0

    for i in range(n - 1):
        prefix += a[i]

        if prefix == 2 * target:
            ans += cnt

        if prefix == target:
            cnt += 1

    print(ans)