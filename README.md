# Introduction – Student Feedback App

As part of fulfilling the requirement of the CS7319 course we developed this application to show case Client/Server
architecture and the Layered architecture.

## Platform

### Selected Architecture

The application was developed using `python`  `version 3.10.0` programming language
and `Django framework` `version 4.2.7`.

### Downloading & Setup

1. Follow this link to download [python](https://www.python.org/downloads/).
2. Once downloaded, setup a virtual environment by running this command in the terminal `python -m venv env`,
   where `env` is the name of the environment.
3. Navigate to the folder where you created the virtual environment and run the following command.
   Windows: `env\Scripts\activate`
   Mac: `source env/bin/activate`

******NB:****** To deactivate a virtual environment navigate to the folder and run `deactivate`.

4. Once the virtual environment is activated. run the following command to install all
   dependencies. `pip install -r requirements.txt`
5. This command will spin up a local server and display the link log in the terminal. The default is `localhost:8000`

## Rationale

We chose to implement the Client/Server architecture style because this style is best suited for handling multiple
client connections. We felt this attribute would fit our requirement where multiple students (the clients) at SMU would
be using our applications at the same time.

Secondly, our choice was guided by the ease with which Client/Server can be scaled to match demand.

Thirdly, client/server architectural design is suited well for `django` since the framework uses `server side rendering`
for the `HTML` pages and all business logic is abstracted away from the client. This creates an opportunity to add more
features to our application, such as, performing analytics on review data to find the common qualms students have or
common praises for a lecturer, without being concerned about the processing power of clients.