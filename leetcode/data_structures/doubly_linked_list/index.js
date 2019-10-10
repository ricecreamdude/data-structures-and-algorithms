class DoublyLinkedList{

  /* @param {number} capacity */
  constructor(capacity){
    this.head = null;
    this.tail = null;
    this.capacity = capacity;
  }

  /* Add a node at the front */

  addToFront(newNode){
    
    //Assign new node's next value to current head
    newNode.next = this.head;
    
    if (this.head){
      this.head.prev = newNode
    }

    this.head = newNode
  }



}

class Node{
  /* @param {string} data */
  constructor(data){
    this.data = data;
    this.next = null;
    this.prev = null;
  }

}

let test = new DoublyLinkedList(4);
let testNode = new Node(3);
let testNodeTwo = new Node(5);

test.addToFront(testNode);
test.addToFront(testNodeTwo);

console.log(test)