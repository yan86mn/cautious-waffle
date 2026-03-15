# -*- coding: utf-8 -*-
"""Python命令行计算器程序

支持加、减、乘、除四种基本运算，包含完整的交互界面和输入验证功能。
"""


def add(a, b):
    """计算两个数的和

    Args:
        a (float): 第一个操作数
        b (float): 第二个操作数

    Returns:
        float: 两个数的和
    """
    return a + b


def subtract(a, b):
    """计算两个数的差

    Args:
        a (float): 第一个操作数
        b (float): 第二个操作数

    Returns:
        float: 两个数的差
    """
    return a - b


def multiply(a, b):
    """计算两个数的积

    Args:
        a (float): 第一个操作数
        b (float): 第二个操作数

    Returns:
        float: 两个数的积
    """
    return a * b


def divide(a, b):
    """计算两个数的商

    Args:
        a (float): 被除数
        b (float): 除数

    Returns:
        float: 两个数的商

    Raises:
        ZeroDivisionError: 当除数为0时抛出
    """
    if b == 0:
        raise ZeroDivisionError("除数不能为0")
    return a / b


def validate_number(input_str):
    """验证并转换用户输入为有效数字

    Args:
        input_str (str): 用户输入的字符串

    Returns:
        tuple: (is_valid, number)，is_valid为布尔值表示是否有效，number为转换后的数字
    """
    try:
        return True, float(input_str)
    except ValueError:
        return False, None


def display_menu():
    """显示计算器主菜单"""
    print("=" * 50)
    print(" " * 18 + "命令行计算器")
    print("=" * 50)
    print("1. 加法运算")
    print("2. 减法运算")
    print("3. 乘法运算")
    print("4. 除法运算")
    print("5. 使用帮助")
    print("0. 退出程序")
    print("-" * 50)


def display_help():
    """显示使用帮助信息"""
    print("\n" + "=" * 50)
    print(" " * 20 + "使用帮助")
    print("=" * 50)
    print("\n【操作步骤说明】")
    print("1. 从菜单中选择需要的运算类型（输入数字）")
    print("2. 依次输入两个参与运算的数字")
    print("3. 查看计算结果")
    print("4. 按回车键继续进行下一次计算")
    print("\n【完整使用示例】")
    print("  示例：计算 3.5 + (-2)")
    print("  1. 输入菜单选项：1")
    print("  2. 输入第一个数：3.5")
    print("  3. 输入第二个数：-2")
    print("  4. 计算结果：1.5 (整数形式: 1)")
    print("\n【注意事项提醒】")
    print("- 支持整数、小数、负数输入")
    print("- 除法运算时除数不能为0")
    print("- 输入菜单选项时请输入0-5之间的数字")
    print("- 输入'q'或'quit'可在任何时候退出程序")
    print("-" * 50 + "\n")


def get_number(prompt):
    """获取并验证用户输入的数字

    Args:
        prompt (str): 提示信息

    Returns:
        float: 有效的数字，输入'q'或'quit'时返回None表示退出
    """
    while True:
        input_str = input(prompt).strip()
        if input_str.lower() in ('q', 'quit'):
            return None
        is_valid, num = validate_number(input_str)
        if is_valid:
            return num
        print("错误：请输入有效的数字（整数、小数、负数均可）")


def format_result(result):
    """格式化计算结果，整数额外显示整数形式

    Args:
        result (float): 计算结果

    Returns:
        str: 格式化后的结果字符串
    """
    if result == int(result):
        return f"{result} (整数形式: {int(result)})"
    return f"{result}"


def calculate(operation, num1, num2):
    """执行计算操作

    Args:
        operation (str): 运算类型
        num1 (float): 第一个操作数
        num2 (float): 第二个操作数

    Returns:
        tuple: (success, result)，success为布尔值，result为结果或错误信息
    """
    try:
        if operation == '1':
            return True, add(num1, num2)
        elif operation == '2':
            return True, subtract(num1, num2)
        elif operation == '3':
            return True, multiply(num1, num2)
        elif operation == '4':
            return True, divide(num1, num2)
        else:
            return False, "未知的运算类型"
    except ZeroDivisionError as e:
        return False, str(e)
    except Exception as e:
        return False, f"计算错误：{str(e)}"


def main():
    """程序主函数"""
    print("\n" + "#" * 50)
    print("#" + " " * 48 + "#")
    print("#" + " " * 12 + "欢迎使用Python命令行计算器" + " " * 12 + "#")
    print("#" + " " * 48 + "#")
    print("#" + " " * 8 + "支持：加、减、乘、除四种基本运算" + " " * 8 + "#")
    print("#" + " " * 11 + "输入 'q' 或 'quit' 可随时退出" + " " * 11 + "#")
    print("#" + " " * 48 + "#")
    print("#" * 50 + "\n")

    while True:
        display_menu()
        choice = input("请选择操作（输入数字）：").strip()

        if choice.lower() in ('q', 'quit', '0'):
            print("\n感谢使用计算器，再见！\n")
            break

        if choice == '5':
            display_help()
            input("按回车键返回主菜单...")
            continue

        if choice not in ('1', '2', '3', '4'):
            print("错误：请输入有效的菜单选项（0-5）\n")
            continue

        operation_names = {'1': '加法', '2': '减法', '3': '乘法', '4': '除法'}
        print(f"\n您选择了：{operation_names[choice]}运算")

        num1 = get_number("请输入第一个数：")
        if num1 is None:
            print("\n感谢使用计算器，再见！\n")
            break

        num2 = get_number("请输入第二个数：")
        if num2 is None:
            print("\n感谢使用计算器，再见！\n")
            break

        success, result = calculate(choice, num1, num2)
        if success:
            print(f"\n计算结果：{format_result(result)}")
        else:
            print(f"\n错误：{result}")

        print("\n" + "-" * 50)
        input("按回车键继续...")
        print()


if __name__ == "__main__":
    main()
