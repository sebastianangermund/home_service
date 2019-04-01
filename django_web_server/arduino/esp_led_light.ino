#include <ESP8266mDNS.h>
#include <ESP8266WiFi.h>
#include <WiFiClient.h>
#include <ESP8266WebServer.h>

//SSID and Password of your wifi router
const char* ssid = FYLL I WIFI-NAMN HÄR: "";
const char* password = FYLL I WIFI-LÖSEN HÄR: "";

// URL's
String thing_id = FYLL I UUID HÄR: "";

String ping_me = "/" + thing_id + "/";
String state_on = "/" + thing_id + "/set-state=1/";
String state_off = "/" + thing_id + "/set-state=0/";
String get_state = "/" + thing_id + "/get-state/";

// variables
const int PIN = 0;    //GPIO out on ESP
int state = 0;

int port_number = FYLL I PORTNUMMER HÄR: ;


// ESP COMMANDS
ESP8266WebServer server(port_number);

void handlePing() {
  server.send(200, "text/plain", "Hello from Led " + thing_id);
  return;
}

void handleStateOn() {
  digitalWrite(PIN, HIGH);
  state = 1;
  server.send(200, "text/plain", "you just changed the state to ON");
  return;
}

void handleStateOff() {
  digitalWrite(PIN, LOW);
  state = 0;
  server.send(200, "text/plain", "you just changed the state to OFF");
  return;
}

void handleGetState() {
  if (state == 1) {
    digitalWrite(PIN, HIGH);
    server.send(200, "ON");
    return;
  }
  if (state == 0) {
    digitalWrite(PIN, LOW);
    server.send(200, "OFF");
    return;
  }
}

void setup() {
  Serial.begin(115200);
  pinMode(PIN, OUTPUT);
  digitalWrite(PIN, LOW);

  WiFi.begin(ssid, password);     //Connect to your WiFi router
  Serial.println("");

  // Wait for connection
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }

  //If connection successful show IP address in serial monitor
  Serial.println("");
  Serial.print("Connected to ");
  Serial.println(ssid);
  Serial.print("IP address: ");
  Serial.println(WiFi.localIP());  //IP address assigned to your ESP

  server.begin();                  //Start server
  Serial.println("HTTP server started");
  server.on(ping_me, handlePing);
  server.on(state_on, handleStateOn);
  server.on(state_off, handleStateOff);
  server.on(get_state, handleGetState);
}

void loop() {
  server.handleClient();          //Handle client requests
}