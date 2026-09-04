t = int(input())

for _ in range(t):
    n = int(input())
    s = input()
    
    freq_b = {}
    for char in s:
        freq_b[char] = freq_b.get(char, 0) + 1
        
    seen_a = set()
    max_sum = 0
    
    for char in s:
        seen_a.add(char)
        freq_b[char] -= 1
        if freq_b[char] == 0:
            del freq_b[char]
            
        current_sum = len(seen_a) + len(freq_b)
        if current_sum > max_sum:
            max_sum = current_sum
            
    print(max_sum)