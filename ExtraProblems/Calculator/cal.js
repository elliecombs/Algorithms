// "- 3 * 4 5"
function calculator(str) {
    const operators = {
        '+': (a, b) => a + b,
        '-': (a, b) => a - b,
        '*': (a, b) => a * b,
        '/': (a, b) => a / b,
    }
    
    const characters = str.split(" "); // ["-", "3", "*", "4", "5"]
    
    const stack = [];
    let isPreviousDigit = false;
    
    const calculateStack = () => {
        const currentDigit = stack.pop()
        const previousDigit = stack.pop();
        const operator = stack.pop(); 
        
        isPreviousDigit = false;
        if(stack.length >= 2) {
            const oneMorePreviousDigit = stack.pop();
            if (Number.isInteger(oneMorePreviousDigit)) {
                isPreviousDigit = true;
            }
            stack.push(oneMorePreviousDigit);
        }
        stack.push(operators[operator](previousDigit, currentDigit));
        
    }
    
    for(const character of characters) { 

        // Somehow make a while loop to seperate stack
        if(character in operators) {  
            isPreviousDigit = false; 
            stack.push(character)
        } else {
            const number = Number(character)
            if(isPreviousDigit) {
                while(isPreviousDigit) {
                    calculateStack(number)
                    const previousCharacter = stack.pop()
                    if(previousCharacter in operators) {
                        isPreviousDigit = false;
                    }
                } 
            } else {
                isPreviousDigit = true;
                stack.push(number);
            }
        }
    }
    
    //
    while(stack.length >= 3) {
        const currentDigit = stack.pop();
        calculateStack(currentDigit);
    }
    
    if(stack.length > 1) {
        throw new Error("Uh oh");
    }
    
    return stack.pop();
}


//   it("returns zero", function() {
// console.log(calculator("0") === 0);
// // "0" !== 0
// // 0 === 0

// //   it("calculates addition", function() {
// console.log(calculator("+ 3 4") === 3 + 4);

// //   it("calculates subtraction and multiplication", function() {
// console.log(calculator("- 3 * 4 5") === 3 - (4 * 5));  // -17

/**
 * 
 * operators = {
 *  '+': (a, b) => a + b
 *  '-': ...
 * }
 * 
 * characters = split(string, " ")
 * isPreviousDigit = false
 * for all character in characters:
 *  if character is operator:
 *      isPreviousDigit = false
 *      push()
 *      continue
 *  else 
 *      if (ifPreviousDigit):
 *          previousDigit = stack.pop()
 *          opereator = stack.pop()
 *          stack.push(operators[operator](previousDigit, character))
 *      else:
 *          stack.push(character)
 *  return stack.pop()
 */

//   it("calculates addition and multiplication", function() {
// console.log(calculator("* + 3 4 5") === (3 + 4) * 5);  // 35

console.log(calculator("* + + + 1 * 13 2 3 4 5") === ((((13 * 2) + 1) + 3) + 4) * 5); 
