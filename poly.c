#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>
#include <time.h>


typedef struct { // 첫번째 방식에서 사용할 구조체 선언
    int degree;
    int* coef;
} polynomial_1;

typedef struct { // 두번째 방식에서 사용할 구조체 선언
    int expo;
    int coef;
} polynomial_2;

typedef struct polynomial_3 polynomial_3;
struct polynomial_3 { // 세번째 방식에서 사용할 구조체 선언
    int expo;
    int coef;
    polynomial_3* next;
};

void method_1(FILE* input, FILE* output) {

    typedef struct {
        int degree;
        int* coef;
    } polynomial_1;

    int max = 0, max_1 = 0, max_2 = 0, tmp_degree = 0, tmp = 0, tmp_coef = 0;
    polynomial_1 poly_1, poly_2, poly_sum;
    poly_1.degree = 0, poly_2.degree = 0, poly_sum.degree = 0;

    fscanf(input, "%d %d", &max_1, &max_2); // 다항식의 항 개수 읽기

    max = max_1 > max_2 ? max_1 : max_2; // 합을 저장할 다항식은 두 다항식 중 더 길이가 긴 다항식이어야 하므로, 둘 중 더 큰 놈 뽑아오기


    // 먼저 두 다항식을 읽으며, 다항식을 저장하는 배열의 길이를 선언하기 위한 최고차수를 저장하는 과정을 거친다 //
    for (int i = 0; i < max_1; i++) { // 첫번째 다항식 읽기
        fscanf(input, "%d %d", &tmp_coef, &tmp);
        if (poly_1.degree < tmp) {
            poly_1.degree = tmp;
        }
    }
    for (int i = 0; i < max_2; i++) { // 두번째 다항식 읽기
        fscanf(input, "%d %d", &tmp_coef, &tmp);
        if (poly_2.degree < tmp) {
            poly_2.degree = tmp;
        }
    }

    poly_sum.degree = poly_1.degree > poly_2.degree ? poly_1.degree : poly_2.degree; // 두 다항식의 최고 차수를 비교하여 둘 중 더 큰 놈 뽑기
    // 각 구한 최고차수에 맞추어 동적할당을 진행한다. (Calloc을 이용하여 항이 존재하지 않으면 0으로 초기화)
    poly_1.coef = (int*)calloc((poly_1.degree + 1), sizeof(int));
    poly_2.coef = (int*)calloc((poly_2.degree + 1), sizeof(int));
    poly_sum.coef = (int*)calloc((poly_sum.degree + 1), sizeof(int));

    // 다시 두 다항식을 읽어야함. 타임머신을 타고 돌아가봅시다.
    fseek(input, 0, SEEK_SET);
    fscanf(input, "%d %d", &max_1, &max_2); // 맨 처음은 다항식 수를 나타내기 때문에 다시 읽어서 넘기기 (이거 안하고 읽으면 하나씩 당겨져서 읽어서 뭐 값이 이상해짐)
    for (int i = 0; i < max_1; i++) { // 첫번째 다항식
        int a, b = 0;
        fscanf(input, "%d %d", &a, &b);
        poly_1.coef[poly_1.degree - b] = a;
    }
    for (int i = 0; i < max_2; i++) { // 두번째 다항식 
        int a, b = 0;
        fscanf(input, "%d %d", &a, &b);
        poly_2.coef[poly_2.degree - b] = a;
    }
    for (int i = 0; i <= poly_sum.degree; i++) { // 두 다항식의 합 저장하기
        // 여기 코드를 정말 어떻게 짜야할지 고민했는데, 맨 처음에 i = poly_sum.degree로 두고 시작해서 i--를 진행하는 방법으로 하려 했는데, 알고리즘이 머릿속에 정리가 안되서 해당 방법으로 바꿈.
        // 단순히 둘 중 더 큰 놈의 차수만큼 반복문을 돌리는데 밑에 a, b를 저장하는 조건에서 자기 다항식 길이보다 i가 크면 0을 뱉어서 더해도 의미가 없게 만들어주면 됨.
        // 위의 max = max_1 > max_2 ? max_1 : max_2; 이 부분을 보고 생각난 방법인데 Attach와 Add를 한번에 해결하는 방식임. (한번에 처리하면 좋은거 아니야~?)
        int a = (i <= poly_1.degree) ? poly_1.coef[poly_1.degree - i] : 0;
        int b = (i <= poly_2.degree) ? poly_2.coef[poly_2.degree - i] : 0;
        poly_sum.coef[poly_sum.degree - i] = a + b;
    }

    // 첫번째, 두번째, 두 다항식의 합을 각각 출력하는 코드
    // 사실 값을 먼저 출력하고 뒤에 +를 붙이는 방법도 있지만, 다항식이 끝에 도달했을 때도 +가 붙는 경우의 조건을 해결해야하는 문제가 생김
    // 그래서 생각하기 귀찮아서 그냥 첫번째 항이면 앞에 +를 붙이지 않는 방법으로 작성함. (사실 count조건을 i로 두었다가 첫 항이 0일 때의 +가 붙어서 따로 count를 사용함)
    int count = 0;
    for (int i = 0; i < poly_1.degree + 1; i++) {  // 첫번째 다항식 출력하기
        if (count != 0 && poly_1.coef[i] != 0) {
            fprintf(output, " + ");
        }
        if (poly_1.coef[i] != 0) {
            fprintf(output, "%dx^%d", poly_1.coef[i], poly_1.degree - i);
            if (count ==0){
                count = 1;
            }
        }
    }
    fprintf(output, "\n");
    count = 0;
    for (int i = 0; i < poly_2.degree + 1; i++) { // 두번째 다항식 출력하기
        if (count != 0 && poly_2.coef[i] != 0) {
            fprintf(output, " + ");
        }
        if (poly_2.coef[i] != 0) {
            fprintf(output, "%dx^%d", poly_2.coef[i], poly_2.degree - i);
            if (count == 0) {
                count = 1;
            }
        }
    }
    fprintf(output, "\n");
    count = 0;
    for (int i = 0; i < poly_sum.degree + 1; i++) { // 두 다항식의 합 출력하기
        if (count != 0 && poly_sum.coef[i] != 0) {
            fprintf(output, " + ");
        }
        if (poly_sum.coef[i] != 0) {
            fprintf(output, "%dx^%d", poly_sum.coef[i], poly_sum.degree - i);
            if (count == 0) {
                count = 1;
            }
        }
    }
    fprintf(output, "\n");
    // 메모리 해제
    free(poly_1.coef);
    free(poly_2.coef);
    free(poly_sum.coef);

}

