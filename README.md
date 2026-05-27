# Cloud-Computing-Project-Baladi
Our cloud computing project at National Autonomous University of México. 
Baladi is an online game in which the player has to guess the name of the astronomical object shown on the NASA's Astronomy Picture Of the Day.
In order to guess the answer, the player has access to the picture and the description of the astronomical object they're looking at. The picture and description change daily, so there's a new game each day. 


This project seeks to implement the NASA's API called APOD and deploy it in a funny way using Django as the backend framework. Here are the general steps:

- NASA's APOD API provides a daily astronomical image along with its title and description.
- We process the data using Python to extract the "target word" from the image title, prioritizing known astronomical objects such as galaxy, nebula, aurora, and others.
- The description is presented to the player with the target word hidden, serving as the main clue to solve the puzzle.

## Members
- Bialy Calderon - bialycalderonm@gmail.com
- Christian Morales - chrisimg06@gmail.com
- Jesus Almaguer - correodefinitivo97@gmail.com
