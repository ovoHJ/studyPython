for i in range(2,9+1):
    for j in range(1, 9+1):
        if i > 7:
            break
        if j%2 == 0 :
            continue
        print(i, "×", j, "=", i*j)
    print("-------------")