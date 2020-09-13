Line1=input().split()
Value=[int(I) for I in Line1]
Value.sort()
print(*Value, sep='\n')
print()
print(*Line1,sep='\n')