fruits = {'fruit': 'apple', 'color': 'green'}



def longest_value(dictionary):
    store = 0
    result = ""
    
    for value in dictionary.values():
        temp = len(value)
        if(store<temp):
            store = temp
            result = value
            
    print(result)
    
longest_value(fruits)