'''Create a function that takes three arguments prob,
prize, pay and returns true if prob * prize > pay;
otherwise return false.'''

def is_worth_it(prob, prize, pay):
  """
  Returns True if prob * prize > pay, otherwise False.

  Args:
    prob: The probability of winning the prize.
    prize: The value of the prize.
    pay: The amount of money paid to enter the contest.

  Returns:
    True if prob * prize > pay, otherwise False.
  """

  expected_value = prob * prize
  return expected_value > pay

print(is_worth_it(12, 2000, 60))
