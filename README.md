# WebSocket Chat App

Welcome to our WebSocket-based chat application! This application enables users to engage in real-time conversations using WebSocket technology. Users are required to log in to access the chat functionality.

## Installation

To run this application locally, follow these steps:

1. Clone this repository to your local machine.
2. Install the required dependencies by running:
    ```
    pip install -r requirements.txt
    ```
3. Run the Django development server:
    ```
    python manage.py runserver
    ```
4. Access the application through the provided URL.

## Usage

1. Register or log in to your account.
2. Enter the chat room by specifying the room name.
3. Start chatting with other users in real-time!

## Features

- **Real-time Communication**: Utilizes WebSocket technology for instant messaging between users.
- **User Authentication**: Users must log in to access the chat functionality, ensuring security and privacy.
- **Room-based Chatting**: Users can create or join different chat rooms based on their interests or topics.
- **Asynchronous Messaging**: Messages are sent and received asynchronously, providing a seamless chatting experience.


### Code Overview

The core functionality of the chat application is implemented in `consumers.py`. Here's a brief overview:

- **ChatConsumer**: Handles WebSocket connections, disconnections, and message exchanges between users.
- **get_user_from_jwt**: Asynchronously retrieves a user object from a JWT token for authentication.
