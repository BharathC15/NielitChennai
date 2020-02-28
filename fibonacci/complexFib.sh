#Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
a=0
b=1
c=0
sum=0
echo "Enter the largest term"
read n
while [ $(echo "$a+$b" | bc) -le $n ]
do
    c=$(echo "$a+$b" | bc)
    echo "$c"
    if [ $(echo "$c % 2" | bc) -eq 0 ]
    then
        sum=$(echo "$sum + $c" | bc)
    fi
    a=$b
    b=$c
done
echo "The sum of the even fibonacci numbers is $sum"