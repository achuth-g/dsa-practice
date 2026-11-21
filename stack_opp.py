#include <stdio.h>
#include <stdlib.h>

// Defining the maximum stack capacity (MAX > 15)
#define MAX 20

// Global variables for the stack and top pointer
int stack[MAX];
int top = -1; // -1 indicates the stack is initially empty

// Function Prototypes
void push();
void pop();
void display();
void checkOverflowUnderflow();

int main() {
    int choice;

    while (1) {
        // e. Menu-driven interface
        printf("\n=================================");
        printf("\n--- STACK OPERATIONS MENU ---");
        printf("\n1. Push an Element (Insert)");
        printf("\n2. Pop an Element (Delete)");
        printf("\n3. Demonstrate Overflow/Underflow Status");
        printf("\n4. Display Stack Status & Elements");
        printf("\n5. Exit");
        printf("\n=================================");
        printf("\nEnter your choice: ");
        scanf("%d", &choice);

        switch (choice) {
            case 1:
                push();
                break;
            case 2:
                pop();
                break;
            case 3:
                checkOverflowUnderflow();
                break;
            case 4:
                display();
                break;
            case 5:
                printf("\nExiting the program successfully.\n");
                exit(0);
            default:
                printf("\nInvalid choice! Please choose a option between 1 and 5.\n");
        }
    }
    return 0;
}

// a. Function to Push an Element onto the Stack
void push() {
    int item;
    
    // Check for Stack Overflow
    if (top == MAX - 1) {
        printf("\n[OVERFLOW ERROR]: Cannot push element. The stack has hit its maximum capacity of %d elements!\n", MAX);
        return;
    }
    
    printf("\nEnter the integer element to push: ");
    scanf("%d", &item);
    
    top++;            // Increment top pointer
    stack[top] = item; // Insert item at the top position
    printf("Success: %d has been pushed onto the stack.\n", item);
}

// b. Function to Pop an Element from the Stack
void pop() {
    // Check for Stack Underflow
    if (top == -1) {
        printf("\n[UNDERFLOW ERROR]: Cannot pop element. The stack is completely empty!\n");
        return;
    }
    
    int deleted_item = stack[top]; // Retrieve the top element
    top--;                         // Decrement top pointer
    printf("\nSuccess: Popped element %d from the stack.\n", deleted_item);
}

// c. Function to clearly demonstrate current Overflow and Underflow conditions
void checkOverflowUnderflow() {
    printf("\n--- STACK BOUNDARY MONITOR ---");
    
    if (top == -1) {
        printf("\nCurrent Status: [UNDERFLOW SITUATION]");
        printf("\nExplanation   : The top index is %d. The stack contains 0 elements, meaning any pop execution will fail.\n", top);
    } 
    else if (top == MAX - 1) {
        printf("\nCurrent Status: [OVERFLOW SITUATION]");
        printf("\nExplanation   : The top index has reached %d (MAX-1). The stack is filled to capacity (%d/%d elements). Any subsequent push execution will fail.\n", top, top + 1, MAX);
    } 
    else {
        printf("\nCurrent Status: [NORMAL]");
        printf("\nExplanation   : The stack is operating safely. It currently holds %d elements (Remaining Capacity: %d).\n", top + 1, MAX - (top + 1));
    }
}

// d. Function to display the comprehensive status & contents of the Stack 
void display() {
    // Check if the stack is empty
    if (top == -1) {
        printf("\nThe stack is empty. There are no elements to display.\n");
        return;
    }
    
    printf("\n--- CURRENT STACK STATUS ---");
    printf("\nTop Pointer Index : %d", top);
    printf("\nTotal Elements     : %d / %d", top + 1, MAX);
    printf("\nStack Contents (Top to Bottom):\n");
    
    // Loop from the top down to 0 to mimic the linear structure of a stack
    for (int i = top; i >= 0; i--) {
        if (i == top) {
            printf("| %4d | <-- TOP\n", stack[i]);
        } else {
            printf("| %4d |\n", stack[i]);
        }
    }
    printf("\n");
}
