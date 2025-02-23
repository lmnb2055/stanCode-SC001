"""
File: weather_master.py
Name: Sidney
-----------------------
This program should implement a console program
that asks weather data from user to compute the
average, highest, lowest, cold days among the inputs.
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""

Exit = -100


def main():
    """
	TODO:
	"""

    print("\"Weather Master4.0\"")
    data = int(input('Next temperature: (or -100 to quit) ?  '))
    cold = 0
    day = 0
    a = data
    sum_data = data
    # cold days
    if data < 16:
        cold += 1
    while True:
        # if first data is Exit, it needs to show no temperatures.
        if data == Exit:
            if day == 0:
                # there is no data.
                print('No temperatures were entered.')
                break
        else:
            highest = data
            lowest = data
            # there has been already a data, so day should start with 1.
            day = 1
            while True:

                data = int(input('Next temperature: (or -100 to quit) ?  '))
                if data == Exit:
                    # print temperature data
                    print('Highest temperature =  ' + str(highest))
                    print('Lowest temperature =  ' + str(lowest))
                    print('Average =  ' + str(average))
                    print(str(cold) + '  cold day(s)')
                    break
                else:
                    # calculate the average -> days
                    day += 1
                    # cold days
                    if data < 16:
                        cold += 1
                    # a variable that sum for all data
                    a += data
                    average = a / day
                    if data > highest:
                        highest = data
                    if data < lowest:
                        lowest = data


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
    main()
