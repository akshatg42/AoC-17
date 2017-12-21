#include <iostream>
#include <string>
using namespace std;

int main(){
    string input;
    cin>>input;
    int sum = 0;
    bool garbage = false;
    for(int i=0; i<input.size(); i++){
        if(input[i] == '>'){
            garbage = false;
        }
        if(garbage){
            sum++;
        }
        if(input[i] == '<'){
            if(!garbage){
                garbage = true;
            }
        }
        if(input[i] == '!'){
            if(garbage){
                sum--;
            }
            i++;
        }
    }
    cout<<sum<<endl;
}