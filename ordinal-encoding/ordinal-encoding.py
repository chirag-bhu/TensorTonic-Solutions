def ordinal_encoding(values, ordering):
    """
    Encode categorical values using the provided ordering.
    """
    # Write code here
    hmap={}
    result=[]
    for i in range(len(ordering)):
        hmap[ordering[i]]=i
    for j in range(len(values)):
        ans=hmap[values[j]]
        result.append(ans)
    return result