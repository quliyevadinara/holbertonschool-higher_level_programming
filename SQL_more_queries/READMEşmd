# SQL - More Queries

## Description

This project covers advanced SQL concepts including user privileges, table constraints, and complex queries using JOINs and subqueries. All scripts are written for MySQL and follow the Holberton School curriculum.

## Learning Objectives

- How to create new MySQL users
- How to manage privileges for a user to a database or table
- What is a `PRIMARY KEY`
- What is a `FOREIGN KEY`
- How to use `NOT NULL` and `UNIQUE` constraints
- How to retrieve data from multiple tables using `JOIN` and subqueries
- What are the different types of JOINs (`INNER`, `LEFT`, `RIGHT`, `FULL OUTER`)
- What is DCL (Data Control Language)

## Requirements

- Ubuntu 20.04 LTS
- MySQL 8.0 (version 8.0.25)
- All SQL keywords must be in uppercase
- All files must end with a new line
- All SQL queries must have a comment just before them
- The first line of every file must be a comment describing the task

## Files

| File                                  | Description                                                        |
| ------------------------------------- | ------------------------------------------------------------------ |
| `0-privileges.sql`                    | Lists all privileges of users `user_0d_1` and `user_0d_2`          |
| `1-create_user.sql`                   | Creates user `user_0d_1` with all privileges                       |
| `2-create_read_user.sql`              | Creates database `hbtn_0d_2` and user `user_0d_2` with SELECT only |
| `3-force_name.sql`                    | Creates table `force_name` with a NOT NULL name column             |
| `4-never_empty.sql`                   | Creates table `id_not_null` with id defaulting to 1                |
| `5-unique_id.sql`                     | Creates table `unique_id` with a UNIQUE id defaulting to 1         |
| `6-states.sql`                        | Creates database `hbtn_0d_usa` and table `states`                  |
| `7-cities.sql`                        | Creates table `cities` with a FOREIGN KEY referencing `states`     |
| `8-cities_of_california_subquery.sql` | Lists all cities of California using a subquery                    |
| `9-cities_by_state_join.sql`          | Lists all cities with their state name using JOIN                  |
| `10-genre_id_by_show.sql`             | Lists shows that have at least one genre linked                    |
| `11-genre_id_all_shows.sql`           | Lists all shows with genre id, NULL if none                        |
| `12-no_genre.sql`                     | Lists all shows without any genre linked                           |
| `13-count_shows_by_genre.sql`         | Lists genres and the number of shows linked to each                |
| `14-my_genres.sql`                    | Lists all genres of the show Dexter                                |
| `15-comedy_only.sql`                  | Lists all Comedy shows                                             |
| `16-shows_by_genre.sql`               | Lists all shows and their linked genres                            |

## Usage

Run any script against your MySQL server like this:

```bash
# For scripts that don't require a database argument
cat 0-privileges.sql | mysql -hlocalhost -uroot -p

# For scripts that require a database argument
cat 3-force_name.sql | mysql -hlocalhost -uroot -p hbtn_0d_2
```

## Concepts Covered

### DCL — Data Control Language

SQL commands used to control access to data: `GRANT` and `REVOKE`.

### Constraints

- `NOT NULL` — ensures a column cannot have a NULL value
- `UNIQUE` — ensures all values in a column are different
- `DEFAULT` — sets a default value for a column
- `PRIMARY KEY` — uniquely identifies each row in a table
- `FOREIGN KEY` — links two tables together, enforcing referential integrity

### JOIN Types

- `INNER JOIN` — returns rows with matching values in both tables
- `LEFT JOIN` — returns all rows from the left table, with matched rows from the right (NULL if no match)
- `RIGHT JOIN` — returns all rows from the right table, with matched rows from the left (NULL if no match)
- `FULL OUTER JOIN` — returns all rows when there is a match in either table

### Subqueries

A query nested inside another query, used to filter results dynamically without using JOIN.

## Author

Holberton School — Higher Level Programming