// qsort를 사용하기 위한 비교 함수
// qsort에 대해 아무것도 몰랐어서 이 함수 이해하는데 시간 좀 걸림
int CompareByExpo(const void* a, const void* b) {
    polynomial_2* poly_1 = (polynomial_2*)a;
    polynomial_2* poly_2 = (polynomial_2*)b;
    return poly_2->expo - poly_1->expo;
}

void method_2(FILE* input, FILE* output) {

    int max, which_max, max_1, max_2 = 0;
    polynomial_2* poly, * poly_sum;
    // method_1과 마찬가지로 다항식의 항 갯수를 읽어옴. 다른 점이 있다면 이번엔 차수가 아닌 갯수를 이용해서 동적할당을 한다는 점임
    fscanf(input, "%d %d", &max_1, &max_2);
    // 구조체 배열 두개 만들면 지저분해보일 것 같아서 갯수 두개 더해서 그냥 하나로 만듬
    max = max_1 + max_2;
    which_max = max_1 > max_2 ? max_1 : max_2; // 추후 두 다항식의 합을 저장하기 위한 배열을 동적할당 하려고 둘 중에 큰거 가져감
    poly = (polynomial_2*)calloc(max + 1, sizeof(polynomial_2));

    for (int i = 0; i < max; i++) { // 다항식 일자로 쭉 저장함 
        fscanf(input, "%d %d", &poly[i].coef, &poly[i].expo);
    }
    // 다행히도 input.txt가 첫번째 다항식이 끝난 후에 두번째 다항식이 나와서 각 다항식의 길이만큼 qsort를 해주면 편하게 정렬이 됨 
    qsort(poly, max_1, sizeof(polynomial_2), CompareByExpo);
    qsort(poly + max_1, max_2, sizeof(polynomial_2), CompareByExpo);

    // 다항식의 합을 저장하는 배열을 동적 할당해주는데, 이게 참 애매한 부분인게 운이 더럽게 없으면 첫번째 다항식에 없는 차수만 두번째 다항식에 존재할 수 있어서 크기가 왔다갔다가 더럽게 큼
    // 그래서 C++의 벡터처럼 크기 다 되면 2배씩 늘리기로 함. 처음 크기를 두개 중 큰걸로 잡아놔서 realloc이 많아도 한번 돌아갈건데 메모리 더 아끼는 방법이 더 있나?
    poly_sum = (polynomial_2*)calloc(which_max + 1, sizeof(polynomial_2));
    int count_1 = 0, count_2 = 0, i = 0;
    while (count_1 < max_1 || count_2 < max_2) { // 여기 조건 이거 if문 조건이랑 착각해서 &&로 썼다가 계속 뭐 출력하다 말아가지고 한참 해맸음 하....
        if (i > which_max) {
            which_max *= 2;
            poly_sum = (polynomial_2*)realloc(poly_sum, (which_max + 1) * sizeof(polynomial_2));
            // 위의 주석에 말했던 i가 원래 할당한 길이보다 커지면 realloc하는 부분
        }
        // method 1과 같은 원리로 항이 존재하면 값을, 없으면 0을 뽑게 만들었는데, 여기선 <=쓰니까 뭔가 얘 혼자 하나 중복으로 더함.
        // 이게 내가보기에는 max_1이 인덱스 상으로는 두번째 다항식의 첫번째 항이라서 두번째 항의 첫번째 값이 중복으로 더해지는거 같은데, 이거 맞아요??(진짜모름)
        int a = (count_1 < max_1) ? poly[count_1].coef : 0;
        int b = (count_2 < max_2) ? poly[count_2 + max_1].coef : 0;
        // 여기를 생각을 좀 잘해야했던게, method_1과 다르게 여긴 모든 항의 값이 존재하기 때문에, 인덱스를 같이 올리면 막 지혼자 어떤 값 건너뛰고 난리남...
        // 그래서 두 차수가 같으면 더하고 둘다 올려주기, 첫번째가 높으면 첫번째만 넣고 올려주고, 두번째가 높으면 두번째만 넣고 올려주기 이렇게 나눠서 해줌...
        // 사실 이것도 attach함수랑 add함수로 만들어서 넣어야하는데, 이미 여기서 알고리즘 짜고 한번에 처리하는게 더 편해서 그냥 여기다 만들어서 넣음
        if (poly[count_1].expo == poly[count_2 + max_1].expo) {
            poly_sum[i].coef = a + b;
            poly_sum[i].expo = poly[count_1].expo; // 이부분은 두 차수가 같아서 아무거나 넣고 둘다 올려주고 있고, 밑에서도 이 방법을 채택하고 있는데, 이 방법이 좋은 건지는 잘 모르겠음
            count_1++;
            count_2++;
        }
        else if (poly[count_1].expo > poly[count_2 + max_1].expo) {
            poly_sum[i].coef = a;
            poly_sum[i].expo = poly[count_1].expo;
            count_1++;
        }
        else if (poly[count_1].expo < poly[count_2 + max_1].expo) {
            poly_sum[i].coef = b;
            poly_sum[i].expo = poly[count_2 + max_1].expo;
            count_2++;
        }
        i++;
    }
    // method_1과 같은 메커니즘으로 출력함. 여기서 주의해야할 점이 두가지 있음
    // 1. method_1과 다르게 모든 항이 값이 존재하기 때문에 count를 따로 둘 필요 없이 i가 0인지의 조건으로 해결 가능
    for (int i = 0; i < max_1; i++) {
        if (i != 0 && poly[i].coef != 0) {
            fprintf(output, " + ");
        }
        if (poly[i].coef != 0) {
            fprintf(output, "%dx^%d", poly[i].coef, poly[i].expo);
        }
    }
    fprintf(output, "\n");
    // 2. method_1과 다르게 두 다항식이 한 배열에 연속되게 배치되어있어서 인덱스 설정을 잘해줘야함. 이거 제대로 안하면 지혼자 문워크해서 이전값 출력하고 난리남
    // 이런 사소한 문제때문에 알고리즘 잘 짜도 계속 code=3221225477(참조 오류) 계속 떠서 노트북 부술 뻔 했음. 여기는 양반임
    for (int i = max_1; i < max_2 + max_1; i++) {
        if (i != max_1 && poly[i].coef != 0) {
            fprintf(output, " + ");
        }
        if (poly[i].coef != 0) {
            fprintf(output, "%dx^%d", poly[i].coef, poly[i].expo);
        }
    }
    // 3. 여기서는 인덱스를 i로 사용하지 않은 이유가, 사실 이전 while문에서 이미 외부에서 선언한 i를 항의 갯수만큼 증가시켰음(= i는 두 다항식의 합의 항의 갯수라는 거임)
    // 근데 이 방법이 좋은 건 아닌게, 이전 for문에서 for문 내부의 인덱스를 i로 사용하고 있기에 코드를 보는 사람 입장에서 헷갈릴 수 있음
    fprintf(output, "\n");
    for (int j = 0; j < i; j++) {
        if (j != 0 && poly_sum[j].coef != 0) {
            fprintf(output, " + ");
        }
        if (poly_sum[j].coef != 0) {
            fprintf(output, "%dx^%d", poly_sum[j].coef, poly_sum[j].expo);
        }
    }

    fprintf(output, "\n");
    // 마찬가지로 메모리 해제
    free(poly);
    free(poly_sum);

}

