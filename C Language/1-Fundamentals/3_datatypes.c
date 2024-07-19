# include<stdio.h>
# include<stdbool.h>

int main(){

/**
 * 
    Type	                    Size (bytes)	                Format Specifie
    
    int	                    at least 2, usually 4	        %d, %i
    char	                1	                            %c
    float	                4	                            %f
    double	                8	                            %lf
    short int	            2 usually	                    %hd
    unsigned int	        at least 2, usually 4	        %u
    long int	            at least 4, usually 8	        %ld, %li
    long long int	        at least 8	                    %lld, %lli
    unsigned long int	    at least 4	                    %lu
    unsigned long long int	at least 8	                    %llu
    signed char	            1	                            %c
    unsigned char	        1	                            %c
    long double	            at least 10, usually 12 or 16	%Lf
 */


    /**
     * Integer -----------------------------------------------
     */
    // int mynum = 5;

    // float myfloat = 2.3;
    double mynum = 19.99;
    printf("%lf",mynum);

    /**
     * float ------------------------------------------------
     */
    float a = 5;
    float b = 2;
    printf("\n%f",a/b);
    float c = 5/2;
    printf("\n%f",c);

    // float vs. double
    // The precision of a floating point value indicates how many digits the value can have after the decimal point. 
    // The precision of float is six or seven decimal digits, while double variables have a precision of about 15 digits. 
    // Therefore, it is often safer to use double for most calculations - but note that it takes up twice as much memory as float (8 bytes vs. 4 bytes).

    // Scientific Numbers
    // "e" or "E" to indicate the power of 10:
    mynum = 12E4;
    printf("\n%lf",mynum);

    /**
     * character ----------------------------------------------------------
     */
    char mychar = 'A';

    printf("\n%c",mychar);
    printf("\n%d",mychar); // ASCII value

    /*
    ASCII stands for the "American Standard Code for Information Interchange".
    0-9 -> 48-57
    A-Z -> 65-90
    a-z -> 97-122
    */

    // char name = "priyank";
    // printf("\n%c",name); //error

    /**
     * String -----------------------------------------------------------
     */

    // char stringname[] = "text"
    char name[] = "priyank mali";
    printf("\n%s",name);

    
    /**
     * Bolean -----------------------------------------------------------
     */

    bool isprogrammingfun = false;
    printf("\n%d",isprogrammingfun);
    
    // /*
    // Memory size:

    // int	    2 or 4 bytes
    // float	4 bytes
    // double	8 bytes
    // char	    1 byte
    // bool	    1 byte

    // */
    // printf("\n%lu",sizeof(int));
    // printf("\n%lu",sizeof(float));
    // printf("\n%lu",sizeof(double));
    // printf("\n%lu",sizeof(char));
    
    /*
    Note that we use the %lu format specifer to print the result, 
    instead of %d. It is because the compiler expects the sizeof operator to return a long unsigned int (%lu),instead of int (%d). 
    On some computers it might work with %d, but it is safer to use %lu.
    */    

//    int item = 50;
//    float costPerItem = 9.99;
//    float totalCost = item * costPerItem;
//    char currency = '$';

//    printf("\nNumber of items: %d",item);
//    printf("\nCost per item: %.2f",costPerItem);
//    printf("\nToatl cost: %c %.2f",currency,totalCost);

    /*
    Type conversion

    1.) Implicit Conversion( done automatically by the compiler )
    2.) Explicit Conversion
    */


    float x = 9;
    printf("\n%f",x);
    int z = 9.99;
    printf("\n%d",z);

    printf("\n%d",5/2);

    float div1 = 5/2;
    printf("\n%f",div1);


    // Explicit
    div1 = (float)5/2;
    printf("\n%f",div1);

    int q = 10;
    int u = 12;
    printf("%.2f",(float)(q/u));
}