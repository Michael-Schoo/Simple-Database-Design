# Assessment Instrument 3 - Simple Database Design (Year 11 - Semester 2 - Web dev)

## Summary

As an avid collector of many things, you have identified the need to construct a web application that will allow you to easily manage, display, search and filter your collections. You believe that not only will this be a useful tool for you, but that a market exists for a tool that performs this task well across multiple devices and operating systems.

Knowing that managing collections could be a complex system, you have decided to use your newly developed skills in database design to implement a solution for managing your collection, in preparation for integrating it into a fully dynamic website built on a relational database platform using SQL.

The first step in your development process will be to design a normalised table/data structure that makes correct use of primary and foreign keys to maintain data integrity. You will represent this design using an ER diagram, and clearly identify/label the data types and relationships that will be used in the model.

From there, you will then write the SQL statements that will be required to fulfil the core functional requirements of your system. This will require populating the database with test data (best achieved with a script), and executing a series of tests to ensure the system behaves as expected.

For the purposes of this task you do NOT need to integrate the database into a website at this stage - integration of the database will occur once you have confirmed the correctness and functionality of your design.
You can build this tool for any collection you own. Examples might include books, CDs, DVDs, stamps, Magic: The Gathering cards, Pokémon – anything really, as long as each item of a collection should have properties that could be filtered or sorted by (for our examples above, these may include the genre for books, type for Pokémon, colour for Magic, or the country of origin for stamps. There should be at least 3 or 4 properties (including the name) that can be used as a filter).

## Part 1: Database Design

Your project will require the use of a simple relational database, built on top of an SQL-based platform. Your first task is to design a database that will allow you to easily store the collection and all associated information about the collection. To begin, you will need to think about what kind of relationships exist in the system and how best to model these in an Entity-Relationship (or ER) diagram.

**You will also want to consider how you might store information about users and any custom collections they might create - this will be beneficial next year when we continue this project. Remember that although the complete collection is listed, individual users may have their own collections that contain other sets of items.**

You will then need to come up with appropriate table and field names that will describe the data being stored in your database. You will also need to think about appropriate data types for each of your fields, and identify any keys that might be necessary to uniquely identify records in the database or to establish relationships between records.
For each of the tables in your design, you must provide a written explanation of your choice of structure and an example of how the data will be stored and accessed by referring to your example data. Your choice must be well articulated and justification for your design decisions well presented.

## Part 2: Query Identification and Development

Once your design has been completed, you will then need to write out the appropriate SQL statements to set up the tables and relationships in your database. It is also a good idea to populate it with some test data that you can use during the implementation of your website next year to check that you are storing and retrieving the data correctly.

As a minimum, you will need to identify the correct SQL statements necessary to do all of the following:

* Creating all necessary database tables;
* Selecting all items from the collection according to a variety of different criteria
  * Consider some of the filtering options you implemented for Assignment 1 - they will be a good indication of the kinds of restrictions you might use in your select queries;
* Adding new records to the database, thinking carefully about the process for adding records that may require entries in multiple tables;
* Updating existing records in the database, again thinking carefully about how you use the keys in each table to update only the target records; and
* Deleting entries from the database, the integrity of the data in your collections.

You do not need to integrate these into your existing site code - it will be enough for this assignment to demonstrate a working database file and example queries, much like you will have done in the SQL topic for classwork.
