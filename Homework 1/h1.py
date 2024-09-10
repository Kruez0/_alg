# 方法 a
def power2n_a(n):
    return 2**n

# 方法 b：用遞迴
def power2n_b(n):
    if n == 0: return 1
    return power2n_b(n-1)+power2n_b(n-1)

# 方法 c：用遞迴
def power2n_c(n):
    # pass
    if n == 0: return 1
    return 2*power2n_c(n-1)

# 方法 d：用遞迴+查表
Power2n_d=[None]*100
def power2n_d(n):
    if n==0:return 1
    if not Power2n_d[n] is None: return Power2n_d[n]
    else:
        Power2n_d[n]=power2n_d(n-1)+power2n_d(n-1) 
    return Power2n_d[n]
print('power2n(10)=', power2n_d(40))