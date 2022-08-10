# Tests for `SENG 265`, Assignment #2

## Tests

* Test 1
    * Inputs: `drivers.csv, results.csv`
    * Expected output: `test01.csv`
    * Command: `./f1_statistics.py --question=1 --files=drivers.csv,results.csv`
    * Test: `./tester.py test01.csv`

* Test 2
    * Input: `drivers.csv, results.csv`
    * Expected output: `test02.csv`
    * Command: `./f1_statistics.py --question=2 --files=drivers.csv,results.csv`
    * Test: `./tester.py test02.csv`

* Test 3
    * Input: `constructors.csv, results.csv`
    * Expected output: `test03.csv`
    * Command: `./f1_statistics.py --question=3 --files=constructors.csv,results.csv`
    * Test: `./tester.py test03.csv`

* Test 4
    * Input: `circuits.csv, races.csv`
    * Expected output: `test04.csv`
    * Command: `./f1_statistics.py --question=4 --files=circuits.csv,races.csv`
    * Test: `./tester.py test04.csv`

* Test 5
    * Input: `drivers.csv, results.csv`
    * Expected output: `test05.csv`
    * Command: `./f1_statistics.py --question=5 --files=drivers.csv,results.csv`
    * Test: `./tester.py test05.csv`

## Library installation for tester.py

To be able to execute tester.py, you'll need to execute the following command in your environment:

pip3 install csv-diff