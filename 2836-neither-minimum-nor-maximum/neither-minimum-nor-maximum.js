/**
 * @param {number[]} nums
 * @return {number}
 */
var findNonMinOrMax = function(nums) {
    
    function s(a,b){
        return a-b
    }
     nums.sort(s)
     if(nums.length<3){
         return -1
     }else{
         return nums[parseInt(nums.length/2)]
     }
     
};

console.log(findNonMinOrMax([1,2]))