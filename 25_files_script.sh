#!/bin/bash

i=0

fileName="rashmi-"

extension=".txt"

fullFileName=""

startFileIndex=0

endFileIndex=0



while true; do 

	i=$((i+1))

	fullFileName="$fileName$i$extension"

	echo "Testing $fullFileName"

	if test -f "$fullFileName"; then

		echo "exists"

		continue

	else 

		startfileIndex=$i

		endFileIndex=$((i+25))

		for (( j = $startFileIndex; j < $endFileIndex; j++))

		do

			fullFileName="$fileName$j$extension"

			touch $fullFileName

			echo $fullFileName

		done

		break

	fi

done


