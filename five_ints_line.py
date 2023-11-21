#!/usr/bin/env python3
# Created By: Alex M
# Date: nov 5, 2023
# This program gives the sum of user input

def main():
        for counter in range (1000, 2001):
                if counter == 1000 or counter == 2000:
                    print (f"{counter} ",end="")
                elif counter %5 == 0 :
                    print(f" \n {counter} ",end="" )
                else :
                    print (f"{counter} ",end="")




if __name__ == "__main__":
        main()