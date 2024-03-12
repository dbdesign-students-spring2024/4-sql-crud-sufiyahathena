
CREATE TABLE restaurants (
    RestaurantID INTEGER PRIMARY KEY,
    Name TEXT NOT NULL,
    Category TEXT,
    PriceTier TEXT,
    Neighborhood TEXT,
    OpeningHours TEXT,
    ClosingHours TEXT,
    AverageRating REAL,
    GoodForKids BOOLEAN
);

CREATE TABLE reviews (
    ReviewID INTEGER PRIMARY KEY,
    RestaurantID INTEGER,
    Rating INTEGER,
    Comment TEXT,
    Date TEXT,
    FOREIGN KEY (RestaurantID) REFERENCES restaurants(RestaurantID)
);

