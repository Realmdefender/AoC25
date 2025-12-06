import re

"""
After helping the Elves in the kitchen, you were taking a break and helping them re-enact a movie scene when you over-enthusiastically jumped into the garbage chute!
A brief fall later, you find yourself in a garbage smasher. Unfortunately, the door's been magnetically sealed.
As you try to find a way out, you are approached by a family of cephalopods! They're pretty sure they can get the door open, but it will take some time. While you wait, they're curious if you can help the youngest cephalopod with her math homework.
Cephalopod math doesn't look that different from normal math. The math worksheet (your puzzle input) consists of a list of problems; each problem has a group of numbers that need to be either added (+) or multiplied (*) together.

However, the problems are arranged a little strangely; they seem to be presented next to each other in a very long horizontal list. For example:

123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  
Each problem's numbers are arranged vertically; at the bottom of the problem is the symbol for the operation that needs to be performed.
Problems are separated by a full column of only spaces. The left/right alignment of numbers within each problem can be ignored.
So, this worksheet contains four problems:

123 * 45 * 6 = 33210
328 + 64 + 98 = 490
51 * 387 * 215 = 4243455
64 + 23 + 314 = 401

To check their work, cephalopod students are given the grand total of adding together all of the answers to the individual problems. In this worksheet, the grand total is 33210 + 490 + 4243455 + 401 = 4277556.
Of course, the actual worksheet is much wider. You'll need to make sure to unroll it completely so that you can read the problems clearly.
Solve the problems on the math worksheet. What is the grand total found by adding together all of the answers to the individual problems?
"""

def read_input(file_path):
    with open(file_path, 'r') as file:
        return [re.split(r" +", line.strip()) for line in file.readlines()]    
    
def solve_problems(problems):
    results_sum = 0

    for i in range(len(problems[0])):
        result = 0 if (problems[-1][i] == '+') else 1
        for j in range(len(problems) - 1):
            result = result + int(problems[j][i]) if (problems[-1][i] == '+') else result * int(problems[j][i])
        results_sum += result

    return results_sum



file_path = 'Day 6/input.txt'
problems = read_input(file_path)
grand_total = solve_problems(problems)
print(f'Grand total of all problems: {grand_total}')

"""
The big cephalopods come back to check on how things are going. When they see that your grand total doesn't match the one expected by the worksheet, they realize they forgot to explain how to read cephalopod math.
Cephalopod math is written right-to-left in columns. Each number is given in its own column, with the most significant digit at the top and the least significant digit at the bottom. (Problems are still separated with a column consisting only of spaces, and the symbol at the bottom of the problem is still the operator to use.)

Here's the example worksheet again:

123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  
Reading the problems right-to-left one column at a time, the problems are now quite different:

The rightmost problem is 4 + 431 + 623 = 1058
The second problem from the right is 175 * 581 * 32 = 3253600
The third problem from the right is 8 + 248 + 369 = 625
Finally, the leftmost problem is 356 * 24 * 1 = 8544
Now, the grand total is 1058 + 3253600 + 625 + 8544 = 3263827.

Solve the problems on the math worksheet again. What is the grand total found by adding together all of the answers to the individual problems?
"""

def read_input_2(file_path):
    problems = []

    with open(file_path, 'r') as file:
        lines = file.readlines()
        
        problem = []
        for i in range(len(lines[0])):
            number = ''
            for j in range(len(lines) - 1):
                number += lines[j][i]
            if (number.strip() != ''):
                problem.append(int(number.strip()))
            else:
                problems.append(problem)
                problem = []

        signs = re.split(r" +", lines[-1].strip())

    return problems, signs

def solve_problems_2(numbers, signs):
    results_sum = 0

    for i in range(len(numbers)):
        result = 0 if (signs[i] == '+') else 1
        for j in range(len(numbers[i])):
            result = result + numbers[i][j] if (signs[i] == '+') else result * numbers[i][j]
        results_sum += result

    return results_sum

numbers, signs = read_input_2('Day 6/input.txt')
grand_total_2 = solve_problems_2(numbers, signs)
print(f'Grand total of all problems (right-to-left): {grand_total_2}')