spam = ['apples', 'bananas', 'tofu', 'cats', 1, 'origin', 'hsbl', 'boeing', 2234, 'foxtrot']

if spam:
    
    for i in range(len(spam)):
        
        if i == len(spam) - 1:
            
            print('and ' + str(spam[i]) + '.')

        else:
            
            print(str(spam[i]) + ', ', end='')
            
