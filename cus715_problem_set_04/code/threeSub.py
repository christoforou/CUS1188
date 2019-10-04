def mergeSortThree(arr):
    if(len(arr)>1):
        if(len(arr)>2 and len(arr)%3==0):
            mid1 = len(arr)//3
            mid2 = 2*mid1
            L = arr[:mid1]
            M = arr[mid1:mid2]
            R = arr[mid2:]

            mergeSortThree(L)
            mergeSortThree(M)
            mergeSortThree(R)

            i = j = k = n =0

            while (i < len(L) and j < len(R) and n < len(M)):
                if (min(L[i],R[j],M[n])==L[i]): 
                    arr[k] = L[i]
                    i+=1
                elif (min(L[i],R[j],M[n])==R[j]):
                    arr[k] = R[j]
                    j+=1
                else:
                    arr[k] = M[n]
                    n+=1
                k+=1

            while (i < len(L) and j < len(R)):
                if (L[i] < R[j]):
                    arr[k] = L[i]
                    i+=1
                else:
                    arr[k] = R[j]
                    j+=1
                k+=1
            while (j < len(R) and n < len(M)):
                if (M[n] < R[j]):
                    arr[k] = M[n]
                    n+=1
                else:
                    arr[k] = R[j]
                    j+=1
                k+=1
            while (n < len(M) and i < len(L)):
                if (M[n] < L[i]):
                    arr[k] = M[n]
                    n+=1
                else:
                    arr[k] = L[i]
                    i+=1
                k+=1

            while (i < len(L)):
                arr[k] = L[i]
                i+=1
                k+=1

            while (j < len(R)):
                arr[k] = R[j]
                j+=1
                k+=1

            while (n < len(M)):
                arr[k] = M[n]
                n+=1
                k+=1

        elif(len(arr)%3==1):
            mid1 = len(arr)//3
            mid2 = 2*mid1
            L = arr[:mid1]
            M = arr[mid1:mid2]
            R = arr[mid2:]
            mergeSortThree(L)
            mergeSortThree(M)
            mergeSortThree(R)

            i = j = k = n =0

            while (i < len(L) and j < len(R) and n < len(M)):
                if (min(L[i],R[j],M[n])==L[i]):
                    arr[k] = L[i]
                    i+=1
                elif (min(L[i],R[j],M[n])==R[j]):
                    arr[k] = R[j]
                    j+=1
                else:
                    arr[k] = M[n]
                    n+=1
                k+=1

            while (i < len(L) and j < len(R)):
                if (L[i] < R[j]):
                    arr[k] = L[i]
                    i+=1
                else:
                    arr[k] = R[j]
                    j+=1
                k+=1

            while (j < len(R) and n < len(M)):
                if (M[n] < R[j]):
                    arr[k] = M[n]
                    n+=1
                else:
                    arr[k] = R[j]
                    j+=1
                k+=1

            while (n < len(M) and i < len(L)):
                if (M[n] < L[i]):
                    arr[k] = M[n]
                    n+=1
                else:
                    arr[k] = L[i]
                    i+=1
                k+=1

            while (i < len(L)):
                arr[k] = L[i]
                i+=1
                k+=1

            while (j < len(R)):
                arr[k] = R[j]
                j+=1
                k+=1

            while (n < len(M)):
                arr[k] = M[n]
                n+=1
                k+=1
        else:
            if(len(arr)//3==0):
                L = arr[0]
                M = arr[1]

                arr[0]=min(L,M)
                arr[1]=max(L,M)
            else:
                mid1 = len(arr)//3
                mid2 = 2*mid1+1
                L = arr[:mid1]
                M = arr[mid1:mid2]
                R = arr[mid2:]

                mergeSortThree(L)
                mergeSortThree(M)
                mergeSortThree(R)

                i = j = k = n =0

                while (i < len(L) and j < len(R) and n < len(M)):
                    if (min(L[i],R[j],M[n])==L[i]):
                        arr[k] = L[i]
                        i+=1
                    elif (min(L[i],R[j],M[n])==R[j]):
                        arr[k] = R[j]
                        j+=1
                    else:
                        arr[k] = M[n]
                        n+=1
                    k+=1

                while (i < len(L) and j < len(R)):
                    if (L[i] < R[j]):
                        arr[k] = L[i]
                        i+=1
                    else:
                        arr[k] = R[j]
                        j+=1
                    k+=1

                while (j < len(R) and n < len(M)):
                    if (M[n] < R[j]):
                        arr[k] = M[n]
                        n+=1
                    else:
                        arr[k] = R[j]
                        j+=1
                    k+=1

                while (n < len(M) and i < len(L)):
                    if (M[n] < L[i]):
                        arr[k] = M[n]
                        n+=1
                    else:
                        arr[k] = L[i]
                        i+=1
                    k+=1

                while (i < len(L)):
                    arr[k] = L[i]
                    i+=1
                    k+=1

                while (j < len(R)):
                    arr[k] = R[j]
                    j+=1
                    k+=1

                while (n < len(M)):
                    arr[k] = M[n]
                    n+=1
                    k+=1

arr = [9,5,7,6,8,3,1,4,2]
mergeSortThree(arr)
print(arr)
