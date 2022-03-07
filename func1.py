def my_func(x1, x2, x3):
    try:
        sum1=𝒙𝟏+𝒙𝟐+𝒙𝟑
        sum2=𝒙𝟐+𝒙𝟑
        mone=sum1*sum2*x3
        mechane=𝒙𝟏+𝒙𝟐+𝒙𝟑
        calculate= mone/mechane
        if mechane == 0:
            return 'Not a number – denominator equals zero'
        else:
            return calculate
    except:
        return 'Error: parameters should be float'

print(my_func("want",3.2,8884.1))

