# buggy_code.py

def calculate_average(numbers):
    """计算列表中所有数值的平均值"""
    total = 0
    count = 0
    for num in numbers:
        total += num
        count += 1
    return total / count  # 可能会引发除零错误


def find_max(numbers):
    """查找列表中的最大值"""
    max_num = numbers[0]  # 当列表为空时会出错
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num


def reverse_string(s):
    """反转字符串"""
    reversed_str = ""
    for i in range(len(s)):
        reversed_str += s[len(s) -1 - i]  # 索引越界错误
    return reversed_str


def is_palindrome(s):
    """检查字符串是否为回文"""
    reversed_s = reverse_string(s)
    return s == reversed_s


def process_data(data):
    """处理数据列表，返回处理后的结果列表"""
    result = []
    for item in data:
        if item % 2 == 0:  # 假设data中的元素都是整数，但实际可能不是
            result.append(item * 2)
    return result


def main():
    # 测试用例1: 计算平均值
    numbers = [1, 2, 3, 4, 5]
    avg = calculate_average(numbers)
    print(f"平均值: {avg}")

    # 测试用例2: 查找最大值
    max_num = find_max(numbers)
    print(f"最大值: {max_num}")

    # 测试用例3: 反转字符串
    s = "hello"
    reversed_s = reverse_string(s)
    print(f"反转后的字符串: {reversed_s}")

    # 测试用例4: 检查回文
    palindrome = "radar"
    print(f"'{palindrome}' 是回文吗? {is_palindrome(palindrome)}")

    # 测试用例5: 处理数据
    data = [1, 2, "three", 4, 5]  # 包含非整数值
    processed_data = process_data(data)
    print(f"处理后的数据: {processed_data}")

    # 测试用例6: 空列表
    empty_list = []
    print(f"空列表的平均值: {calculate_average(empty_list)}")


if __name__ == "__main__":
    main()