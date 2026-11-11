def solution(A):
    if len(A) < 2:
        return 0

    min_price = A[0]
    max_profit = 0

    for price in A[1:]:
        # 1. Update maximum achievable profit if sold today
        if price - min_price > max_profit:
            max_profit = price - min_price
        
        # 2. Update historical minimum purchase price
        if price < min_price:
            min_price = price
    
    return max_profit

if __name__ == "__main__":
    print(solution([23171, 21011, 21123, 21366, 21013, 21367])) # Expected output: 356
    print(solution([5, 4, 3, 2, 1])) 
    
