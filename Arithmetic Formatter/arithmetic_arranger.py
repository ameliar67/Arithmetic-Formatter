import re


def arithmetic_arranger(problems, c=False):
  arranged_problems = ''
  potential = []
  answer = ''
  count = 0

  for k in problems:

    split_solution = k.split()

    x = re.search('\*|\/|x', split_solution[1])
    b = re.search('[a-z]', k)

    if x is not None:
      arranged_problems = "Error: Operator must be '+' or '-'."
      break
    elif b is not None:
      arranged_problems = "Error: Numbers must only contain digits."
      break
    elif len(split_solution[0]) > 4:
      arranged_problems = "Error: Numbers cannot be more than four digits."
      break
    elif len(split_solution[2]) > 4:
      arranged_problems = "Error: Numbers cannot be more than four digits."
      break

    elif len(problems) > 5:
      arranged_problems = 'Error: Too many problems.'
      break

    if split_solution[1] == "+":
      answer = int(split_solution[0]) + int(split_solution[2])
    else:
      answer = int(split_solution[0]) - int(split_solution[2])
    count = count + 1


    if len(split_solution[0]) > len(split_solution[2]):
      longest_length = len(split_solution[0])
      amount_of_spaces = longest_length + 1 - len(split_solution[2])
      
      line_one = " " + " " + split_solution[0]
      line_two = split_solution[1] + " " * amount_of_spaces + split_solution[2]
      amount_of_dashes = len(split_solution[0]) + 2
      line_three = '-' * amount_of_dashes
      answer =  " " * (amount_of_dashes - len(str(answer))) + str(answer)

    else:
      longest_length = len(split_solution[2])
      amount_of_spaces = longest_length + 2 - len(split_solution[0])

      line_one = " " * amount_of_spaces + split_solution[0]
      line_two = split_solution[1] + " " + split_solution[2]
      amount_of_dashes = len(split_solution[2]) + 2
      line_three = '-' * amount_of_dashes
      answer =  " " * (amount_of_dashes - len(str(answer))) + str(answer)

    
    if count != len(problems):
      line_one = line_one + " " * 4
      line_two = line_two + " " * 4
      line_three = line_three + " " * 4
      answer = answer + " " * 4



    string_ = '\n'.join([line_one, line_two, line_three, answer])

    potential.append(string_)


    first_line = ''
    second_line = ''
    third_line = ''
    fourth_line = ''

    for k in potential:
      lines = [k.splitlines()]

      first_line = first_line + lines[0][0]
      second_line = second_line + lines[0][1]
      third_line = third_line + lines[0][2]
      fourth_line = fourth_line + lines[0][3]


    if c:
      final = [first_line, second_line, third_line, fourth_line]
    else:
      final = [first_line, second_line, third_line]
      
    arranged_problems = '\n'.join(final)

  return arranged_problems
