








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

/* Tree A
        A
      /   \
    B      E
  /   \
 C    D

*/

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

let treeA = new Tree(nodeA);
let treeB = new Tree(nodeAy);

console.log('TREE A:', treeA);
console.log('TREE B:', treeB);