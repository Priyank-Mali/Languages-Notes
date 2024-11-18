
// A recursive function is a function that calls itself somewhere within the body of the function.
// function calling itself
// Recursion and loops work in similar ways. 
// Every recursive function you write has an alternative solution with a loop.

// syntax

// he Three Parts of a Recursive Function
// Every time you write a recursive function, three elements must be present. They are:

// The function definition.
// The base condition.
// The recursive call.

/**
 * 
 * function recursiveFn(){
 *      if(base condition) {
 *           stops recursion if condition is met
 *      } else recursion continues
 *      recursiveFn()
 */

function printNumbers(num){

    if (num>100) return;
    console.log(num);

    printNumbers(++num)
}

printNumbers(10)