#include <iostream>
#include <string>
#include <vector>

using namespace std;


struct node{
    int weight;
    string name;
    vector<node*> children;
    node* parent;
};

int main(){
    vector<node> all;


}