###   

```java
class ParkingSystem {
    int bigParking;
    int mediumParking;
    int smallParking;

    public ParkingSystem(int big, int medium, int small) {
        bigParking = big;
        mediumParking = medium;
        smallParking = small;
    }
    
    public boolean addCar(int carType) {
        if (carType == 1 && bigParking > 0) {
            return bigParking--> 0;
        } else if (carType == 2 && mediumParking > 0) {
            return mediumParking--> 0;
        } else if (carType == 3 && smallParking > 0) {
            return smallParking--> 0;
        }
        return false;
    }
}
```  

- 考虑并发情况，使用原子类  

```java
class ParkingSystem {
    AtomicInteger big;
    AtomicInteger medium;
    AtomicInteger small;

    public ParkingSystem(int big, int medium, int small) {
        this.big = new AtomicInteger(big);
        this.medium = new AtomicInteger(medium);
        this.small = new AtomicInteger(small);
    }
    
    public boolean addCar(int carType) {
        switch(carType) {
            case 1:
                return big.decrementAndGet() >= 0;
            case 2:
                return medium.decrementAndGet() >= 0;
            case 3: 
                return small.decrementAndGet() >= 0;
            default:
                return false;
        }
    }
}
```

