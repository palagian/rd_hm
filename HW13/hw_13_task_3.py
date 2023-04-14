# 3. В попередньо написаний кастомний Exception додати запис помилки і час її виникнення у файл.
import json

import json
import time

class MyCustomException(Exception):
    """ my custom exception class """

try:
    raise MyCustomException('Custom exception is occurred')

except MyCustomException as ex:
    # getting time of error
    current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

    # saving error data and time of error in dict
    error_data = {"error": str(ex), "time": current_time}

    # opening and saving data into json file
    with open("json_exeption.json", "a") as file:
        json.dump(error_data, file)
        file.write("\n")
    print("Error data has been saved to errors.json file.")