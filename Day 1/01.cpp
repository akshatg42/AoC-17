#include<iostream>
#include<string.h>
using namespace std;

int main(){
    int sum=0;
    string s;
    getline (cin, s);
    int size = s.size();
    for(int i=0; i<size; i++){
        if(s[i] == s[(i+1) % size]){
            sum+=int(s[i])-48;
        }
    }
    cout<<sum<<endl;
}