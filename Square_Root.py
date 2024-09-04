def Square_Root_Target_Value(Target_value,tolerance=1e-7,max_iterations=100):
    if Target_value<0:
        raise ValueError('square root of negative value is not real number')
    if Target_value==1:
        root=1
        print(f'square root of {Target_value} is {root}')
    elif Target_value==0:
        root=0
        print(f'square root of {Target_value} is {root}')
    else:
        low=0
        high=max(1,Target_value)
        root = None
        for _ in range(max_iterations):
            mid=(low+high)/2
            square_mid=mid**2
            if abs(square_mid-Target_value)<tolerance:
                root=mid
            elif square_mid<Target_value:
                low=mid
            else:
                high=mid
    if root is None:
        print(f'Failed to converge within {max_iterations} iterations')
    else:
        print(f'The square root of {Target_value} is approximately {root}')
    return root
X=25
Square_Root_Target_Value(X)

