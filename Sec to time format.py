seconds = int(input("Enter number of seconds : "))

rem_sec = str(seconds%60).rjust(2,'0')

rem_min = str(seconds//60).rjust(2,'0')

hours = str(seconds//3600).rjust(2,'0')

print(seconds)

print(f'{hours}:{rem_min}:{rem_sec}')
