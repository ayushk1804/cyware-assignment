# cyware-assignment
A repository for solving cyware assignment

## Part 1
Steps:
- Executing using Dockerfile:
  - Navigate to Part 1 dir, containing Dockerfile
  - Build image: `$ docker build -f Dockerfile -t app_runner .`
  - Run image: `$ docker run --rm app_runner`
- Executing using Docker-compose:
  -  Navigate to Part 1 dir, containing docker-compose.yml
  - Build: `$ docker-compose build`
  - Run: `$ docker-compose up`

> Q. Describe how you tested and provide output
Testing the project:
- Code:
  - I have added unittests for testing the code. The unittests can be triggered by installing the requirements for project then executing `pytest test_app.py`.
  - There are 2 unittests configured:
    - Health check: This test ensures that the health check api is giving status code 200. It will fail if respose status_code!=200
    - View Assertion: This test ensures that our output is as expected. In my code, I have asserted it to the respose text, which should be `Hi Team!`.
    - Screenshots of executed pytests
    - ![webapp.png](https://github.com/ayushk1804/cyware-assignment/blob/main/Part%201/images/webapp.png)
- Docker-compose:
  - I have tested it by executing the project using docker-compose.
  - Screenshots of executing program
  - ![docker-compose.png](https://github.com/ayushk1804/cyware-assignment/blob/main/Part%201/images/docker-compose.png)

> Q. Is the stack ready to be used in production? (Give reasons for whatever your answer is)
No, the stack is not ready for use in production.
For production environment, we can cut down on our images and extract the useful parts to a slimmer image.
We can enable high availability by creating a fleet of containers and loadbalancing between them to ensure availability of our application.
We should also add a domain to the application for easier access, followed by adding a signed certificate for the used address.
