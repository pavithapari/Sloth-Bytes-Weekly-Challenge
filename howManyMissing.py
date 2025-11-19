def howManyMissing(lst):
  count=0
  for i in range(1,len(lst)):
    count+=lst[i]-lst[i-1]-1
  return count
  
    
