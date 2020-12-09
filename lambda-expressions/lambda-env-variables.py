import os

function = lambda argument: "http://localhost" if argument not in os.environ else argument

print(function('address'))