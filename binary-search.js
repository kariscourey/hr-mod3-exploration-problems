function binary_search(lst, value, left=undefined, right=undefined) {
    /*
    Return index of value in sorted list.
    If value is not present or list is empty, return -1

    Keyword arguments:
    lst -- a sorted list
    value -- value to locate in list
    left (optional, default None) -- left bound of index range
    right (optional, default None) -- right bound of index range
    */

    // Set initial index range, return -1 if lst is empty
    if (left === undefined && right === undefined) {
      right = lst.length;

      // Return -1 for empty lst
      if (right === 0) {
        return -1;
      }

      left = 0;
    }

    // Get middle index of the index range
    var mid = Math.floor((left + right) / 2);

    // Base case: last item in index range is not the value
    if (right - left < 1 && lst[mid] != value) {
      return -1;
    }

    // Base case: found value at mid index, return index
    if (lst[mid] == value) {
      return mid;

    } else if (lst[mid] > value) {

      // Recursive case: value checked was greater than arg value
      return binary_search(lst, value, left=left, right=(mid-1));

    } else if (lst[mid] < value) {

      // Recursive case: value checked was less than arg value
      return binary_search(lst, value, left=(mid+1), right=right);

    }
  }

// function binary_search(lst, value, left=undefined, right=undefined) {
//     /*
//     Return index of value in sorted list.
//     If value is not present or list is empty, return -1

//     Keyword arguments:
//     lst -- a sorted list
//     value -- value to locate in list
//     left (optional, default None) -- left bound of index range
//     right (optional, default None) -- right bound of index range
//     */

//     // Set initial index range, return -1 if lst is empty
//     if (left === undefined && right === undefined) {
//       right = lst.length;

//       // Return -1 for empty lst
//       if (right === 0) {
//         return -1;
//       }

//       left = 0;
//     }

//     // Get middle index of the index range
//     var mid = Math.floor((left + right) / 2);

//     // Base case: found value at mid index, return index
//     if (lst[mid] === value) {
//       return mid;
//     }
//     // Base case: value not in lst

//     // Recursive case: check value for new, smaller index range

//     // pass
//   }

// function binary_search(lst, value) {
//     /*
//     Return index of value in sorted list.
//     If value is not present, return -1

//     Keyword arguments:
//     lst -- a sorted list
//     value -- value to locate in list
//     */

//     // Check middle value in this index range

//     // Base case: found value, return index

//     // Base case: value not in lst

//     // Recursive case: check value for new, smaller index range

//     // pass
//   }
