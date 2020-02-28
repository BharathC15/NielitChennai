echo "Enter the number of terms"
read n
a=1;b=1
echo "0";echo $a;echo $b;
n=`echo "$n-2"|bc`
for i in `seq 1 1 $n`
do
    c=`echo "$a+$b"|bc`
    div=`echo "$b/$c"|bc -l`
    idiv=`echo "$b/$a"|bc -l`
    echo "$c -> $div ->$idiv"
    a=$b;b=$c
    sleep 1
done
