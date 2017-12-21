#include <iostream>
#include <string>
#include <stack>
using namespace std;

int main(){
    string input;
    cin>>input;
    stack<int> my_stack;
    int curr = 1, sum = 0;
    bool garbage = false;
    for(int i=0; i<input.size(); i++){
        if(input[i] == '{'){
            if(!garbage){
                my_stack.push(curr);
                curr++;
            }
        }
        if(input[i] == '}'){
            if(!garbage){
                int p = my_stack.top();
                my_stack.pop();
                sum+=p;
                curr--;
            }
        }
        if(input[i] == '<'){
            if(!garbage){
                garbage = true;
            }
        }
        if(input[i] == '>'){
            garbage = false;
        }
        if(input[i] == '!'){
            i++;
        }
    }
    cout<<sum<<endl;
}