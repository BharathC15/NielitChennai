print('Both names should be either in capital or small cases, then only the result will be correct')

Boy = input('Enter the boy name in capital letters :')
Girl = input('Enter the girl name in capital letters :')

if Boy == Girl:
 exit()

Boy_list = list(Boy)
Girl_list = list(Girl)

print(Boy_list)
print(Girl_list)

length_boy = len(Boy)
length_girl = len(Girl)

print('The length of the Boy characters are', length_boy)
print('The length of the Girl characters are', length_girl)

common_count=0

for a in Boy_list:
 print('The letter is :',a)
 if a in Girl_list:
  common_count +=2
  del(Girl_list[Girl_list.index(a)])
  print('letters present in boy list is', Boy_list)
  print('Letters present in girl is', Girl_list)
  

print('the common count is', common_count)


Total_Count = length_boy+length_girl-common_count
print('The Total count to calculate is', Total_Count)
  
  
FLAMES = ['F','L','A','M','E','S']

len_flames = len(FLAMES)
print('The total length of the word FLAMES is', len_flames)


while len_flames > 1:
 remainder = Total_Count % len_flames
 print('The total to be counted is', remainder)

 if remainder:
  FLAMES = FLAMES[remainder:] + FLAMES[:remainder-1]

 else:
  FLAMES = FLAMES[:remainder-1]

 print('the character is', FLAMES)
 len_flames = len(FLAMES)
 print('The length of the flames is: ',len(FLAMES))


print('The final outcome is......', FLAMES)
print('Result is :', FLAMES)

print('ALL THE BEST')


