'''
제작일:2020년 11월 13일
제작자:박형규
<간단설명>
정보쌤이 만들어보라고 해서 만들어보는 문자열계산기.
문자열로 '7^(8-2)/3+8', '7/((6+7)*3)*8+6^(8+2)' 이런느낌으로 입력하면 계산해주는 계산기를 만들어보자!
'''

def PrintLine(num):
    num = int(num)
    if num<0:
        num *= -1

    if num==0:
        return 0
    else:
        print("-")
        PrintLine(num-1)

class Preprocesser():
    '''
    <현재까지 생각해낸 전처리들>
    1.공백 제거
    2.등호 검사 후 알맞은 위치에 있다면 제거
    3.괄호 일괄 ()로 변환
    4.괄호 개수 확인
    5.x, X 등을 *로 변환 + **를 ^로 변환
    6.숫자, 연산자 이외의 기타 문자 존재 확인
    7.소수점 맞게 찍었는지 확인
    8.연산자 두개 이상 겹쳐서 썼는지 검사

    Calculator클래스 다 만들고 갑자기 생각난건데 나중에 시간 남으면 삼각함수도 추가해보자!
    삼각함수 -> 파이 -> 자연상수 -> 각도(라디안말고 90분법인가 그거)로 이어지는 사고의 흐름에 삼각함수부터는 안만들기로 함.

    +2020-1115에 발견한 오류
    5(8*2+3)+3는 어떻게 처리해야하지. -> 해결했다!

    6(-7). 포기. 열정이 식었다.
    '''
    #0 => 오류 없음 / 1 => 오류 있음

    def __init__(self):
        self.OPERATORS = ['^', '/', '*', '+', '-']

    def __ChangeOneCharacter(self, index, character): #parentheses:소괄호
        if index == 0:
            self.expression = character+self.expression[1:]
        elif index == len(self.expression)-1:
            self.expression = self.expression[:index]+character
        else:
            self.expression = self.expression[:index]+character+self.expression[index+1:]

    def __ChangeCharacters(self, index_start, index_end, character):
        if index_start == 0:
            self.expression = character+self.expression[index_end+1]
        elif index_end == len(self.expression)-1:
            self.expression = self.expression[:index_start]+character
        else:
            self.expression = self.expression[:index_start]+character+self.expression[index_end+1:]

    def __RemoveSpace(self): #첫번째 : 공백 제거
        while self.expression.find(' ') != -1:
            index = self.expression.find(' ')
            self.__ChangeOneCharacter(index, '')

    def __RemoveEqualSign(self): #두번째 : 등호 검사 후 알맞은 위치에 있다면 제거
        if self.expression.count("=") >= 2:
            return 1
        while self.expression.count('=') == 1:
            index = self.expression.find('=')
            if index == len(self.expression) - 1:
                self.expression = self.expression[:-1]
                return 0
            else:
                return 1
        return 0
    #return

    def __ChangeBrackets(self): #세번째 : 괄호 일괄 ()로 변환
        while self.expression.find('[') != -1:
            self.__ChangeOneCharacter(self.expression.find('['), '(')
        while self.expression.find(']') != -1:
            self.__ChangeOneCharacter(self.expression.find(']'), ')')
        while self.expression.find('{') != -1:
            self.__ChangeOneCharacter(self.expression.find('{'), '(')
        while self.expression.find('}') != -1:
            self.__ChangeOneCharacter(self.expression.find('}'), ')')

    def __CheckNumberOfBrackets(self): #네번째 : 괄호 개수 확인
        number = 0
        index = 0
        while index < len(self.expression):
            if self.expression[index] == '(':
                number += 1
            elif self.expression[index] == ')':
                number -= 1

            if number < 0:
                print("There is a wrong bracket")
                return 1
            index += 1
        if number > 0:
            print("There is a wrong bracket")
            return 1
        else:
            return 0
    #return

    def __ChangeMultiplicationSign(self): #다섯번째 : x, X 등을 *로 변환 + **는 ^로 변환
        while self.expression.find("**") != -1:
            self.__ChangeCharacters(self.expression.find("**"), self.expression.find("**")+1, "^")
        index = 0
        while index < len(self.expression):
            if self.expression[index] == 'x' or self.expression[index] == 'X':
                self.__ChangeOneCharacter(index, '*')
            index += 1

    #1:58 추가아이디어. **를 ^로 변환해줘야하지 않을까.

    def __CheckUnexpectedCharacters(self): #여섯번째 : 숫자, 연산자 이외의 기타 문자 존재 확인
        index = 0
        another_characters = list()
        while index < len(self.expression):
            if self.expression[index] not in ['0','1','2','3','4','5','6','7','8','9','^','/','*','+','-','.','(',')']:
                another_characters.append(self.expression[index])
            index += 1
        if another_characters == []:
            return 0
        else:
            print("There is unexpected characters except numbers, operators, brackets.")
            print("Here is the list of them. ", end='')
            print(another_characters)
            return 1
    #return

    def __CheckDecimalPoint(self): #일곱번째 : 소수점 맞게 찍었는지 확인
        count = 0
        index = 0
        while index < len(self.expression):
            if self.expression[index] == '.':
                count += 1
            elif self.expression[index] in self.OPERATORS and count > 0:
                count -= 1

            if count >= 2:
                print("There is a wrong decimal point")
                return 1
            index += 1
        return 0
    #return

    def __CheckOperators(self): #여덟번째 : 연산자 두개 이상 겹쳐서 썼는지 검사
        index = 1
        cont = self.expression[0]
        while index < len(self.expression)-1:
            if self.expression[index] == '(' or self.expression[index] == ')':
                index += 1
                continue

            if cont in self.OPERATORS and self.expression[index] in self.OPERATORS:
                print("There is wrong operators")
                return 1

            cont = self.expression[index]
            index += 1
        return 0
    #return

    def CheckAndGetPreprocessedExpression(self, original_expression):
        self.expression = original_expression
        self.__RemoveSpace()
        if self.__RemoveEqualSign()==1:
            return 1
        self.__ChangeBrackets()
        if self.__CheckNumberOfBrackets()==1:
            return 1
        self.__ChangeMultiplicationSign()
        if self.__CheckUnexpectedCharacters()==1:
            return 1
        if self.__CheckDecimalPoint()==1:
            return 1
        if self.__CheckOperators()==1:
            return 1
        return self.expression

