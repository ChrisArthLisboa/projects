package com.lisboa.weather_forecast;


public class Weather_forecast {
    
    public static void main(String[] args) {
        
        Fetcher teste = new Fetcher("https://weather.com");
           
        teste.robot();
    }
}
