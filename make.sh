#lmp_serial -in start.h

for (( a = 1; a <= 3; a++ ))
    do
        echo "$a"
        for (( b = 1; b <= 3; b++ ))
        do
            echo "$b"
        done
    done
