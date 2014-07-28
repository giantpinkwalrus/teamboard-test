i=0
mkdir "logs"
while [ 1 ]
do
        ((i++))
        fmbt test.conf | tee logs/log$i.xml
done