// 사실 이거도 method_3안에 그대로 넣어도 되는데, create_node는 뭔가 있어 보여서 빼놓음. (사실 연결리스트 pdf보면서 이해하고 만들다 보니 이렇게 만들게 됨...)
polynomial_3* create_node(int coef, int expo) {
    polynomial_3* new_node = (polynomial_3*)malloc(sizeof(polynomial_3));
    new_node->coef = coef;
    new_node->expo = expo;
    new_node->next = NULL;
    return new_node;
}

// 이거는 너무 많이 코드가 중복되서 그냥 함수로 뺐음. (사실 이거도 그냥 method_3안에 넣어도 됨)
void append_node(polynomial_3** head, polynomial_3** tail, int coef, int expo) {
    polynomial_3* new_node = create_node(coef, expo);
    if (*head == NULL) {
        *head = *tail = new_node;
    }
    else {
        (*tail)->next = new_node;
        *tail = new_node;
    }
}

void method_3(FILE* input, FILE* output) {
    polynomial_3* head = NULL, * tail = NULL;
    polynomial_3* count_1 = NULL, * break_1 = NULL, * count_2 = NULL;
    polynomial_2* tmp_poly;
    int max_1, max_2 = 0;
    // 두 항의 갯수를 읽고 이전 method_2에서 사용했던 구조체에 method_2에서 사용했던 방법으로 동적 할당을 진행하고 값을 넣어줌 (이건 연결리스로 연결시키기 전 정렬을 위해서 넣었음)
    fscanf(input, "%d %d", &max_1, &max_2);
    tmp_poly = (polynomial_2*)calloc((max_1 + max_2 + 1), sizeof(polynomial_2));

    for (int i = 0; i < max_1 + max_2; i++) {
        fscanf(input, "%d %d", &tmp_poly[i].coef, &tmp_poly[i].expo);
    }
    qsort(tmp_poly, max_1, sizeof(polynomial_2), CompareByExpo);
    qsort(tmp_poly + max_1, max_2, sizeof(polynomial_2), CompareByExpo);
    // 여기까지가 다항식을 읽고 정렬하는 부분임. method_2와 똑같다고 생각하면 됨
    
    // 자 이제 항 갯수만큼 노드를 만들어서 연결리스트로 연결해야함
    for (int i = 0; i < max_1 + max_2; i++) {
        // 사실 연결리스트에서 이해가 가장 오래걸린 부분이 여긴데, new_node에 create_node를 통해 만든 new_node를 넣어주는 건 완벽히 이해했음
        // 근데 문제는 왜 같은 이름의 new_node를 만들어도 값을 덮어씌우는게 아니라 각자의 노드로 존재하는지 이해가 안갔음
        // 이게 사실 head공간에서 동적할당을 계속 하면 할 때마다 다른 공간을 할당받고, 포인터는 그것을 가리키는 변수일 뿐인거임
        // 그래서 이전에 만든 노드가 다른곳에 연결되어있는 링크가 있기만 한다면 데이터는 우리가 계속 찾을 수 있도록 남아있음 (근데 연결이 끊기면 못찾음...)
        polynomial_3* new_node = create_node(tmp_poly[i].coef, tmp_poly[i].expo); // 여기 사실 append_node가 아닌 create_node를 사용한 이유가 break_1, count_1을 저장하기 위해서임
        // 여러개 노드를 생성하고 연결하기에 큐와 같은 개념으로 head포인터와 tail포인터를 사용함.
        if (head == NULL) {
            head = new_node;
            tail = new_node;
            count_1 = new_node;
        }
        else {
            tail->next = new_node;
            tail = new_node;
            if (i == max_1) {
                count_2 = new_node;
                break_1 = new_node; // 이게 마찬가지로 연결리스트를 하나의 경로로 쭉 연결하기 때문에 첫번째 다항식이 어디까지인지 가리키는 포인터가 필요한데 그게 break_1임
            }
        }
    }
    tail->next = NULL; // 다 연결하고 나면 tail은 NULL을 가리키게 하여 연결리스트가 끝을 표시함. (근데 이걸 원형 큐마냥 다시 돌아가게 만들 수는 있는데 여기서 구현은 하지 않음)
    free(tmp_poly);
    // 이게 head를 움직여버리면 이전에 있는 노드를 찾을 수가 없어서 head 위치를 저장하는 current를 써야함.
    polynomial_3* current = head;
    for (int i = 0; i < max_1; i++) {
        if (current != NULL) {
            if (i != 0 && current->coef != 0) {
                fprintf(output, " + ");
            }
            if (current->coef != 0) {
                fprintf(output, "%dx^%d", current->coef, current->expo);
            }
            current = current->next;
        }
    }
    fprintf(output, "\n");
    for (int i = max_1; i < max_1 + max_2; i++) {
        if (current != NULL) {
            if (i != max_1 && current->coef != 0) {
                fprintf(output, " + ");
            }
            if (current->coef != 0) {
                fprintf(output, "%dx^%d", current->coef, current->expo);
            }
            current = current->next;
        }
    }

    // 여기는 좀 복잡하게 보일 수 있는데, 사실 method_2에서 했던 것과 같은 원리임
    polynomial_3* head_sum = NULL, * tail_sum = NULL, * current_sum = NULL; // 합의 연결리스트의 연결을 위한 포인터들 선언 
    while (count_1 != break_1 || count_2 != NULL) {
        // 근데 여기서 아주 주의 깊게 생각해야 하는 부분이 하나 있음
        if (count_1 != break_1 && count_2 != NULL) { // count_1과 count_2 둘 다 다항식의 끝에 도달하지 않았을 때,
            // 여기 if문의 조건이 사실 위의 count_2 != NULL 조건이 없으면 count_2->expo가 NULL을 참조하는 오류가 발생해서 바로 code=3221225477오류가 발생함
            // 그래서 위의 조건을 추가해주고 위 조건문의 예외를 else if로 밑에 처리해줌
            if (count_1->expo == count_2->expo) {
                append_node(&head_sum, &tail_sum, count_1->coef + count_2->coef, count_1->expo);
                count_1 = count_1->next;
                count_2 = count_2->next;
            }
            else if (count_1->expo > count_2->expo) { 
                append_node(&head_sum, &tail_sum, count_1->coef, count_1->expo);
                count_1 = count_1->next;
            }
            else if (count_1->expo < count_2->expo) {
                append_node(&head_sum, &tail_sum, count_2->coef, count_2->expo);
                count_2 = count_2->next;
            }
        }
        else if (count_1 != break_1) { // count_1만 다항식의 끝에 도달하지 못했을 때,
            append_node(&head_sum, &tail_sum, count_1->coef, count_1->expo);
            count_1 = count_1->next;
        }
        else if (count_2 != NULL) { // count_2만 다항식의 끝에 도달하지 못했을 때,
            append_node(&head_sum, &tail_sum, count_2->coef, count_2->expo);
            count_2 = count_2->next;
        }
    }
    tail_sum->next = NULL;
    fprintf(output, "\n");
    current_sum = head_sum;
    while (current_sum != NULL) {
        if (current_sum != head_sum && current_sum->coef != 0) {
            fprintf(output, " + ");
        }
        if (current_sum->coef != 0) {
            fprintf(output, "%dx^%d", current_sum->coef, current_sum->expo);
        }
        current_sum = current_sum->next;
    }
    fprintf(output, "\n");

    // 언제나 있는 메모리 해제 시간
    polynomial_3* tmp_free;
    // 연결리스트 방식은 메모리 해제를 각 노드마다 해줘야하는데 이거 생각보다 조심해야하는게, head를 움직이면 이전 노드를 못찾아서 문제임
    // 그리고 head를 해제하고 넘기려고 하면 head노드의 존재가 세상에서 지워져버리기 때문에 참조할 next도 존재하지 않아서 참조에 오류가 생김 (like 404에러)
    // 그래서 tmp_free에 head정보를 저장하고 head는 다음 노드로 넘기면서 tmp_free를 해제하는거임
    while (head != NULL) {
        tmp_free = head;
        head = head->next;
        free(tmp_free);
    }
    // 다항식을 저장하는 연결리스트는 따로 존재하기 때문에 따로 while문을 돌려줘야함
    while (head_sum != NULL) {
        tmp_free = head_sum;
        head_sum = head_sum->next;
        free(tmp_free);
    }
}


