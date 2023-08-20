package com.lisboa.weather_forecast;

import java.io.IOException;
import org.jsoup.Jsoup;
import org.jsoup.nodes.Document;

public class Fetcher {
    
    /**
     * A class to take data from any site using JSoup.
     */
    
    public String link;
    public Document doc;
    
    /**
    * This piece is a constructor that
    * Automatically connects to the Site
    * Using JSoup as a base
    * @param link
    */
    public Fetcher(String link) {

        this.link = link;
        try {
            Document doc = Jsoup.connect(link).get();
            this.doc = doc;
        }
        catch (IOException e) {
            System.err.println(e);
        }
    }
    
    /**
     * 
     */
    public void robot() {
        try {
            Document rob = Jsoup.connect(link + "/robots.txt").get();
            
            
            
        } catch (Exception e) {
            System.out.println(e);
        }
    }
    
}
