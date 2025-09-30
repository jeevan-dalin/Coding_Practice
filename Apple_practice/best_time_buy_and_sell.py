# You are given an array prices where prices[i] is the price of a given stock on the ith day.

# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.


def best_time(arr):
    buy_price=arr[0]
    buy_day=0
    plug=0
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i]<arr[j]:
                buy_price=arr[i]
                buy_day=i+1
                plug=1
                break
        if plug==1:
            break
    sell_price=arr[buy_day-1]
    for i in range(buy_day,len(arr)):
        if arr[i]>sell_price:
            sell_price=arr[i]
    print(sell_price-buy_price)
   

arr=[7,6,4,3,1]

best_time(arr)   