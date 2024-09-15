int main() {
    int num;
    printf("Please Enter Number (0-1000)  : ");
    scanf("%d", &num);

    if (num >= 0 && num <= 100) {
        printf("num : 0 - 100 \n");
        printf("----------------------------------------\n");
        if (num % 2 == 0) {
            printf("%d divided by 2 , result = %.2f \n", num, (float)(num * num));
        }
        if (num % 4 == 0) {
            printf("%d divided by 4 , result = %.2f \n", num, (float)(num * num * num));
        }
        if (num % 5 == 0) {
            printf("%d divided by 5 , result = %.2f \n", num, (float)(num / 2));
        }
        if (num % 8 == 0) {
            printf("%d divided by 8 , result = %.2f \n", num, (float)(num / 2 * 8));
        }
    } else if (num >= 101 && num <= 1000) {
        printf("num : 101 - 1000 : \n");
        if (num % 10 == 0) {
            printf("%d divided by 10 , result = %.2f \n", num, (float)(num * 10));
        }
        if (num % 15 == 0) {
            printf("%d divided by 15 , result = %.2f \n", num, (float)(num / 2 * 8));
        }
    } else {
        printf("Out of Range ! \n Please enter 0 - 1000 \n");
    }
    printf("----------------------------------------\n");

    return 0;
}

