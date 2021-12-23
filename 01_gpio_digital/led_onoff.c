#include <wiringPi.h>
#define LED_PIN_1 7
#define LED_PIN_2 0
#define LED_PIN_3 2

int main(void){
    //wiringPisetup();
    wiringPiSetup();
    
    pinMode (LED_PIN_1, OUTPUT);
    pinMode (LED_PIN_2, OUTPUT);
    pinMode (LED_PIN_3, OUTPUT);

    for (int i = 0; i < 5; i++){
       digitalWrite (LED_PIN_1, HIGH) ; delay(2000);
       digitalWrite (LED_PIN_1, LOW) ; delay(0);

       digitalWrite (LED_PIN_2, HIGH) ; delay(2000);
       digitalWrite (LED_PIN_2, LOW) ; delay(0);

       digitalWrite (LED_PIN_3, HIGH) ; delay(2000);
       digitalWrite (LED_PIN_3, LOW) ; delay(0);
    }
    return 0 ;
}