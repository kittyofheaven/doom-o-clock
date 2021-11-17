# doom-o-clock
Doom o’clock is a website/project that features a countdown of “when will the earth end” and a greenhouse gas effect emission prediction that’s predicted not based on black magic wizardry, but predicted based on factual data from various sources, namely the Climatic Research Unit at the University of East Anglia, ESRL/NOAA Global Monitoring Division, Godard Institute for Space Studies at NASA, SOLARIS-HEPPA project website, and from the ESRL/NOAA Physical Sciences Division while using Artificial Intelligence and Machine Learning. As a bonus Doom 'o clock also shows non-profit organizations and projects that are trying their hardest to make climate change cease to exist, and how you can do so too. 
Make sure to check out the branch frontend to see our front end progression.

## Demo video
[![Watch the video](https://img.youtube.com/vi/grlAmeC-Rro/hqdefault.jpg)](https://www.youtube.com/watch?v=grlAmeC-Rro)

## Inspiration
I got the inspiration from a book "Will fart end the earth?" by Gleen Murphy, the book tells that in the future we must do a change so that the earth can stay healthy enough for human _~Hazel_

## What it does
The website is connected to the backend api that we built and predicted based on factual data from various sources, namely the Climatic Research Unit at the University of East Anglia, ESRL/NOAA Global Monitoring Division, Godard Institute for Space Studies at NASA, SOLARIS-HEPPA project website, and from the ESRL/NOAA Physical Sciences Division while using Artificial Intelligence and Machine Learning

## How we built it
First the backend team (Hazel & Arnav) will make a machine learning model with tensorflow, then created a rest api with flask and deploy it to heroku, at the same time. The frontend team (Vio & Theo) is designing and building the web landing page. Lastly we connect the frontend into backend api that running on heroku

## Challenges we ran into
- Deploying api to heroku **(Solved)**
- The api can process frontend input **(Solved)**

## Accomplishments that we're proud of
- How we can build such a good webpage
- The design is cool
- The frontend is so responsive

## What we learned
- How to work in team
- How to build an api
- How to connect to the api
- Never give up on solving bug

## What's next for Doom o'clock
We hope that after we make this website, our webpage visitors will more aware of climate change and try to prevent it

## Team
- [Arnav Pandey](https://github.com/splitxorpio) [Devpost](https://devpost.com/Split) (Backend programmer)
- [Hazel Handrata](https://github.com/kittyofheaven) [Devpost](https://devpost.com/kittyofheaven) (Machine learning engineer & Rest api programmer) 
- [Marvin Savio](https://github.com/marvinsavio) [Devpost](https://devpost.com/marvinzahir20) (Web designer & Demo video creator) 
- [Theo Halpern](https://github.com/dumax315) [Devpost](https://devpost.com/dumax315) (Responsive frontend programmer) 

## Achievments
- Winning infinihacks hackathon as The best environment [project](https://devpost.com/software/doom-o-clock) 

## API reference
https://doom-clock-api.herokuapp.com/atmosphere
please include our license to your app if you want to use our api

- GET : 
 
return JSON 
```
{"doom_month": int, "doom_year": int}
```
- POST :

POST JSON 
```
{Year : int , Month : int}
```
return JSON
```
{"Aerosols": "str", "CFC-11": "str", "CFC-12": "str", "CH4": "str", "CO2": "str", "N2O": "str", "TSI": "str", "Temp": "str"}
```
