function insertionSort(a) {
    let i = 1;
    while (i < a.length) {
      let j = i;
      while (j > 0 && a[j-1] > a[j]) {
        const tmp = a[j];
        a[j] = a[j - 1];
        a[j - 1] = tmp;
        j -= 1;
      }
      i += 1;
    }
  }
