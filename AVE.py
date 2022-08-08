
last_number = int(input("Enter last number: "))
total_list=[]



for num in range(2,last_number + 1):

    if num > 1:
        for i in range(2,num):
            if (num % i) == 0:
            
            break
            
            
        else:
                   total_list.append(num)
                  
     sum=0
     for i in total_list:
     sum += i
     
     print( 'Sum of all Prime numbers= %d' %sum)
     
     def Average(total_sum, total_length):
      total_average = total_sum / total_length 
       return total_average 
       
       average = Average( float(sum), len(total_list))
       
       print(average)
       
       
                   
                   
 
 
 
