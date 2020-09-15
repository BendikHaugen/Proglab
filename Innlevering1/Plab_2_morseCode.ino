const int buttonPin = 2;     
unsigned long time_ = 0;
unsigned long pressStart = 0;
unsigned long pressDuration = 0;
int sent = 0; //To keep track on how many blank spaces have been sent
int buttonState = 0;    

void setup() {
  Serial.begin(9600);  
  pinMode(buttonPin, INPUT);  
     
}



void loop(){ 
  buttonState = digitalRead(buttonPin); // Reeds button state
  if(buttonState == 0){ //if button is pressed
    time_ = millis(); // sets time_ to be time since program start
    pressStart = millis(); // registers when you pressed
    while(buttonState == 0){
      buttonState = digitalRead(buttonPin); // While the button is pressed, keep regestering how long since programstart
    }
    pressDuration = millis() - pressStart; //calculates time button is pressed
  }
  if(pressDuration > 1000 && pressDuration >0){ //uses pressDuration to determine wether to send 0, 1, " " or N
    Serial.print("N");
    sent = 0;
  }else if(pressDuration > 300 && pressDuration > 0){
    Serial.print("1");
    sent = 0;
  } else if (pressDuration > 0) {
    Serial.print("0");
    sent = 0;
  }
  pressDuration = 0;
  if(millis() - time_ > 1500 && sent == 0){
    Serial.print(" ");
    time_ = millis();
    sent = 1; //makes sure you dont sent two or more spaces
  }
  
}
