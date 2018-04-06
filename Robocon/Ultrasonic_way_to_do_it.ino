int c=0;
int t1=12, e1=11, t2=8, e2=9;
int d,t;
float dist(int trig,int echo)
{
  digitalWrite(trig,LOW);
  delayMicroseconds(2);
  digitalWrite(trig,HIGH);
  delayMicroseconds(10);
  digitalWrite(trig,LOW);
  delayMicroseconds(2);
 float t=pulseIn(echo,HIGH);
 float d= t*340/20000;
 return d;
}
void setup() 
{
  pinMode(t1,OUTPUT);
  pinMode(t2,OUTPUT);
  pinMode(e1,INPUT);
  pinMode(e2,INPUT);
  Serial.begin(9600);
  Serial.println("Starting....."); 
}
void loop() 
{
  if(dist(t1,e1)<=10)
  {
    c++;
    while(dist(t2,e2)>10){}
    
 }
  if(dist(t2,e2)<=10)
  {
    c--;
    while(dist(t1,e1)>10){}
  }
  if(c<0)
  {
    c=0;
  }
  Serial.print(dist(t1,e1));
  Serial.print("\t"); 
  Serial.println(dist(t2,e2));
  Serial.println("_ _____ _____ ____ _____ __ __  _ _ __ __ __ __ __ __  __ _ __ _ _ _ __ ___ __ __ _ _ _");
  Serial.println(c);
  Serial.println("________________________________________________________________________________________");
delay(1000);
}
