def mergeSortThree(array):
    if(len(arr)>1):
        if(len(arr)%3==0):
            mid1 = len(arr)//3
            mid2 = 2*mid1
            L = arr[:mid1]
            M = arr[mid1:mid2]
            R = arr[mid2:]

            mergeSortThree(L)
            mergeSortThree(M)
            mergeSortThree(R)

            i = j = k = n =0

            while i < len(L) and j < len(R) and n < len(M):
                if (max(L[i],R[j],M[n])==L[i]):
                    arr[k] = L[i]
                    i+=1
                elif (max(L[i],R[j],M[n])==R[j]):
                    arr[k] = R[j]
                    j+=1
                else:
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

            while i < len(L) and j < len(R) and n < len(M):
                if (max(L[i],R[j],M[n])==L[i]):
                    arr[k] = L[i]
                    i+=1
                elif (max(L[i],R[j],M[n])==R[j]):
                    arr[k] = R[j]
                    j+=1
                else:
                    arr[k] = M[n]
                    n+=1
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
                mergeSort(arr)
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

            while i < len(L) and j < len(R) and n < len(M):
                if (max(L[i],R[j],M[n])==L[i]):
                    arr[k] = L[i]
                    i+=1
                elif (max(L[i],R[j],M[n])==R[j]):
                    arr[k] = R[j]
                    j+=1
                else:
                    arr[k] = M[n]
                    n+=1
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

arr = [2,3,1]
mergeSortThree(arr)
print(arr) 
