# common-columns
A tool to identify the common columns in a 2D array, sometimes simplifying a data set for viewing.

## Examples

```csv
Name,Age,Sex,City,State,Country
Jim,42,M,Baraboo,WI,USA
Bob,77,M,Madison,WI,USA
Susan,59,F,Baraboo,WI,USA
Alan,61,M,Baraboo,WI,USA
Chris,17,F,Madison,WI,USA
```
      
```md
common-columns foo.csv --sort-columns --pretty --reverse-locf

COLUMN  | COMMON_VALUE
======= | ============
State   | WI
Country | USA

City    | Sex | Name  | Age
======= | === | ===== | ===
Baraboo |   M | Jim   |  42
        |     | Alan  |  61
        |   F | Susan |  59
Madison |   M | Bob   |  77
        |   F | Chris |  17
```
