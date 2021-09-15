secondsCount = int(input("Please, input an integer number of seconds to be formatted: "))
hoursCount = secondsCount//3600
remainingMinutes = (secondsCount - hoursCount*3600)//60
remainingSeconds = (secondsCount - hoursCount*3600 - remainingMinutes*60)
print ("{:02d}".format(hoursCount),":","{:02d}".format(remainingMinutes),":","{:02d}".format(remainingSeconds))
