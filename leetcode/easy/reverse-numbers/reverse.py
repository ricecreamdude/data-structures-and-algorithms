def reverse(x: int) -> int:              
  negFlag = False
  #convert the number input into a string
  numString = str(x)
  
  #Split the string into an array, so that each digit is an array value
  def split(string):
    nonlocal negFlag

    newArray = [char for char in string]
      
    if newArray[0] is '-':
      negFlag = True
      newArray = newArray[1:len(newArray)]
    
    return newArray

  #If the number is outside of the correct range, return 0
  def validateBitSign(x:int) -> int:
    output = x
    if abs(x) > 2147483648:
      output = 0
    return output
  
  if abs(x) > 2147483648:
    return 0
  

  #Remove the negative sign from beginning of string, and switch
  #the negative flag
  numList = split(numString)
  
  #Reverse the order of the array via [::-1]
  numList = numList[::-1]
  
  #Join the array values into a string again
  reverseString = ''.join(numList)
  
  if negFlag is True:
    reverseString = "-" + reverseString
  
  if abs(int(reverseString)) > 2147483648:
    return 0
  
  #Convert new value into a string
  return int(reverseString)

if __name__ == "__main__":
  print( reverse(123) )