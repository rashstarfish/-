package com.ccit.pojo;

public class Hotel {
    private Integer id;
    private String name;
    private String commentNum;
    private String price;
    private String city;
    private String area;
    private String address;
    private String lat; // 假设这是纬度
    private String log; // 假设这是经度，但通常我们使用 "lng" 来表示经度
    private String rating;
    private String environmentalRating;
    private String healthRating;
    private String serviceRating;
    private String facilityRating;
    private String tag;
    public Hotel() {}

    @Override
    public String toString() {
        return "Hotel{" +
                "id=" + id +
                ", name='" + name + '\'' +
                ", commentNum='" + commentNum + '\'' +
                ", price='" + price + '\'' +
                ", city='" + city + '\'' +
                ", area='" + area + '\'' +
                ", address='" + address + '\'' +
                ", lat='" + lat + '\'' +
                ", log='" + log + '\'' +
                ", rating='" + rating + '\'' +
                ", environmentalRating='" + environmentalRating + '\'' +
                ", healthRating='" + healthRating + '\'' +
                ", serviceRating='" + serviceRating + '\'' +
                ", facilityRating='" + facilityRating + '\'' +
                ", tag='" + tag + '\'' +
                '}';
    }

    public Integer getId() {
        return id;
    }

    public void setId(Integer id) {
        this.id = id;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getCommentNum() {
        return commentNum;
    }

    public void setCommentNum(String commentNum) {
        this.commentNum = commentNum;
    }

    public String getPrice() {
        return price;
    }

    public void setPrice(String price) {
        this.price = price;
    }

    public String getCity() {
        return city;
    }

    public void setCity(String city) {
        this.city = city;
    }

    public String getArea() {
        return area;
    }

    public void setArea(String area) {
        this.area = area;
    }

    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }

    public String getLat() {
        return lat;
    }

    public void setLat(String lat) {
        this.lat = lat;
    }

    public String getLog() {
        return log;
    }

    public void setLog(String log) {
        this.log = log;
    }

    public String getRating() {
        return rating;
    }

    public void setRating(String rating) {
        this.rating = rating;
    }

    public String getEnvironmentalRating() {
        return environmentalRating;
    }

    public void setEnvironmentalRating(String environmentalRating) {
        this.environmentalRating = environmentalRating;
    }

    public String getHealthRating() {
        return healthRating;
    }

    public void setHealthRating(String healthRating) {
        this.healthRating = healthRating;
    }

    public String getServiceRating() {
        return serviceRating;
    }

    public void setServiceRating(String serviceRating) {
        this.serviceRating = serviceRating;
    }

    public String getFacilityRating() {
        return facilityRating;
    }

    public void setFacilityRating(String facilityRating) {
        this.facilityRating = facilityRating;
    }

    public String getTag() {
        return tag;
    }

    public void setTag(String tag) {
        this.tag = tag;
    }
}
