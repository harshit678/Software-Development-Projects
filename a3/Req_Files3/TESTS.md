# Tests for `SENG 265`, Assignment #3

* Test 1
    * Input: `top_songs_1999.csv`
    * Expected output: `test01.csv`
    * Command: `./song_analyzer --sortBy=popularity --display=10 --files=top_songs_1999.csv`
    * Test: `./tester.py test01.csv`

* Test 2
    * Input: `top_songs_1999.csv`
    * Expected output: `test02.csv`
    * Command: `./song_analyzer --sortBy=energy --display=5 --files=top_songs_1999.csv`
    * Test: `./tester.py test02.csv`

* Test 3
    * Input: `top_songs_1999.csv`
    * Expected output: `test03.csv`
    * Command: `./song_analyzer --sortBy=danceability --display=3 --files=top_songs_1999.csv`
    * Test: `./tester.py test03.csv`

* Test 4
    * Input: `top_songs_2009.csv`
    * Expected output: `test04.csv`
    * Command: `./song_analyzer --sortBy=popularity --display=3 --files=top_songs_2009.csv`
    * Test: `./tester.py test04.csv`

* Test 5
    * Input: `top_songs_2019.csv`
    * Expected output: `test05.csv`
    * Command: `./song_analyzer --sortBy=danceability --display=5 --files=top_songs_2019.csv`
    * Test: `./tester.py test05.csv`

* Test 6
    * Input: `top_songs_1999.csv,top_songs_2009.csv`
    * Expected output: `test06.csv`
    * Command: `./song_analyzer --sortBy=energy --display=5 --files=top_songs_1999.csv,top_songs_2009.csv`
    * Test: `./tester.py test06.csv`

* Test 7
    * Input: `top_songs_1999.csv,top_songs_2009.csv,top_songs_2019.csv`
    * Expected output: `test07.csv`
    * Command: `./song_analyzer --sortBy=popularity --display=10 --files=top_songs_1999.csv,top_songs_2009.csv,top_songs_2019.csv`
    * Test: `./tester.py test07.csv`


## Library installation for tester.py

To be able to execute tester.py, you'll need to execute the following command in your environment:

pip3 install csv-diff