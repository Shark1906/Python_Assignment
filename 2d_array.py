class NegativeValueError(Exception):
    def __init__(self, value):
        self.value = value

count = 1
while count == 1:
    try:
        rows = input('Enter number of rows : ')
        cols = input('Enter number of columns : ')
        if int(rows) > 0 and int(cols) > 0:
            arr = []
            for i in range(int(rows)):
                col = []
                for j in range(int(cols)):
                    element = input("Enter the [{}][{}] element : ".format(i, j))
                    col.append(int(element))
                arr.append(col)
            print(arr)
            break
        else:
            raise NegativeValueError("Negative value")

    except NegativeValueError as error:
        print("Exception :", error.value)                                                                                                                                                                            