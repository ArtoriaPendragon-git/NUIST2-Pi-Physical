import RPi.GPIO as GPIO
import time  # 控制LED亮灯时长

# GPIO引脚初始化
GREEN_LED = 17  # 正确-绿灯
RED_LED = 18    # 错误-红灯
GPIO.setmode(GPIO.BCM)  # 使用BCM引脚编号（树莓派标准）
GPIO.setwarnings(False) # 关闭GPIO警告
# 设置引脚为输出模式，初始低电平（LED熄灭）
GPIO.setup(GREEN_LED, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(RED_LED, GPIO.OUT, initial=GPIO.LOW)

def led_correct():
    """答对：亮绿灯1秒，之后熄灭"""
    GPIO.output(GREEN_LED, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(GREEN_LED, GPIO.LOW)

def led_incorrect():
    """答错：亮红灯1秒，之后熄灭"""
    GPIO.output(RED_LED, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(RED_LED, GPIO.LOW)

def python_quiz():
    print("Welcome to the Python Syntax Quiz!")
    print("Answer with the option letter (a/b/c/d/e), e.g., 'a'\n")
    # 问题列表：[问题内容, 正确答案]
    quiz_data = [
        [
            "1) Which of the following is NOT a python data type?\na) int\nb) float\nc) rational\nd) string\ne) bool",
            "c"
        ],
        [
            "2) Which of the following is NOT a built-in operation in Python?\na) +\nb) %\nc) abs()\nd) sqrt()",
            "d"
        ],
        [
            "3) In a mixed-type expression involving ints and floats, Python will convert:\na) floats to ints\nb) ints to strings\nc) floats and ints to strings\nd) ints to floats",
            "d"
        ],
        [
            "4) The best structure for implementing a multi-way decision in Python is:\na) if\nb) if-else\nc) if-elif-else\nd) try",
            "c"
        ],
        [
            "5) What statement can be executed in the body of a loop to cause it to terminate?\na) if\nb) exit\nc) continue\nd) break",
            "d"
        ]
    ]
    score = 0
    # 遍历答题
    for question, answer in quiz_data:
        user_ans = input(question + "\nYour answer: ").strip().lower()
        if user_ans == answer:
            print("Correct!\n")
            score += 1
            led_correct()  # 亮绿灯
        else:
            print(f"Incorrect! The correct answer is {answer}\n")
            led_incorrect()  # 亮红灯
    # 输出最终分数
    total = len(quiz_data)
    print(f"Quiz completed! You got {score}/{total} questions correct.")
    # 清理GPIO引脚（必须，否则下次运行报错）
    GPIO.cleanup()

# 运行问答函数
if __name__ == "__main__":
    python_quiz()
