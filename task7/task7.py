def task7_23435_1():
    scr_size = 2560*1440
    i = 32
    scr_size_compressed = 1920*1080
    i_compressed = 31
    count = 110
    res1 = scr_size * i 
    res2 = scr_size_compressed * i_compressed
    res = res1 * 110 - res2 * 110
    print(res / 8 / 1024)

def task7_21406_2():
    size = 3840 * 2160
    i = 17
    size_c = 1280*720
    i_c = 5
    count = 120
    res1 = size * i
    res2 = size_c * i_c
    print(((res1 - res2) * 120) / 8 / 1024)

def task7_17861_3(): #41
    size = 1024 * 768
    i = 12
    speedbps = 1_310_720
    t = 300
    r1 = speedbps * t
    r2 = size * i
    print(r1 / r2)

def task7_23553_4(): # 396000
    size = 1920 * 1080
    i = 32
    size_c = 1280*1024
    i_c = 30
    count = 120
    res1 = size * i
    res2 = size_c * i_c
    print(((res1-res2) * 120) / 8 / 1024)

def task7_19239_5(): # 292
    size = 3840*2160
    i = 24
    c = 3742
    max_memb = 16 * 1024 * 1024 * 1024 * 8
    memb = c * i * size
    print(memb / max_memb)
    print(memb, max_memb*5)
    print('-----')
    print(c % ((max_memb) // (size * i)))
task7_19239_5()