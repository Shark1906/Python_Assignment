class NegativeValueError(Exception):
    def __init__(self, value):
        self.value = value

count = 1
while count == 1:
    try:
        t = input('Enter the temperature in Farenhiet : ')
        v = input('Enter the speed of wind : ')
        if int(v) > 0:
            wind_chill = (35.74 + 0.6215 * float(t) + (0.4275 * float(t) - 35.75) * pow(float(v), 0.16))
            print('WindChill : ',wind_chill)
            break
        else:
            raise NegativeValueError("Negative value for wind speed")

    except NegativeValueError as error:
        print("Exception :", error.value)    