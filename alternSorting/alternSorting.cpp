#include <iostream>
#include <vector>
#include <iomanip>
using namespace std;
int main()
{
    /*By: Pedro Luis Cabrera Acosta, ing.cabrera.acosta@gmail.com
    I would like you to share your opinion with me,comments, suggestions,bugs.
    compiled with codeblocks 16.01C++11 ISO, 27/06/2016
    */
    cout <<"Alternate sorting: Given an UNSORTED array of integers, rearrange the array in such a way "<<endl;
    cout<<"that the first element is first maximum and second element is first minimum. " << endl;
    cout<<"Version 1.0" << endl;
    cout<<"In this version i am sorting the array using an unorthodox approach, and by that I mean not doing what most would"<<endl;
    cout<<"think and use a sorting algorithm with a well-earned reputation for easy way to reorder the data in the array. This"<<endl;
    cout<<"in order to compare the performance of this approach against other more 'popular'" << endl;
    vector<int> unsortedArray(99);
    for (int i=0;i<unsortedArray.size();i++){
            unsortedArray[i] = i;
    }
    int maxV = unsortedArray[0];
    int minV = unsortedArray[0];
    int temp1 = 0, temp2 = 0,sortedPos= 0,posMax= 0, posMin= 0,other=0;
    while(sortedPos < unsortedArray.size()){
        maxV = unsortedArray[sortedPos];
        minV = unsortedArray[sortedPos];
        for (unsigned int i=sortedPos;i<unsortedArray.size();i++){
                if (unsortedArray[i]>=maxV){
                    maxV=unsortedArray[i];
                    posMax = i;
                }
                if (unsortedArray[i]<=minV){
                    minV=unsortedArray[i];
                    posMin = i;
                }
        }
        temp1 = unsortedArray[sortedPos];
        temp2 = unsortedArray[sortedPos+1];
        unsortedArray[sortedPos] = maxV;
        unsortedArray[sortedPos+1] = minV;
        if ((posMax > sortedPos + 1) || (posMin > sortedPos+2)){
            other = 0;
            if (posMax > sortedPos + 1){
                if (sortedPos != posMin){
                    unsortedArray[posMax] = temp1;
                    other = temp2;
                }else{
                    unsortedArray[posMax] = temp2;
                    other = temp1;
                }
            }else{
                if (posMax==sortedPos){
                   other = temp2;
                }else{
                    other = temp1;
                }
            }
            if (posMin > sortedPos + 1){
                unsortedArray[posMin] = other;
            }
        }
        sortedPos+=2;
    }
   for (unsigned int i=0;i<unsortedArray.size();i++){
            cout<<"Value: "<<unsortedArray[i]<< endl;
    }
    return 0;
}
