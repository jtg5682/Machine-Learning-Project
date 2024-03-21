import socket

def input_data():
    dataX =input ("Input X: ")
    dataY =input ("Input Y: ")
    dataZ =input ("Input Z: ")
    dataXR =input ("Input XR: ")
    dataYR =input ("Input YR: ")
    dataZR =input ("Input ZR: ")
    return dataX, dataY, dataZ, dataXR, dataYR, dataZR

def gooddata(test_data):
    try: 
        float(test_data[0])
        float(test_data[1])
        float(test_data[2])
        float(test_data[3])
        float(test_data[4])
        float(test_data[5])
        return True
    except ValueError:
        return False
    
    
def main():

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('127.0.0.1', 5024))

    while True:
        dataX, dataY, dataZ, dataXR, dataYR, dataZR = input_data()
        mydata = dataX+","+dataY+","+dataZ+","+dataXR+","+dataYR+","+dataZR
        test_data = [dataX, dataY, dataZ, dataXR, dataYR, dataZR]

        result = gooddata(test_data)

        if dataX == "\n" or dataY == "\n" or dataZ == "\n":
            print("No data")
            continue
        elif dataX == "stop" or dataY == "stop" or dataZ == "stop":
            print("stopped.")
            break
        elif result == False: 
            print("Please input a numeric value: ")
            continue
        else:
            s.send(bytes(str(mydata),"utf-8"))
            print("sent :)")

main()