# Revelant metadata for input csv files

## circuits.csv

* **circuitId**: Unique integer identifier of the circuit.
* **circuitRef**: Unique string identifier of the circuit.
* **name**: Official name of the circuit.
* **location**: City where the circuit is located.
* **country**: Contry wher the circuit is located.
* **lat**: Latitute of the circuit
* **lng**: Longitude of the circuit.
* **alt**: Altitude of the circuit.
* **url**: Wikipedia link.

## constructors.csv

* **constructorId**: Unique integer identifier of the constructor.
* **constructorRef**: Unique string identifier of the constructor.
* **name**: Name of the constructor without sponsors.
* **nationality**: Nationality of the constructor.
* **url**: Wikipedia link.

## drivers.csv

* **driverId**: Unique integer identifier of the driver.
* **driverRef**: Unique string identifier of the driver.
* **number**: Number chosen by the driver that is used for identification purposes.
* **code**: Identification code for the driver displayed during event broadcasts.
* **forename**: Forename of the driver.
* **surname**: Surname of the driver.
* **dob**: Date of birth of the driver.
* **nationality**: Nationality of the driver.
* **url**: Wikipedia link.

## races.csv

* **raceId**: Unique integer identifier of the race.
* **year**: Year of the race.
* **round**: Position of the race in the F1 calendar for a given year.
* **circuitId**: Unique integer identifier of the circuit that hosted the race.
* **name**: Name of the circuit without sponsors.
* **date**: Date of the race.
* **time**: Time of the race.
* **url**: Wikipedia link.

## results.csv
 
* **resultId**: Unique integer identifier of the race result for a driver.
* **raceId**: Unique integer identifier of the race for a particular result.
* **driverId**: Unique integer identifier of the driver.
* **constructorId**: Unique integer identifier of the constructor.
* **number**: N\A
* **grid**: Starting grid position of a driver.
* **position**: Position achieved (number) by a driver during the race.
* **positionText**: Position achieved (string) by a driver during the race.
* **positionOrder**: Official final position achieved by a driver during the race (after filtering retirements or other position-affecting events).
* **points**: Points achieved by a driver during the race. 
* **laps**: Laps completed by the driver during the race.
* **time**: Total time taken to complete the race by a driver.
* **milliseconds**: Total time taken (in milliseconds) to complete the race by a driver.
* **fastestLap**: Lap number when the driver achieved personal fastest lap in the race.
* **rank**: N\A
* **fastestLapTime**: Time of fastest lap by the driver.
* **fastestLapSpeed**: Max. speed of fastest lap.
* **statusId**: N\A