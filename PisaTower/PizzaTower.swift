//
//  main.swift
//  codeExecutionRunTimeTester
//
//  Created by Pedro Luis Cabrera Acosta on 27/1/18.
//  Copyright © 2018 Pedro Luis Cabrera Acosta. All rights reserved.
//

import Foundation

//1. Original function that does what the problem requires
func pisaTower(n:Int,char:Character)->Void{
         if (n<=1){return }
         var paddingLeft = "\(String(repeating:" ", count: n))"
         print("\(paddingLeft)\(String(repeating:char,count: n))")
         var decrease = 1
         let middleRow = "\(char)\(String(repeating:" ", count: n-2))\(char)"
         while(decrease<n){
             paddingLeft.removeLast()
             print("\(paddingLeft)\(middleRow)")
             decrease+=1
         }
         print("\(String(repeating:" ", count: n-decrease))\(String(repeating:char, count: n))\n")

 }
pisaTower(n:10,char:".")



//2.A little variation, Saving each "row" of the tower in an array.
func pisaTowerRowByRow(n:Int,char:Character)->Array<String>{
    var res_data:Array<String> = []
    if (n<=1){return ["\(char)"]}
    var paddingLeft = "\(String(repeating:" ", count: n))"
    res_data.append("\(paddingLeft)\(String(repeating:char,count: n))")
    var decrease = 1
    let middleRow = "\(char)\(String(repeating:" ", count: n-2))\(char)"
    while(decrease<n){
        paddingLeft.removeLast()
        res_data.append("\(paddingLeft)\(middleRow)")
        decrease+=1
    }
    res_data.append("\(String(repeating:" ", count: n-decrease))\(String(repeating:char, count: n))\n")
    return res_data
}
let towerRows = pisaTowerRowByRow(n:20,char:".")
for row in towerRows{
    print(row)
}
