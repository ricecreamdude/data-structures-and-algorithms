/* Tree A
        A
      /   \
    B      E
  /   \
 C    D

*/
class Tree{
  constructor(node){
    this.root = node;
  }
}

class Node{
  constructor(value){
    this.value = value;
    this.right = null;
    this.left = null;
  }
}


let nodeA = new Node('A')
let nodeB = new Node('B')
let nodeC = new Node('C')
let nodeD = new Node('D')
let nodeE = new Node('E')

nodeA.left = nodeB
nodeA.right = nodeE
nodeB.left = nodeC
nodeB.right = nodeD

/* Tree B
        A
      /   \
    E      B
         /   \
        D      C
*/

let nodeAy = new Node('A')
let nodeBe = new Node('B')
let nodeCe = new Node('C')
let nodeDe = new Node('D')
let nodeEe = new Node('E')

nodeAy.left = nodeEe;
nodeAy.right = nodeBe;
nodeBe.left = nodeDe;
nodeBe.right = nodeCe;

function checkIfReverse(nodeA, nodeB){

  let isReverse = true;

  function traverse(nodeA, nodeB){
    if(nodeA.value !== nodeB.value){
      console.log('MISMATCHED VALUES');
      return isReverse = false;
    }
    if(nodeA.left){
      if(nodeB.right){
        traverse(nodeA.left, nodeB.right);
      } else {
        console.log('NODE A LEFT DOES NOT MATCH NODE B RIGHT')
        return isReverse = false;
      }
    }
    if(nodeA.right){
      if(nodeB.left){
        traverse(nodeA.right, nodeB.left);
      } else {
        console.log('NODE A RIGHT DOES NOT MATCH NODE B LEFT')
        return isReverse = false;
      }
    }
  }

  traverse(nodeA, nodeAy);

  return isReverse;

};

console.log('RESULT:',checkIfReverse(nodeA, nodeB) )







