#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <unistd.h>
// #include<conio.h>

typedef struct
{

    int stationery_no;
    char description[100];
    float sale_price;
    int total_quantity;
    int sale_quantity;
    float sale_amount;
    int balance;

} Stationery;

Stationery s[100];
char response;
int count = 0;

//Functions Used
// void Red();
// void Cyan();
// void White();
// void Menu();
// void Exit();
// void backToMenu();
// void DataEntry();
// void ComputeSaleAmount();
// void ShopInformation();
// void ListSaleAmt();
// void ListTotalQuantity();
// void ShopEntry();
// void SaveData();
// void GroupMembers();
//---------------
void Red()
{

    printf("\033[1;31m");
}

void Cyan()
{

    printf("\033[1;48m");
}

void White()
{

    printf("\033[0;39m");
}

void Menu()
{

    int opt;

    printf("\nPlease Wait While Loading..........\n");
    sleep(3);
    printf("\nStationery Shop Information System\n");
    printf("**********************************");
    printf("\n\n");
    printf("1. Stationery Shop Data Entry\n");
    printf("2. Compute Sale Amount\n");
    printf("3. Display Sale Information in Detail\n");
    printf("4. Display Sale List by Sale Amount (Descending order)\n");
    printf("5. Display Sale List by Total Quantity (Descending order)\n");
    printf("6. Stationery Shop Enquiry\n");
    printf("7. Save Stationery Shop Data into File named Stationery.dat\n");
    printf("8. Exit\n");

    do
    {
        printf("Select option number (1-8) : ");
        scanf("%d", &opt);
        fflush(stdin);
    } while (opt < 1 || opt > 8);

    switch (opt)
    {
    case 1:
        DataEntry();
        break;
    case 2:
        ComputeSaleAmt();
        break;
    case 3:
        ShopInformation();
        break;
    case 4:
        ListSaleAmt();
        break;

    case 5:
        ListTotalQuantity();
        break;

    case 6:
        ShopEnquiry();
        break;

    case 7:
        SaveData();
        break;

    case 8:
        Exit();
        break;

    default:
        break;
    }
}
void Exit()
{

    printf("\nTerminating the program........\n");
    sleep(3);
    printf("Program got killed x_x x_x....Byeee!");
    sleep(3);

    int x;
    double y;
    char text[] = "\n\n \t\t\tS\tL\tA\tT\tT\t\t\t";

    printf("\n");
    for (x = 0; text[x] != '\0'; x++)
    {
        Red();
        printf("%c", text[x]);
        for (y = 0; y <= 90000000; y++)
        {
        }
    }
    printf("\n");

    White();

    exit(1);
}
void backToMenu()
{

    char Q;

    printf("\nEnter 'Q' to termimnate else go back to Menus : ");
    scanf("%c", &Q);

    if (Q == 'Q')
        Exit();
    else
        Menu();
}
void DataEntry()
{

    printf("\nStock Data Entry\n");
    printf("******************\n");

    do
    {

        printf("Stationary No : ");
        scanf("%d", &s[count].stationery_no);

        printf("Description : ");
        scanf(" %[^\n]s", &s[count].description);
        // gets(s[count].description);
        // fflush(stdin);

        printf("Sale Price  : ");
        scanf("%f", &s[count].sale_price);

        printf("Total Quantity : ");
        scanf("%d", &s[count].total_quantity);

        printf("Sale Quantity : ");
        scanf("%d", &s[count].sale_quantity);

        count++;

        do
        {

            fflush(stdin);
            printf("Any more data (y/n)? : ");
            scanf("%c", &response);
            fflush(stdin);

        } while (response != 'y' && response != 'n');

    } while (response != 'n');

    backToMenu();
}
void ComputeSaleAmt()
{

    if (count == 0)
    {
        printf("\nYou haven't added any item yet....\n");
        sleep(1);
        printf("Input some data first!");
        sleep(1);
        printf("\nThe system has redirected back to Menu.......\n");
        sleep(1);
        Menu();
    }
    else
    {

        printf("\nComputing sale amounts and balances......\n");
        sleep(3);

        for (int i = 0; i < count; i++)
        {

            s[i].sale_amount = s[i].sale_quantity * s[i].sale_price;
            s[i].balance = s[i].total_quantity - s[i].sale_quantity;
        }

        printf("\nSale amount and Balance are calculated\n");

        backToMenu();
    }
}
void ShopInformation()
{

    if (count == 0)
    {
        printf("\nYou haven't added any item yet....\n");
        sleep(1);
        printf("Input some data first!");
        sleep(1);
        printf("\nThe system has redirected back to Menu.......\n");
        sleep(1);
        Menu();
    }

    else
    {

        printf("\nStationary Shop Information in Detail\n");
        printf("\n**************************\n");

        printf("\nNo\tDescription\tSale_Price\tTotal_Quantity\tSale_Quantity\tSale_Amount\tBalance\n");
        printf("*****\t*****\t*****\t*****\t*****\t*****\t*****\n");

        for (int i = 0; i < count; i++)
        {
            printf("\n%d\t%s\t%0.2f\t%d\t%d\t%.2f\t%d\n", s[i].stationery_no, s[i].description, s[i].sale_price, s[i].total_quantity, s[i].sale_quantity, s[i].sale_amount, s[i].balance);
        }

        backToMenu();
    }
}
void ListSaleAmt()
{

    if (count == 0)
    {
        printf("\nYou haven't added any item yet....\n");
        sleep(1);
        printf("Input some data first!");
        sleep(1);
        printf("\nThe system has redirected back to Menu.......\n");
        sleep(1);
        Menu();
    }

    else
    {

        printf("\nPlease Wait While Sorting...........\n");
        sleep(3);

        // bubble sorting sale amounts
        for (int i = 0; i < count; i++)
        {

            for (int j = i + 1; j < count; j++)
            {

                if (s[i].sale_amount < s[j].sale_amount)
                {

                    Stationery temp = s[i];
                    s[i] = s[j];
                    s[j] = temp;
                }
            }
        }

        printf("\nListed by Sale Amount (Descending Order)\n");
        printf("*********************************");

        printf("\nNo\tDescription\tSale_Price\tTotal_Quantity\tSale_Quantity\tSale_Amount\tBalance\n");
        printf("*****\t*****\t*****\t*****\t*****\t*****\t*****\n");

        for (int i = 0; i < count; i++)
        {
            printf("\n%d\t%s\t%0.2f\t%d\t%d\t%.2f\t%d\n", s[i].stationery_no, s[i].description, s[i].sale_price, s[i].total_quantity, s[i].sale_quantity, s[i].sale_amount, s[i].balance);
        }

        backToMenu();
    }
}
void ListTotalQuantity()
{

    if (count == 0)
    {
        printf("\nYou haven't added any item yet....\n");
        sleep(1);
        printf("Input some data first!");
        sleep(1);
        printf("\nThe system has redirected back to Menu.......\n");
        sleep(1);
        Menu();
    }

    else
    {

        printf("\nPlease Wait While Sorting...........\n");
        sleep(3);

        // bubble sorting sale amounts
        for (int i = 0; i < count; i++)
        {

            for (int j = i + 1; j < count; j++)
            {

                if (s[i].total_quantity < s[j].total_quantity)
                {

                    Stationery temp = s[i];
                    s[i] = s[j];
                    s[j] = temp;
                }
            }
        }

        printf("\nListed by Total Quantity (Descending Order)\n");
        printf("*********************************");

        printf("\nNo\tDescription\tSale_Price\tTotal_Quantity\tSale_Quantity\tSale_Amount\tBalance\n");
        printf("*****\t*****\t*****\t*****\t*****\t*****\t*****\n");

        for (int i = 0; i < count; i++)
        {
            printf("\n%d\t%s\t%0.2f\t%d\t%d\t%.2f\t%d\n", s[i].stationery_no, s[i].description, s[i].sale_price, s[i].total_quantity, s[i].sale_quantity, s[i].sale_amount, s[i].balance);
        }

        backToMenu();
    }
}
void ShopEnquiry()
{

    if (count == 0)
    {
        printf("\nYou haven't added any item yet....\n");
        sleep(1);
        printf("Input some data first!");
        sleep(1);
        printf("\nThe system has redirected back to Menu.......\n");
        sleep(1);
        Menu();
    }
    else
    {

        int enquiry_No;
        char enq_Name[30];
        int opt;

        printf("Enter Shop Enquiry : '1' to search by No. and '2' to search by Description : ");
        scanf("%d", &opt);

        switch (opt)
        {

        case 1:
            printf("\nEnter Stationary No. to serach in the list : ");
            scanf("%d", &enquiry_No);
            fflush(stdin);

            printf("\nPlease Wait While Searching............\n");
            sleep(2);

            for (int i = 0; i < count; i++)
            {

                if (enquiry_No == s[i].stationery_no)
                {

                    printf("\n\nThe system has found your item.\n\n");
                    sleep(2);
                    printf("Stationary No. : %d\n", s[i].stationery_no);
                    printf("Description : %s\n", s[i].description);
                    printf("Sale Price : %.2f\n", s[i].sale_price);
                    printf("Total Quantity : %d\n", s[i].total_quantity);
                    printf("Sale Quantity : %d\n", s[i].sale_quantity);
                }
            }
            break;

        case 2:
            fflush(stdin);
            printf("\nEnter Description to serach in the list : ");
            gets(enq_Name);
            fflush(stdin);

            printf("\nPlease Wait While Searching............\n");
            sleep(2);

            for (int i = 0; i < count; i++)
            {

                if (!strcmp(enq_Name, s[i].description))
                {

                    printf("\n\nThe system has found your item.\n\n");
                    sleep(2);
                    printf("Stationary No. : %d\n", s[i].stationery_no);
                    printf("Description : %s\n", s[i].description);
                    printf("Sale Price : %.2f\n", s[i].sale_price);
                    printf("Total Quantity : %d\n", s[i].total_quantity);
                    printf("Sale Quantity : %d\n", s[i].sale_quantity);
                }
            }
            break;

        default:
            break;
        }

        backToMenu();
    }
}
void SaveData()
{

    FILE *file = fopen("project/stationery.dat", "wb");

    for (int i = 0; i < count; i++)
    {
        fwrite(&s, sizeof(s), 1, file);
    }

    fclose(file);

    backToMenu();
}
void GroupMembers(){

    char member[] = "\n\n\t\t\t<!********Group's Members********!>\t\t\t \n\n"
                    "\t\t\t 1.Han Min Lwin.rollNo(ECE - 008)\t\t\t"
                    "\n\t\t\t 2.Kaung Khant Hein.rollNo(CSE - 009) \t\t\t"
                    "\n\t\t\t 3.Nyan Min Myat.rollNo(ECE - 033)\t\t\t"
                    "\n\n\t\t\t***********************************\t\t\t\n";
    
    printf("\n");
    for (int i = 0; member[i] != '\0'; i++)
    {
        // Cyan();
        printf("%c", member[i]);
        for (int j = 0; j <= 10000000; j++)
        {
        }
    }
    printf("\n");

}
void main()
{
    printf("\n\n");
    printf("Loading from Memory.....");
    sleep(2);
    printf("\nPlease Wait :!\n");
    sleep(3);
    printf("\nProgram Has Started!");

    int i;
    long int j;
    char intro[] = "\n\n \t\t\t< Welcome To Our Program />";

    printf("\n");
    for (i = 0; intro[i] != '\0'; i++)
    {
        Cyan();
        printf("%c", intro[i]);
        for (j = 0; j <= 90000000; j++)
        {
        }
    }
    printf("\n");
    // getch();

    sleep(2);
    White();

    GroupMembers();
    sleep(1);

    Menu();
}
