//: Playground - noun: a place where people can play

import UIKit
import Darwin

/*given a function that calculates and return a random Value between  0 to n,we must create a function that
 return a RANDOM value  between 0 to n+1.
 Conditions:
 1.- We can  not  modify the original function that calculate the random value (arc4random_uniform) and
 2.- Everytime we cal our random Function we can only use the same value for the argument n
 Example:
 suppose we have a function call random and it recive a parameter n of type Integer and it returns a random value between 0-n
 so if we call random(n) the reuslt can be 0,1,2...n-1,n
 you have to create a function that recives the right limit(n in our example) and return a random value between 0,1,2,3... n-1,n,n+1
 
 myfunc(n){
    mycode here, remember
    return value between 0 and n+1
 }
 
*/

func randN(n:UInt32)->Int{//randN is create to make it clearer and avoid using arc4random_uniform name
   return  Int(arc4random_uniform(n))//arc4random_uniform willnreturns a value between 0 and n-1, so our goal in this case will be, get a value between
    //0 and n
    
}

func randomPlusOne(n:UInt32)->Int{
    return randN(n) + Int(round(Float(randN(n))/Float(Int(n-1))))
}


let n:UInt32 = 10// using n=10 remember that our swift random function arc4random_uniform will return values between 0 and 10-1 in this case

for x in 1..<50{
    arc4random_uniform(n)//here we can get random values between 0 and n-1
    }
for x in 1..<50{
    randomPlusOne(n)//but now here we can get random  values between 0 and n, as we want it
  
}
