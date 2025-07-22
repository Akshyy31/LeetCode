/**
 * @param {number[]} nums
 * @return {number}
 */
var majorityElement = function (nums) {
    const obj = {}
    const majority = Math.floor(nums.length / 2)
    for (i of nums) {
        obj[i] = (obj[i] || 0) + 1
        if (obj[i] > majority) {
            return i
        }
    }



};