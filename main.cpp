//  Text to ASCII Converter
//
//  Created by William Dickinson on 9/11/19.
//  Copyright (c) 2019 Grand Valley State University. All rights reserved.
//

#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int main(int argc, const char * argv[])
{
    char filename[800];
    char token;
    ifstream file;
    int ASCIIval;
        
    string summary = "ASCIIEncoding.txt";
    ofstream summaryFile(summary.c_str());
        
    cout <<"Please input filename: ";
    cin >>filename;
    cout << '\n';
    file.open(filename,ios::in);
    if (!file)
        cout <<"So sorry. I could not open your file. :-( \n";
    else {
        file.get(token);
        while (!file.eof()) {
            ASCIIval = int(token);
            if (ASCIIval>=1000) // Unicode encountered
                cout << "Conversion Fail. There is somekind of unicode character in your file somehow. Sorry!";
            else
            {
                if (ASCIIval<10) //To convert to three digits pad these values with two zeros
                    summaryFile << "00"; 
               else 
                    {
                        if ((10 <= ASCIIval) and (ASCIIval < 100)) //To convert to three digits pad these values with one zero
                        summaryFile << "0";
                    }
               //now write the value out
               summaryFile <<  int(token);
            }
            //get the next token
            file.get(token);
        }
        summaryFile << endl;
    }
    file.close();
    summaryFile.close();
    exit(0);
};


