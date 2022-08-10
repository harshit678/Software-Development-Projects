# Tests for `SENG 265`, Assignment #1

* Test 1
    * Input: `one.ics`
    * Expected output: `test01.txt`
    * Command: `./event_manager --start=2022/1/22 --end=2022/1/23 --file=one.ics`
    * Test: `./event_manager --start=2022/1/22 --end=2022/1/23 --file=one.ics | diff test01.txt -`

* Test 2
    * Input: `one.ics`
    * Expected output: `test02.txt`
    * Command: `./event_manager --start=2022/2/14 --end=2022/2/14 --file=one.ics`
    * Test: `./event_manager --start=2022/2/14 --end=2022/2/14 --file=one.ics | diff test02.txt -`

* Test 3
    * Input: `one.ics`
    * Expected output: `test03.txt`
    * Command: `./event_manager --start=2022/2/10 --end=2022/2/16 --file=one.ics`
    * Test: `./event_manager --start=2022/2/10 --end=2022/2/16 --file=one.ics | diff test03.txt -`

* Test 4
    * Input: `two.ics`
    * Expected output: `test04.txt`
    * Command: `./event_manager --start=2022/4/18 --end=2022/4/21 --file=two.ics`
    * Test: `./event_manager --start=2022/4/18 --end=2022/4/21 --file=two.ics | diff test04.txt -`

* Test 5
    * Input: `two.ics`
    * Expected output: `test05.txt`
    * Command: `./event_manager --start=2022/4/20 --end=2022/4/30 --file=two.ics`
    * Test: `./event_manager --start=2022/4/20 --end=2022/4/30 --file=two.ics | diff test05.txt -`

* Test 6
    * Input: `three.ics`
    * Expected output: `test06.txt`
    * Command: `./event_manager --start=2022/5/1 --end=2022/5/20 --file=three.ics`
    * Test: `./event_manager --start=2022/5/1 --end=2022/5/20 --file=three.ics | diff test06.txt -`

* Test 7
    * Input: `many.ics`
    * Expected output: `test07.txt`
    * Command: `./event_manager --start=2022/5/28 --end=2022/7/7 --file=many.ics`
    * Test: `./event_manager --start=2022/5/28 --end=2022/7/7 --file=many.ics | diff test07.txt -`

* Test 8
    * Input: `diana-devops.ics`
    * Expected output: `test08.txt`
    * Command: `./event_manager --start=2022/1/1 --end=2022/12/31 --file=diana-devops.ics`
    * Test: `./event_manager --start=2022/1/1 --end=2022/12/31 --file=diana-devops.ics | diff test08.txt -`
