# party-diary

This is a capsule submission for the SRPOL Bixby Hackathon.

The capsule is called "Party Diary" and it is used to register ones alcohol intake during a night out.

It allows users to register their bodyweight and the drinks they have. Using this data the system can estimate their Blood Alcohol Content and give this information back to the user. Additionally the user can define and register his level of hangover on the next day.

The capsule uses Bixby for natural language processing and an external RESTful web api written in Python for calculations and memory.

It uses the viv.measurement library capsule to handle the different weight units that can be used to represent the user's bodyweight.

This repo contains both the capsule, the web api and two user stories used for end-to-end testing of the capsule.

The NLP part of the system is mostly feature-complete. Perhaps an additional parameter for the volume of consumed beverages could be implemented and a more complex transactional model could be used in addition to the simple single-utterance commit that is currently available.

The server side part of the system is very rudimentary and should be completely overhauled in case of any comercial system. It was designed with the limitations of the free version of the hosting service pythonanywhere.com in mind.
