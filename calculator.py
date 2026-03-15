"""
简易计算器程序
支持加、减、乘、除四种基本运算，提供友好的中文交互界面。
"""

import os
import platform


def clear_screen():
    """清空控制台屏幕，兼容Windows和Unix系统。"""
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")


def add(a, b):
    """执行加法运算。

    Args:
        a: 第一个操作数。
        b: 第二个操作数。

    Returns:
        两个操作数的和。
    """
    return a + b


def subtract(a, b):
    """执行减法运算。

    Args:
        a: 被减数。
        b: 减数。

    Returns:
        两个操作数的差。
    """
    return a - b


def multiply(a, b):
    """执行乘法运算。

    Args:
        a: 第一个操作数。
        b: 第二个操作数。

    Returns:
        两个操作数的积。
    """
    return a * b


def divide(a, b):
    """执行除法运算。

    Args:
        a: 被除数。
        b: 除数。

    Returns:
        两个操作数的商。

    Raises:
        ZeroDivisionError: 当除数为0时抛出。
    """
    if b == 0:
        raise ZeroDivisionError("除数不能为0")
    return a / b


def get_valid_number(prompt):
    """获取用户输入的有效数字。

    Args:
        prompt: 提示用户输入的文本。

    Returns:
        用户输入的有效数字（整数或浮点数）。
    """
    while True:
        user_input = input(prompt).strip()
        try:
            return float(user_input)
        except ValueError:
            print("输入无效，请输入一个有效的数字（支持整数、小数、负数）。")


def format_result(result):
    """格式化计算结果，处理浮点精度问题。

    Args:
        result: 计算结果。

    Returns:
        格式化后的结果字符串。
    """
    rounded = round(result, 10)
    if rounded == int(rounded):
        return f"{int(rounded)}（整数形式）"
    return f"{rounded:g}"


def print_welcome():
    """打印欢迎引导界面。"""
    clear_screen()
    print("=" * 50)
    print(" " * 15 + "欢迎使用简易计算器")
    print("=" * 50)
    print()
    print("本计算器支持以下功能：")
    print("  · 加法运算")
    print("  · 减法运算")
    print("  · 乘法运算")
    print("  · 除法运算（自动处理除数为0的情况）")
    print()
    print("使用提示：")
    print("  · 支持整数、小数、负数输入")
    print("  · 可连续进行多次计算")
    print("  · 选择菜单选项 5 可查看详细帮助")
    print("=" * 50)


def print_menu():
    """打印操作菜单。"""
    print()
    print("-" * 30)
    print("请选择操作：")
    print("-" * 30)
    print("  1. 加法运算")
    print("  2. 减法运算")
    print("  3. 乘法运算")
    print("  4. 除法运算")
    print("  5. 使用帮助")
    print("  0. 退出程序")
    print("-" * 30)


def print_help():
    """打印使用帮助信息。"""
    clear_screen()
    print("=" * 50)
    print(" " * 18 + "使用帮助")
    print("=" * 50)
    print()
    print("【操作步骤】")
    print("  1. 从菜单中选择要进行的运算类型（输入1-4）")
    print("  2. 根据提示输入第一个数字")
    print("  3. 根据提示输入第二个数字")
    print("  4. 系统自动计算并显示结果")
    print("  5. 按回车键继续下一次计算")
    print()
    print("【使用示例】")
    print("  示例1 - 加法：")
    print("    输入第一个数字: 15")
    print("    输入第二个数字: 27")
    print("    结果: 15 + 27 = 42（整数形式）")
    print()
    print("  示例2 - 除法：")
    print("    输入第一个数字: 10")
    print("    输入第二个数字: 3")
    print("    结果: 10 ÷ 3 = 3.3333333333333335")
    print()
    print("  示例3 - 负数运算：")
    print("    输入第一个数字: -5")
    print("    输入第二个数字: 3")
    print("    结果: -5 + 3 = -2（整数形式）")
    print()
    print("【注意事项】")
    print("  · 除法运算时，除数不能为0，否则会提示错误")
    print("  · 输入数字时支持小数，如：3.14、-2.5")
    print("  · 计算结果为整数时会同时显示整数形式")
    print("  · 输入0可退出程序")
    print("=" * 50)


def perform_calculation(operation):
    """执行计算操作。

    Args:
        operation: 运算类型（1-4分别对应加减乘除）。
    """
    operation_names = {
        1: ("加法", "+", add),
        2: ("减法", "-", subtract),
        3: ("乘法", "×", multiply),
        4: ("除法", "÷", divide),
    }

    name, symbol, func = operation_names[operation]

    print()
    print(f"【{name}运算】")
    num1 = get_valid_number("请输入第一个数字: ")
    num2 = get_valid_number("请输入第二个数字: ")

    try:
        result = func(num1, num2)
        print()
        print("-" * 30)
        print(f"计算结果: {num1} {symbol} {num2} = {format_result(result)}")
        print("-" * 30)
    except ZeroDivisionError as e:
        print()
        print("-" * 30)
        print(f"错误提示: {e}")
        print("请重新选择运算并输入非零的除数。")
        print("-" * 30)


def get_valid_choice():
    """获取有效的菜单选择。

    Returns:
        用户选择的有效菜单选项（0-5）。
    """
    while True:
        choice = input("请输入选项 (0-5): ").strip()
        if choice in ["0", "1", "2", "3", "4", "5"]:
            return int(choice)
        print("输入无效，请输入 0-5 之间的数字。")


def main():
    """程序主函数，处理用户交互和计算流程。"""
    print_welcome()

    while True:
        print_menu()
        choice = get_valid_choice()

        if choice == 0:
            print()
            print("=" * 50)
            print("感谢使用简易计算器，再见！")
            print("=" * 50)
            break
        elif choice == 5:
            print_help()
        else:
            perform_calculation(choice)

        print()
        input("按回车键继续...")
        clear_screen()
        print("=" * 50)
        print(" " * 15 + "简易计算器")
        print("=" * 50)


if __name__ == "__main__":
    main()
