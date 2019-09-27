/**
 * @param {string} J
 * @param {string} S
 * @return {number}
 */
var numJewelsInStones = function(J, S) {
    
  let jewelsCount = 0;
  let stonesDictionary = convertStringToObject(S)
  let jewelsArray = J.split('')
  //J: number of stones that are jewels
  //S: String of characters with stone types 

  jewelsArray.map( (char) => {
    if (stonesDictionary[char]) {
      jewelsCount += stonesDictionary[char]
    }
  });
  //Return number of occurances that J is found in S
  return jewelsCount;
};


/**
  *@param {string} str
  *@return {object}
*/
function convertStringToObject(str){
  
  let stringObject = {}
  let stringArray = str.split('')
  
  //for each character in our string array, add it to our stringObject
  for (var i = 0; i < stringArray.length; i++){
    
    let key = stringArray[i]

    if (stringObject[key]){
      stringObject[key] = stringObject[key] + 1
    } else {
      //If the character already exists, add 1 to the value stored
      stringObject[key] = 1
    }
    
  }

  return stringObject  
}