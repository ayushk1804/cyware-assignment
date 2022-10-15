# cyware-assignment
A repository for solving cyware assignment

## Question 1 
### Part 1
#### Getting Started:
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
    - ![pytest.png](https://github.com/ayushk1804/cyware-assignment/blob/main/Part%201/images/pytest.png)

- Docker-compose:
  - I have tested it by executing the project using docker-compose.
  - Screenshots of executing program
  - ![webapp.png](https://github.com/ayushk1804/cyware-assignment/blob/main/Part%201/images/webapp.png)
  - ![docker-compose.png](https://github.com/ayushk1804/cyware-assignment/blob/main/Part%201/images/docker-compose.png)

> Q. Is the stack ready to be used in production? (Give reasons for whatever your answer is)

No, the stack is not ready for use in production.
For production environment, we can cut down on our images and extract the useful parts to a slimmer image.
We can enable high availability by creating a fleet of containers and loadbalancing between them to ensure availability of our application.
We should also add a domain to the application for easier access, followed by adding a signed certificate for the used address.

### Part 2
Jenkins Groovy Script:
Triggering auto builds
We can add webhooks for triggering a Jenkinsbuild from our SCM. Lets assume that our SCM github then we can trigger Jenkins build API.
To do this, we will have to enable webhooks in our desired github repo, In the webhook settings page ‘Which events would you like to trigger this webhook?’ choose ‘Let me select individual events.’ Then, check ‘Pull Requests’ and ‘Pushes’. At the end of this option, make sure that the ‘Active’ option is checked and click on ‘Add webhook’.
In Jenkins, we add a build trigger (GitHub hook trigger for GITScm polling)

`Sample Jenkinsfile`
```groovy
pipeline {
    agent any
    stages {
        stage ('GIT Checkout'){
            steps {
                git changelog: false, poll: false, url: 'https://github.com/ayushk1804/cyware-assignment.git'
            }
        }
        
        stage('build') {
            steps {
                sh 'pip install -r Part 1/webapp/requirements.txt'
            }
        }
        
        stage ('Test'){
            steps {
                sh 'pytest Part 1/webapp/test_app.py'
            }
        }
    }
}
```