#include<stdio.h>
#include<stdlib.h>
#include<time.h>
#include<ctype.h>

char board[3][3];

const char PLAYER = 'X';
const char COMPUTER = 'Y';

void resetBoard();
void printBoard();
int checkSpaces();
void playerMove();
void comMove();
char checkWinner();
void printWinner(char);

void main(){

    int winner = ' ';

    resetBoard();
    
    while (winner == ' ' && checkSpaces() != 0)
    {
        printBoard();

        playerMove();
        winner = checkWinner();
        if (winner != ' ' || checkSpaces() == 0)
        {
            break;
        }
        
        comMove();
        winner = checkWinner();
        if (winner != ' ' || checkSpaces() == 0)
        {
            break;
        }
        
        
    }
    printBoard();
    printWinner(winner);
   

}

void resetBoard(){

    for (int i = 0; i < 3; i++)
    {
        for (int j = 0; j < 3; j++)
        {
            board[i][j] = ' ';
        }
        
    }
    
}
void printBoard(){

    printf(" %c | %c | %c ",board[0][0],board[0][1],board[0][2]);
    printf("\n---|---|---\n");
    printf(" %c | %c | %c ",board[1][0],board[1][1],board[1][2]);
    printf("\n---|---|---\n");
    printf(" %c | %c | %c ",board[2][0],board[2][1],board[2][1]);
    printf("\n");
    // printf("\n");

}   
int checkSpaces(){

    int freespaces = 9;

    for (int i = 0; i < 3; i++)
    {
        for (int j = 0; j < 3; j++)
        {
            if (board[i][j] != ' ')
            {
                freespaces --;
            }
            
        }
        
    }
    return freespaces;
    
}
void playerMove(){

    int x;
    int y;

    do
    {
        printf("Enter row #(1-3) : ");
        scanf("%d",&x);
        x--;
        printf("Enter coulmn #(1-3) : ");
        scanf("%d",&y);
        y--;

        if (board[x][y] != ' ')
        {
            printf("Invalid move.\n");

        }
        else
        {
            board[x][y] = PLAYER;
            break;
        }
    } while (board[x][y] != ' ');
    
    
    
}
void comMove(){

    int x,y;

    srand(time(NULL));

    if (checkSpaces() > 0)
    {
        do
        {
            x = rand()%3;
            y = rand()%3;

        } while (board[x][y] != ' ');

        board[x][y] = COMPUTER;
        
    }
    else
    {
        printWinner(' ');
    }
    
    
}
char checkWinner(){
    
    for (int i = 0; i < 3; i++)//check rows
    {
        if (board[i][0] == board[i][1] && board[i][0] == board[i][2])
        {
            return board[i][0];
        }
        
    }

    for (int i = 0; i < 3; i++)//check cols
    {
        if (board[0][i] == board[1][i] && board[0][i] == board[2][i])
        {
            return board[0][i];
        }
        
    }

    //check diagonals

    if (board[0][0] == board[1][1] && board[0][0] == board[2][2])
    {
        return board[0][0];    
    }
    if (board[0][2] == board[1][1] && board[0][2] == board[2][0])
    {
        return board[0][2];
    }

    return ' ';
    
}
void printWinner(char winner){

    if (winner == PLAYER)
    {
        printf("YOU WIN!");
    }
    else if (winner == COMPUTER)
    {
        printf("YOU LOSE!");
    }
    else{

        printf("DRAW!");
    }
    
    
}