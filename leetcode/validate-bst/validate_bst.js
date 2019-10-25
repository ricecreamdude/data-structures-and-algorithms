//          10
//        5
//      3
//    1

var isValidBST = function(root) {

  //In this context, Lower and Upper stand for the BOUNDS of the algorithm's accepted values.
  //As the algorithm runs, the upper and lower bounds of the recursive function change to 
  //increasingly limited accepted values. 
  function helper(node, l, u){

    //Allow accepted values to be any value until we start adding constraints.
    let lower = l || -Infinity;
    let upper = u || Infinity;
 
    //Track the value of the current node so it can be used to shrink the boundary of our accepted values
    let val = node.val;

    //End Condition: If node === null, return true;
    if (!node) return true;

    //End Condition: If  lower <= val <= upper, return false;
    if (val <= lower || val >= upper) return false;

    //GO LEFT and only accept No Node or all checks passing conditoins
    if ( !helper(node.left, lower, val) )return false;
    
    //GO RIGHT
    if ( !helper(node.right, val, upper) )return false;

    // Default Condition - return true;
    return true;
  }


  return helper(root)

}