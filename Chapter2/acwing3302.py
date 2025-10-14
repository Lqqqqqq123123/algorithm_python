# 之后在做
s = input()

# 符号栈与数字栈
op, nums = [], []

# 定义运算符优先级
priority = dict()
priority['+'] = 1; priority['-'] = 1; priority['*'] = 2; priority['/'] = 2

def eval(op, nums):
    cur_op, num2, num1 = op.pop(), nums.pop(), nums.pop()
    if cur_op == '+':
        nums.append(num1 + num2)
    elif cur_op == '-':
        nums.append(num1 - num2)
    elif cur_op == '*':
        nums.append(num1 * num2)
    elif cur_op == '/':
        # 向0取整
        nums.append(int(num1 / num2))


for i in range(len(s)):
    # 如果是数字，直接入栈
    if s[i].isdigit():
        # 双指针寻找数字
        j = i
        while j < len(s) and s[j].isdigit():
            j += 1
        # 扣出数字
        num = int(s[i:j])
        nums.append(num)
        i = j - 1
    # 如果是左括号，直接入栈
    elif s[i] == "(":
        op.append(s[i])
    # 如果是右括号，计算栈顶到左括号之间的表达式
    elif s[i] == ")":
        while op[-1] != '(':
            eval(op, nums)
        # 弹出左括号
        op.pop()
    # 如果是正常运算符，就先看看栈顶和当前运算符的优先级，如果栈顶优先级大于等于当前运算符，就先计算栈顶的运算符
    else:
        while op and op[-1] != '(' and priority[op[-1]] >= priority[s[i]]:
            eval(op, nums)
        op.append(s[i])


# 计算栈中剩余的表达式
while op:
    eval(op, nums)

print(nums[0])