#include <iostream>
#include <vector>
using namespace std;
int main()
{
    /*By: Pedro Luis Cabrera Acosta, ing.cabrera.acosta@gmail.com
    I would like you to share your opinion with me,comments, suggestions,bugs.
    compiled with codeblocks 16.01C++11 ISO, 27/06/2016
    */
    cout<<"re-Sorting: Alternate sorting: Given a sorted array of integers(desc or asc order), rearrange the array in such a"<<endl;
    cout<<"way that the first element is first maximum and second element is first minimum."<<endl;
    cout<<"Eg.) Input : {1, 2, 3, 4, 5, 6, 7} Output : {7, 1, 6, 2, 5, 3, 4}"<<endl;
    vector<int> sortedArray = {1,2,3,4,5,6,7,8};//input array to be sorted
    vector<int> alterSortedArray;//alternatibly sorted array
    int left = 0;
    int cont = 0;
    short int direction = 1;//"if is positive, we will be moving from left to right, otherwise, in the other direction"
    int right= sortedArray.size()-1;
    if (sortedArray.size()>0){//we will check the sorting oder, so we should move in the right "direction"
        if (sortedArray[0]>sortedArray[1]){
            left = right;
            right = 0;
            direction=-1;
        }
    }
    while(cont < sortedArray.size()/2){//running from begin to the middle
        alterSortedArray.push_back(sortedArray[right]);
        alterSortedArray.push_back(sortedArray[left]);
        left+= direction;
        right+= direction*(-1);
        cont+=1;
    }
    if(sortedArray.size()%2 == 1){//if the original array values count is odd, ther will be a remainding value right in the middle
         alterSortedArray.push_back(sortedArray[sortedArray.size()/2]);
    }

      for (unsigned int i=0;i<alterSortedArray.size();i++){
            cout<<"Value: "<<alterSortedArray[i]<< endl;
     }
    return 0;
}
