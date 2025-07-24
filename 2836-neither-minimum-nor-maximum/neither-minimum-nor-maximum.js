/**
 * @param {number[]} nums
 * @return {number}
 */
var findNonMinOrMax = function(nums) {
    
    
     nums.sort((a,b)=>a-b)
     if(nums.length<3){
         return -1
     }else{
         return nums[parseInt(nums.length/2)]
     }
     
};

console.log(findNonMinOrMax([1,2]))