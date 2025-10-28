class Stack:
    def __init__(self, max_size=10):
        self.stack = []
        self.max_size = max_size
        self.counter = 0  # 고유 번호 카운터

    def push(self, item):
        if len(self.stack) >= self.max_size:
            print("스택이 가득 찼습니다! (최대 10개)")
        else:
            self.counter += 1
            unique_item = f"{item}-{self.counter}"  # 고유 번호 자동 추가
            self.stack.append(unique_item)
            print(f"추가됨: {unique_item}")

    def pop(self):
        if self.empty():
            print("스택이 비어 있어서 꺼낼 수 없습니다!")
        else:
            item = self.stack.pop()
            print(f"꺼낸 항목: {item}")

    def peek(self):
        if self.empty():
            print("스택이 비어 있습니다!")
        else:
            print(f"마지막 항목: {self.stack[-1]}")

    def empty(self):
        return len(self.stack) == 0

    def show(self):
        print("현재 스택 상태:", self.stack if self.stack else "비어 있음")



if __name__ == "__main__":
    s = Stack(max_size=10)

    while True:
        print("\n====== 스택(Stack) 메뉴 ======")
        print("1. push (추가)")
        print("2. pop (삭제)")
        print("3. peek (확인)")
        print("4. show (전체 보기)")
        print("5. exit (종료)")
        print("=============================")

        try:
            choice = int(input("번호를 선택하세요 (1~5): "))
        except ValueError:
            print("숫자를 입력하세요!")
            continue

        if choice == 1:
            data = input("추가할 데이터를 입력하세요: ")
            s.push(data)

        elif choice == 2:
            s.pop()

        elif choice == 3:
            s.peek()

        elif choice == 4:
            s.show()

        elif choice == 5:
            print(" 프로그램을 종료합니다.")
            break

        else:
            print("잘못된 번호입니다. 1~5 중에서 선택하세요.")

