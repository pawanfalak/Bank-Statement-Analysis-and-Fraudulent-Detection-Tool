INT_SIZE = 32

# function to find the OR_SUM 
def ORsum(arr, n): 
	# create an array of size 32 
	# and store the sum of bits 
	# with value 0 at every index. 
	zerocnt = [0 for i in range(INT_SIZE)] 

	for i in range(INT_SIZE):	 
		for j in range(n):	 
			if not (arr[j] & (1 << i)): 
				zerocnt[i] += 1			
	
	# for each index the OR sum contributed 
	# by that bit of subset will be 2^(bit index) 
	# now the OR of the bits is 0 only if 
	# all the ith bit of the elements in subset 
	# is 0. 
	ans = 0
	for i in range(INT_SIZE): 
		ans += ((2 ** n - 1) - (2 ** zerocnt[i] - 1)) * 2 ** i 

	return ans 

# Driver code 

if __name__ == "__main__": 
	arr= [1, 2, 3] 
	size = len(arr) 
	print(ORsum(arr, size)) 

# This code is contributed by vaibhav29498 
