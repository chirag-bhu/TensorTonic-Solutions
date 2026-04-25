def binning(values, num_bins):
    """
    Assign each value to an equal-width bin.
    """
    # Write code here
    if min(values) == max(values):
        return [0] * len(values)
    w=(max(values)-min(values))/num_bins
    ans=[]
    for i in values:
        result=min(int((i-min(values))/w),num_bins-1)
        ans.append(result)
    return ans