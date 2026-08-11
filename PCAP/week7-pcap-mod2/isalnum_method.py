# standard alpha numeric examples
print('lambda'.isalnum())
print('lambda30'.isalnum())
print('2018'.isalnum())

# Fail cases (symbols, underscores, empty string, spaces)
print('@'.isalnum())
print('lambda_30'.isalnum())
print(''.isalnum())
print(' '.isalnum())

# Non-Latin letters and spaces
print('Six lambdas'.isalnum())
print('ΑβΓδ'.isalnum())
print('20E1'.isalnum())