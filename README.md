# Transform files

## Purpose

You must implement a conversion system from CSV OR JSON format to JSON.

***DISCLAIMER***
I received the link to the task in the previous format, but saw today that it changed to become simpler.
I read it yesterday and started coding today in late afternoon (july 15th). Yesterday I undertood I could receive either Json or CSV files and was supposed to output to both/either. 
So, I did a reader for both files. But then I updated the page/ferpection task and no jsons were required anymore for reading and no CSV for writing. 
As I already did csv and json reading I left it there. 
As I was to do the writing part, it just outputs to Json.
*****


You must implement a conversion system from CSV OR JSON format to JSON. 


## Task

You must write a program that takes csv files (or a mix of CSV and Json files) as input and transform it to structured JSON. 

Given the following two sample files: ``items.csv`` and ``groups.csv`` where records in the data file are linked to the groups through the group_id you must generate a structured JSON file.

The resulting JSON It should have the following structure where UPPERCASE refers to the header line in the csv.

```python
{
   “UUID_title”:{
      "string”:”TITLE”
   },

   “UUID_description”:{
      "string”:”DESCRIPTION”,
      "context”:”GROUP”
   }
 }
 ```

Example:

```python
{
   “f19c962e-eec0-455f-baa9-c0ba6986d01b_title”:{
      "string”: ”autem deserunt quo quaerat deleniti”
   },
   “f19c962e-eec0-455f-baa9-c0ba6986d01b_description”:{
      "string”: ”aut soluta repudiandae numquam accusantium pariatur culpa fugiat ducimus laudantium consequatur quam rerum dolorem beatae cum eius magni in architecto nihil similique odit été distinctio eligendi alias optio asperiores incidunt unde quaerat dolor a animi sapiente vel saepe ad iusto doloribus libero voluptates voluptate explicabo velit officiis praesentium accusamus possimus”,
      "context”: ”nesciunt quidem iure”
   }
 }
```

When run as a CLI command it must accept a filename in csv format and transform it to JSON.

It will be run similar to the following example:

```# python3 main.py items.csv groups.csv -o output.json```

The CLI should also output a help when called with:

```# python3 main.py -h```


### Notes

The delimiter used is the comma with a pipe as the quoting character for the CSV.

Please note your program will be run using different input files to check the validity.

More info on structured JSON https://docs.transifex.com/formats/json/structured-json

This exercise should not take you more than 3 hours. Please reach out if you have difficulty so we can discuss next steps. Do not spend days trying to craft a solution to impress, this is not the goal.
