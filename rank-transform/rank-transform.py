def rank_transform(values):
    """
    Replace each value with its average rank.
    """
    # Write code here
    original = values[:]   
    sorted_values = sorted(values)

    hmap = {}
    n = len(values)
    i = 0

    while i < n:
        j = i

    
        while j < n and sorted_values[j] == sorted_values[i]:
            j += 1

        
        avg_rank = ((i + 1) + j) / 2.0

        hmap[sorted_values[i]] = avg_rank

        i = j

    ans = []

    for value in original:
        ans.append(float(hmap[value]))

    return ans
        
            
        