/**
 * @param {string[]} words
 * @return {string[]}
 */
var commonChars = function(words) {
    return [...words[0]].reduce((acc, char) => {
        const minCount = Math.min(...words.map(word => word.split('').filter(c => c === char).length));
        if (minCount > acc.filter(c => c === char).length) {
            acc.push(char);
        }
        return acc;
    }, []);
};

// Example 1:
console.log(commonChars(["bella","label","roller"])); // Output: ["e","l","l"]

// Example 2:
console.log(commonChars(["cool","lock","cook"])); // Output: ["c","o"]
