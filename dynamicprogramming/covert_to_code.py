"""
T(0)=T(1) = 2

T(n) = E 2*T(i)*T(i-1) for n > 1 where i = 1 to n-1
"""

def recurive(num, total=0):
    """
    time compelxity -> O(n), space O(1) excluding stack
    including stack ->O(n)
    :param num:
    :param total:
    :return:
    """
    if num == 0 or num== 1:
        return 2
    for i in range(1, num):
        total += 2* recurive(i, total) * recurive(i-1, total)
    return total


def memoize(num, total, mem):
    """
    time complexity -> O(n)
    space complexity -> O(n)
    :param num:
    :param total:
    :param mem:
    :return:
    """
    if mem.get(num):
        return mem.get(num)
    if num == 0 or num == 1:
        mem[num] = 2
        return mem[num]
    for i in range(1, num):
        total = 2* memoize(i, total, mem) * memoize(i-1, total, mem)
        mem[i] = total
    return total


def bottom_up(num):
    """
    time O(n)
    space O(n)
    :param num:
    :return:
    """
    output = [0]*(num+1)
    output[0] = 2
    output[1] = 2
    output[2] = 2* output[1] * output[0]
    for i in range(3, num):
        output[i] = output[i-1]+ 2 * output[i-1] * output[i-2]
    print(output)
    return output[-1]


if __name__ == "__main__":

    print(recurive(5, 0))
    print(memoize(5, 0, {0:2, 1:2}))
    print(bottom_up(5))