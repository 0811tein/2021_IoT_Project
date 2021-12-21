#include <wiringPi.h>
#define LED_RED 10
#define LED_YELLOW 9
#define LED_GREEN 11
int main (void)
{
  //wiringPiSetup () ;
  wiringPiSetupGpio();
  pinMode (LED_RED, OUTPUT) ;
  pinMode (LED_YELLOW, OUTPUT) ;
  pinMode (LED_GREEN, OUTPUT) ;
  for (int i=0; i<5; i++)
  {
    digitalWrite (LED_RED, HIGH) ; delay (1000) ;
    digitalWrite (LED_RED,  LOW) ; delay (1000) ;
    digitalWrite (LED_YELLOW, HIGH) ; delay (1000) ;
    digitalWrite (LED_YELLOW,  LOW) ; delay (1000) ;
    digitalWrite (LED_GREEN, HIGH) ; delay (1000) ;
    digitalWrite (LED_GREEN,  LOW) ; delay (1000) ;

  }
  return 0 ;
}