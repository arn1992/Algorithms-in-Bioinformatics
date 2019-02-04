
def circular_permutation(alpha, beta):
  # Make sure they have the same size
  n=alpha
  m=beta
  if len(n) != len(m):
    return False

  # Rotate through the letters in n
  for i in range(len(n)):
    # Compare the end of n with the beginning of m
    # and the beginning of n with the end of m
    if m.startswith(n[i:]) and m.endswith(n[:i]):
      return True

  return False

print("Name: Md. Aminur Rab Ratul; ID: 300086571")
print('Checking Circular Permutation: ')
alpha=(input("Enter string for alpha: "))
beta=(input("Enter string for beta: "))

decision=circular_permutation(alpha, beta)

if decision==True:
    print(True, ' :alpha and beta are circular permutation of each other')
else:
    print(False, " :alpha and beta are not circular permutation of each other")
