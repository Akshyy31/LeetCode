/**
 * @param {number[]} nums
 * @return {number}
 */
var findNumbers = function (nums) {
  let count = 0;
  for (let number of nums) {
    digits = String(number);
    digits.split("");
    if (digits.length % 2 == 0) {
      count++;
    }
  }
  return count
};

findNumbers([12, 345, 2, 6, 796]);