int main() {
    clock_t start_1, end_1, start_2, end_2, start_3, end_3; // 얼마나 걸리는지 측정하기 위해 사용하는 변수들

    // 이거 사실 함수 내에서 fopen,fclose를 각각 사용하려고 했는데, output 커서 이동 시키기 귀찮아서 그냥 main에서 연 상태로 함수에 인자로 전달함.
    FILE* input = fopen("input.txt", "r");
    if (input == NULL) {
        printf("파일을 열 수 없습니다.\n");
        return 1;
    }
    FILE* output = fopen("output.txt", "w");
    if (output == NULL) {
        printf("파일을 열 수 없습니다.\n");
        return 1;
    }
    // 첫번째 방법 실행 및 시간 측정
    start_1 = clock();
    method_1(input, output);
    end_1 = clock();
    fseek(input, 0, SEEK_SET);
    // 두번째 방법 실행 및 시간 측정
    start_2 = clock();
    method_2(input, output);
    end_2 = clock();
    fseek(input, 0, SEEK_SET);
    // 세번째 방법 실행 및 시간 측정
    start_3 = clock();
    method_3(input, output);
    end_3 = clock();
    
    // 걸린 시간 계산 및 출력
    double time_1 = (double)(end_1 - start_1) / CLOCKS_PER_SEC;
    double time_2 = (double)(end_2 - start_2) / CLOCKS_PER_SEC;
    double time_3 = (double)(end_3 - start_3) / CLOCKS_PER_SEC;

    fprintf(output, "%.6f\t%.6f\t%.6f\n", time_1, time_2, time_3);
    // 사실 과 친구들과 토론을 좀 해봤는데, 다들 연결리스트의 시간이 압도적으로 높게 나왔는데 이상하게 내 노트북 환경에서는 1번 -> 3번 -> 2번 순서로 시간이 나타남.
    // 내가 뭔가 의도한 방향과 다르게 설계했나 싶기도 한데, 이해한 바로는 해당 알고리즘이 맞아서 일단 그런갑다 하고 있음.

    // 파일 닫기
    fclose(input);
    fclose(output);
}
