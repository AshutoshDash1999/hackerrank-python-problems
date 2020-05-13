# problem link = https://www.hackerrank.com/challenges/exceptions/problem
# the try function can be understand as a virtual space where you can try your code
#  and if anything gets wrong the exception function will run


test_no = int(input())
for i in range(test_no): # loop to run the number of test cases as given in the problem
    try:
        input_value = input()
        input_list = list(map(int, input_value.split()))  # the input string values are converted to int and then list

        result = input_list[0] // input_list[1]
        print(result)
    except Exception as e:
        print("Error Code:", e)