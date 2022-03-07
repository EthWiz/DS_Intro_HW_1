def convert(hours, minutes=0):
    
    if (hours<0 or minutes<0):
        print("input error!")
    else:
        second= (hours*60*60+minutes*60)
        print(second)