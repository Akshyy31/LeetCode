/**
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var moveZeroes = function (nums) {
    let zero = 0;

    for (let i = 0; i <= nums.length - 1; i++) {
        if (nums[i] != 0) {

            [nums[i],nums[zero]] = [nums[zero], nums[i]]
            zero++

        }
    }
    

};