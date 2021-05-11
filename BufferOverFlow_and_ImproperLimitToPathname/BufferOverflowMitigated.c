#include <stdio.h>
#include <string.h>
#include <stdlib.h>

// function prototype
void copyText(char*);

int main()
{
	char text[20]; // '\n'
	//char copyText[5];
	
	
	
	printf("Enter text to be stored: \n");
	scanf("%19[^\n]",text);
	
	
	printf("The text you entered was: %s\n", text);
	
	//assume that we don't know the text
	int text_len = strlen(text);
	
	printf("length of text is: %d\n", text_len);
	
	copyText(text);
	
}

/*
* Mitigated copy
*/ 

void copyText(char* text){
	//assume that we don't know the text
	int text_len = strlen(text);
	
	// 10 * 8bytes = 80bytes;
	char *copyText = malloc(sizeof(char) * text_len);
	
	if(copyText == NULL){
		printf("Not enough memory to create");
		return;
	}
	
	strcpy(copyText, text);
	
	printf("\nThe copied text is: %s\n");
	printf("%s", copyText);
	
	printf("\nlength of copied text is: %d\n", strlen(copyText));
}