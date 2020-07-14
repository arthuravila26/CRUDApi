# CRUDApi

This is a simple API that I did for train.
It uses Basic Methods as Post, Patch, Get and Delete.

# What is it?

This API is a person register. It gets the persons name, age, phone and address and register this datas on MongoDB.
You can also update someone, create, delete os get someone by the name.

# How does it works?

It's simples. 
I Just used docker-compose for get MongoDB up and register someone.
On running the program, it's possible register someone using the endpoint /new.
For get someone expecificly, use the route /{the name of the person} and the method GET it will return the person's informations.
If you want to see everybody that it's in the database, just use the route /people and the method GET it will return a bunch of people that is in the database.
Using /{the name of the person} and the method PATCH, you can update that person's informations.
Whether you want to delete someone by any reason, you must get that person id on data base, use ther route /{the id of the person you want delete} and the method DELETE. You will receive the information "The person has been deleted at {Date at the moment the person has been deleted}."

