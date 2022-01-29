def maximumDifference(inputArr):
	# Write your code here
	inputArr_size = len(inputArr)
	max_difference = 0
	for i in range(inputArr_size - 1):
		for j in range(i+1, inputArr_size ):
			if inputArr[j] - inputArr[i] > max_difference:
				max_difference = inputArr[j] - inputArr[i]

	return max_difference

def main():
	# input for inputArr
	inputArr = []
	inputArr_size  = int(input())
	inputArr = list(map(int,input().split()))
	
	result = maximumDifference(inputArr)
	print (result)

if __name__ == "__main__":
	main()