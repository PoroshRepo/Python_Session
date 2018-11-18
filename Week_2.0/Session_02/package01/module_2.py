
def mean(numbers):
    sum_n = 0
    length = len(numbers)
    for num in numbers:
        sum_n = sum_n + num
    
    res = sum_n / length
    
    print("Mean of the list is "+str(res))
        

def divList(base_number, main_list):
    sum_d = 0
    
    
    for list_elements in main_list:
        try:   
            sum_d = sum_d + (base_number/list_elements)
        
        except:
            continue
    
    
    print("The result is: "+str(sum_d))
