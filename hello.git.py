# 这是一个最简单的 Python 示例代码
import math

def main():
    print("--- 欢迎使用 GitHub 托管代码测试 ---")
    name = input("请输入你的名字: ")
    print(f"你好, {name}! 这是一个从本地上传到 GitHub 的程序。")
    
    # 算个小数学题
    radius = 5
    area = math.pi * radius ** 2
    print(f"半径为 {radius} 的圆面积大约是: {area:.2f}")

if __name__ == "__main__":
    main()