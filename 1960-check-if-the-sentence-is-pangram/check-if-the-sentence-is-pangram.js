/**
 * @param {string} sentence
 * @return {boolean}
 */
var checkIfPangram = function(sentence) {
      const news = sentence.toLowerCase().match(/[a-z]/g)
      const unique= new Set(news)
       return unique.size == 26 ? true : false
    };