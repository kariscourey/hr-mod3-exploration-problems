class MyNode {
    constructor(value, link=null) {
      this.value = value;
      // add link property
      this.link = link;
    }
  }


class MySll {

  constructor(head=null, tail=null) {
    this.head = head;
    this.tail = tail;
    this._length = 0;
    }

  // "read-only" length property
  get length() {
      return this._length;
  }
  // Comments truncated

  traverse(idx) {

    // If list empty
    // If idx out of bounds
    // If idx not an integer
    if (
      this._length == 0
      || idx > (this._length - 1)
      || idx != parseInt(idx)
    ) {
      return;
    }

    var i = 0;
    var _currentNode = this.head;

    while (i < idx) {
      _currentNode = _currentNode.link;
      i++;
    }

    return _currentNode;
  }

  insert(val, idx=null) {

    var _newNode = new MyNode(val);

    // idx null (default)
    if (idx === null) {
      idx = this._length;
    }

    if (this.head === null) {
      // list empty, inserting first node
      this.head = _newNode;
      this.tail = _newNode;
      this._length++;
      return;

    } else if (idx == this._length) {
      // insert after tail
      this.tail.link = _newNode;
      this.tail = _newNode;
      this._length++;
      return;

    } else if (idx == 0) {
      // insert before head
      _newNode.link = this.head;
      this.head = _newNode;
      this._length++;
      return;

    } else {
      // insert between two nodes
      var thisIdxNode = this.traverse(idx - 1);
      var nextIdxNode = thisIdxNode.link;

      _newNode.link = nextIdxNode;
      thisIdxNode.link = _newNode;
      this._length++;
      return;
    }
  }

  remove(idx=0) {
    // if idx 0
    if (idx == 0) {
      var _val = this.head.value;
      this.head = this.head.link;
      this._length -= 1;

      if (this._length == 0) {
        this.tail = null;
      }

      return _val;
    }
    // other indices
    var previousIdxNode = this.traverse(idx - 1);
    var thisIdxNode = previousIdxNode.link;

    _val = thisIdxNode.value;
    var nextIdxNode = thisIdxNode.link;

    // connect previous node to next
    previousIdxNode.link = nextIdxNode;

    if (nextIdxNode == null) {
      this.tail = previousIdxNode;
    }

    this._length -= 1;
    return _val;
  }

}


//   class MySll {

//     constructor(head=null, tail=null) {
//       this.head = head;
//       this.tail = tail;
//     }

//     // Length instance attribute

//     // Value can be returned
//     // from any location

//     // Values can be inserted
//     // into the list at any index

//     // Values can be removed
//     // from the list from any location

//     // The list can be searched

//   }
