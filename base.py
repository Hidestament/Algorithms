def base_to_k(n,k):
    """10進数のn -> k進数のstr

    Args:
        n (int): 10進数における整数
        k (int): k 進数

    Returns:
        str: nをk進数で表した文字列
    """
    if n // k != 0:
        return base_to_k(n//k, k) + str(n%k)
    else:
        return str(n%k)
