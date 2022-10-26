test_cases = int(input())

for tc in range(test_cases):
    bags_kids = input().split(' ')
    bags = int(bags_kids[0])
    kids = int(bags_kids[1])
    candies = input().split(' ')
    candies = list(map(int, candies))
    all_candies = sum(candies)
    print('Case #' + str(tc + 1) + ': ' + str(all_candies % kids))
    # print(bags, kids)
    # print(candies)
