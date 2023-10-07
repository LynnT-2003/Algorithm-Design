debit = [65635
,3400
,950
,460
,10325
,22000
,675
,150
,1000
]

credit = [2500
,4645
,300
,9000
,85000
,3000
,150
]

sum = 0
for i in range(len(debit)):
  sum += debit[i]

sum_cr = 0
for i in range(len(credit)):
  sum_cr += credit[i]

print(sum)
print(sum_cr)
print(104595-sum)