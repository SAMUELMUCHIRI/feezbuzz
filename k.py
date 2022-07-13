def feezbuzz(x):
    st=0
    while st<x:
        if st%15==0:
            print("feezbuzz")
        elif st%3==0:
            print("feez")
        elif st%5==0:
            print("buzz")
        else:
            print(st)
        st=st+1
feezbuzz(100)
