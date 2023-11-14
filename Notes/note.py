def printRev( n ):
    if n > 0 :
        print( n )
        printRev( n-1 )


printRev(4)
