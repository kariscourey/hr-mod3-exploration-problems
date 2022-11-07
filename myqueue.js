class MyQueue {

    constructor(head=null, tail=null) {
      this.head = head;
      this.tail = tail;
      }

    // Enqueue: add node to tail
    enqueue(val) {

      // Instantiate new node with  value
      var n = new Node(val);

      // if queue is empty
      if (this.head === null) {
        this.head = n;
        this.tail = n;
      } else {
        // if queue has members
        // link for old tail becomes new node
        this.tail.link = n;

        // tail points to new tail
        this.tail = n;
      }

      // enqueue does not need to return a value
      return;

    }
    // dequeue: remove node from head
    dequeue() {

      // if queue empty, return (undefined)
      if (this.head === null) {
        return;
      } else {

        // Temporarily store value for node at head
        var tempValue = this.head.value;

        // Reassign head property to node
        // current head's link points to
        this.head = this.head.link;

        // If final node removed
        // set tail to null as well

        if (this.head === null) {
          this.tail = null;
        }

        // Return value
        return tempValue;
      }
    }
  }
