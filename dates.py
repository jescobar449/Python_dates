#Name: Jose Melquiades Escobar

#make magic numbers into named constants
monthLowRange = 1
monthHighRange = 12
dayLowRange = 1
dayHighRange = 31
yearLowRange = 0
yearHighRange = 99
firstTwoDigitNumber = 10


#Error variable to stop code from progressing
error = 'no'


#Prompt user for the month
month = int (input( 'Enter a month in numeric form: '))


#Verify the month input if it is between 1 and 12. Display error message otherwise.
if month < monthLowRange or month > monthHighRange:
    print ('Error: month was input incorrectly')
    error = 'yes'
    


#Prompt user for the day
day = int (input( 'Enter a day in numeric form: '))

    
#Verify the day input if it is between 1 and 31. Display error message otherwise.
if day < dayLowRange or day > dayHighRange:
    print ('Error: day was input incorrectly')
    error = 'yes'

       
#Prompt user for the year in two digit format
year = int (input ('Enter a year in two digit format: '))


#Verify the year input if it is between 0 and 99. Display error message otherwise.
if year < yearLowRange or year > yearHighRange:
    print ('Error: year was input incorrectly')
    error = 'yes'


#If the inputs are valid, evaluate the magic date.
if error == 'yes':
    print ('')
    print ('Error: invalid inputs')  #display error message if day, month, or year were entered incorrectly
else: 
    if (month * day) == year:        # check for magic number
        if year < firstTwoDigitNumber:   #check for single digit input by user
            yearToStr = str (year)
            year = '0' + yearToStr   #add a zero in front of single digit numbers
        print ('')
        print ('The dats is ', month, '/', day, '/', year, sep = '')    #display for a magic number
        print ('This is a magic date.') 
    else:
        print ('')                      #dispaly for a number that is not magic
        print ('This date is not magic.')


