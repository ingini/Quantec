switch보다 if else를 선호하지만 switch문이 종종 유용하게
사용되는 경우가 있습니다.

예를 들어 어떤 사건(이벤트)에 따라 상태(플래그)값이 변경되고
그 상태값에따라 수행해야 할 로직이 다르다면 보통은 if문을 쓰게 될겁니다.

/* 일반적인 코딩 방식 */
int flag = 0;
...
flag = get_current_status(stdin);

if(flag == 0)
    printf("%s", "stop");
else if(flag == 1)
    printf("%s", "play");
else if(flag == 2)
    printf("%s", "pause");
else
    ;
그런데 만약 상태값이 0일때 1, 2 상태의 로직도 수행해야 하고
상태값이 1 일때는 2 상태의 로직이 수행되어야 할 경우가 있습니다.

이런 비슷한 상황때문에 패턴이란게 있긴하지만 트릭을 쓰자면
switch문의 제어특성을 사용합니다.

switch(flag)
{
    case 0:
        printf("%s", "stop");
    case 1:
        printf("%s", "play");
    case 2:
        printf("%s", "pause");
        break;
    default:
        break;
}

만약 사용하는 언어에선 case문에 break를
반드시 사용해야 한다면 break 대신 goto문을 사용하면 됩니다.