class Calculator():
    def __init__(self):
        self.OPERATORS = ['^', '/', '*', '+', '-']
        self.BRACKETS_AND_OPERATORS = ['(', ')', '^', '/', '*', '+', '-']

    def __ChangeStrToFloat(self, string):
        #This function should return int or float
        index_dot = string.find('.')
        if index_dot == -1:
            return int(string)
        else:
            a = int(string[:index_dot])
            b = int(string[index_dot+1:])
            size = len(string[index_dot+1:])
            return a+b*(10**-size)

    def __SimpleCalc(self, expression, operator):
        index_operator = expression.find(operator)
        count_start = 2
        count_end = 2
        while index_operator-count_start != -1 and  expression[index_operator - count_start] not in self.OPERATORS:
            count_start += 1
        while index_operator+count_end != len(expression) and expression[index_operator + count_end] not in self.OPERATORS:
            count_end += 1
        index_start = index_operator - count_start + 1
        index_end = index_operator + count_end - 1
        a = self.__ChangeStrToFloat(expression[index_start:index_operator])
        b = self.__ChangeStrToFloat(expression[index_operator + 1:index_end + 1])

        try:
            if operator == '^':
                return expression[:index_start] + str(a ** b) + expression[index_end + 1:]
            elif operator == '/':
                return expression[:index_start] + str(a / b) + expression[index_end + 1:]
            elif operator == '*':
                return expression[:index_start] + str(a * b) + expression[index_end + 1:]
            elif operator == '+':
                return expression[:index_start] + str(a + b) + expression[index_end + 1:]
            elif operator == '-':
                return expression[:index_start] + str(a - b) + expression[index_end + 1:]
            else:
                raise Exception("Unpredicted operator in def __SimpleCalc in class Calculator")
        except Exception as e:
            return e

    def __CalcWithoutBracket(self, expression):
        while '^' in expression:
            expression = self.__SimpleCalc(expression, '^')
        while '/' in expression:
            expression = self.__SimpleCalc(expression, '/')
        while '*' in expression:
            expression = self.__SimpleCalc(expression, '*')
        while '+' in expression:
            expression = self.__SimpleCalc(expression, '+')
        while '-' in expression:
            expression = self.__SimpleCalc(expression, '-')
        return expression

    def __SubstituteString(self, original_string, index_start, index_end, to_insert):
        #5(8*2)+3이런거 맞게 계산하기 위해 조건문 2개 추가함.
        if index_start != 0 and original_string[index_start-1] not in self.BRACKETS_AND_OPERATORS:
            original_string = original_string[:index_start]+"*"+original_string[index_start:]
            index_start += 1
            index_end += 1
        if index_end != len(original_string)-1 and original_string[index_end+1] not in self.BRACKETS_AND_OPERATORS:
            original_string = original_string[:index_end]+"*"+original_string[index_end:]
        return original_string[:index_start]+to_insert+original_string[index_end+1:]

    def Calculate(self, expression):
        index = 0
        opening_bracket = list()
        while expression.find('(') != -1 and expression.find(')') != 1:
            if expression[index]=='(':
                opening_bracket.append(index)
            elif expression[index]==')':
                index_starting_bracket = opening_bracket.pop()
                cont = self.__CalcWithoutBracket(expression[index_starting_bracket+1:index])
                expression = self.__SubstituteString(expression, index_starting_bracket, index, cont)
                index = 0
                continue
            index += 1
        return self.__CalcWithoutBracket(expression)

def main():
    preprocessor = Preprocesser()
    calculator = Calculator()
    print("Date that this program is made : 2020-1115")
    print("This is a calculator that Park Hyeong-gyu made after being requested to made calculator from the information teacher.")
    a = input("Input expression that you wanna calculate : ")
    a = preprocessor.CheckAndGetPreprocessedExpression(a)
    if a==1:
        print("There is an error in expression.")
        return 1
    else:
        result = calculator.Calculate(a)
        if float(result)%1 == 0:
            result = int(float(result))
        print("This is result", result)


if __name__=="__main__":
    main()