#!/bin/bash

ls *.sh > execfile
while read LINE
do
	echo $LINE
done<execfile
