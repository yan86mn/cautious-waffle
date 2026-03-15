#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""命令行计算器程序。

支持加、减、乘、除四种基本运算，提供友好的中文交互界面。
"""

import os
import sys


def add(a, b):
    """执行加法运算。

    Args:
        a (float): 第一个加数。
        b (float): 第二个加数。

    Returns:
        float: 两个数的和。
    """
    return a + b


def subtract(a, b):
    """执行减法运算。

    Args:
        a (float): 被减数。
        b (float): 减数。

    Returns:
        float: 两个数的差。
    """
    return a - b


def multiply(a, b):
    """执行乘法运算。

    Args:
        a (float): 第一个乘数。
        b (float): 第二个乘数。

    Returns:
        float: 两个数的积。
    """
    return a * b


def divide(a, b):
    """执行除法运算。

    Args:
        a (float): 被除数。
        b (float): 除数。

    Returns:
        float: 两个数的商。

    Raises:
        ZeroDivisionError: 当除数为0时抛出异常。
    """
    if b == 0:
        raise ZeroDivisionError("除数不能为0")
    return a / b


def clear_screen():
    """清屏函数，兼容Windows和Unix系统。"""
    os.system('cls' if os.name == 'nt' else 'clear')


def print_separator():
    """打印分隔线。"""
    print("-" * 50)


def print_header(title):
    """打印带标题的头部。

    Args:
        title (str): 标题文本。
    """
    print_separator()
    print(f"  {title}")
    print_separator()


def get_number_input(prompt):
    """获取用户输入的数字。

    验证输入是否为有效数字（支持整数、小数、负数）。

    Args:
        prompt (str): 输入提示文本。

    Returns:
        float: 用户输入的有效数字。
    """
    while True:
        user_input = input(prompt).strip()
        try:
            return float(user_input)
        except ValueError:
            print("❌ 输入无效！请输入一个有效的数字（如：10、3.14、-5）")


def show_welcome():
    """显示欢迎界面。"""
    clear_screen()
    print("\n")
    print("╔" + "═" * 48 + "╗")
    print("║" + " " * 48 + "║")
    print("║" + "       🧮  欢迎使用命令行计算器  🧮".center(44) + "║")
    print("║" + " " * 48 + "║")
    print("╚" + "═" * 48 + "╝")
    print("\n")
    print("  💡 使用提示：")
    print("     • 选择菜单选项进行相应运算")
    print("     • 支持整数、小数和负数")
    print("     • 输入 '5' 查看详细帮助")
    print("     • 输入 '0' 退出程序")
    print("\n")
    input("  按回车键开始...")


def show_help():
    """显示使用帮助。"""
    clear_screen()
    print_header("📖 使用帮助")

    print("\n【操作步骤】")
    print("  1. 在主菜单选择运算类型（1-4）")
    print("  2. 按提示输入第一个数字")
    print("  3. 按提示输入第二个数字")
    print("  4. 查看计算结果")
    print("  5. 按回车键继续下一次计算")

    print("\n【使用示例】")
    print("  示例1 - 加法：")
    print("    请选择操作: 1")
    print("    请输入第一个数字: 10")
    print("    请输入第二个数字: 20")
    print("    结果: 10.0 + 20.0 = 30.0")
    print()
    print("  示例2 - 除法（小数）：")
    print("    请选择操作: 4")
    print("    请输入第一个数字: 22.5")
    print("    请输入第二个数字: 2")
    print("    结果: 22.5 / 2.0 = 11.25")

    print("\n【注意事项】")
    print("  ⚠️  除数不能为0，否则会提示错误")
    print("  ⚠️  输入非数字时会要求重新输入")
    print("  ⚠️  支持负数运算，如：-5 + 3 = -2")
    print("  ⚠️  结果如果是整数，会同时显示整数形式")

    print("\n")
    input("按回车键返回主菜单...")


def show_menu():
    """显示主菜单。

    Returns:
        str: 用户选择的菜单选项。
    """
    clear_screen()
    print_header("🧮 主菜单")
    print("  1. ➕ 加法")
    print("  2. ➖ 减法")
    print("  3. ✖️  乘法")
    print("  4. ➗ 除法")
    print("  5. ❓ 使用帮助")
    print("  0. 🚪 退出程序")
    print_separator()

    while True:
        choice = input("请选择操作 (0-5): ").strip()
        if choice in ['0', '1', '2', '3', '4', '5']:
            return choice
        print("❌ 无效选项！请输入 0-5 之间的数字")


def format_result(result):
    """格式化计算结果。

    如果结果是整数，同时显示整数形式。

    Args:
        result (float): 计算结果。

    Returns:
        str: 格式化后的结果字符串。
    """
    if result == int(result):
        return f"{result} (整数形式: {int(result)})"
    return str(result)


def perform_calculation(operation, symbol, func):
    """执行计算并显示结果。

    Args:
        operation (str): 运算名称（如"加法"）。
        symbol (str): 运算符号（如"+"）。
        func (callable): 执行运算的函数。
    """
    clear_screen()
    print_header(f"➕ {operation}")

    num1 = get_number_input("请输入第一个数字: ")
    num2 = get_number_input("请输入第二个数字: ")

    print_separator()
    try:
        result = func(num1, num2)
        print(f"✅ 计算成功！")
        print(f"   {num1} {symbol} {num2} = {format_result(result)}")
    except ZeroDivisionError as e:
        print(f"❌ 计算错误: {e}")
        print("   提示：除法运算时，除数不能为0，请重新计算")
    print_separator()

    input("\n按回车键继续...")


def main():
    """程序主函数。"""
    show_welcome()

    operations = {
        '1': ('加法', '+', add),
        '2': ('减法', '-', subtract),
        '3': ('乘法', '*', multiply),
        '4': ('除法', '/', divide),
    }

    while True:
        choice = show_menu()

        if choice == '0':
            clear_screen()
            print("\n")
            print("╔" + "═" * 48 + "╗")
            print("║" + "   感谢使用命令行计算器，再见！".center(40) + "║")
            print("╚" + "═" * 48 + "╝")
            print("\n")
            sys.exit(0)

        elif choice == '5':
            show_help()

        else:
            operation, symbol, func = operations[choice]
            perform_calculation(operation, symbol, func)


if __name__ == "__main__":
    main()
