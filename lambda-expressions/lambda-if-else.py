function = lambda argument : "Valor 1" if not argument else argument
print(function("Valid argument"))
print(function(None))