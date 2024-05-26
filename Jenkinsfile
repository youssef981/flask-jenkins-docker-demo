pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git url: 'https://github.com/youssef981/flask-jenkins-docker-demo.git', branch: 'master'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    dockerImage = docker.build("flaskapp")
                }
            }
        }

        stage('Run Docker Container') {
            steps {
                script {
                    // Stop and remove any previous container running on the same port
                    sh 'docker rm -f flaskapp || true'
                    // Run the new container
                    dockerImage.run("-d -p 5000:5000 --name flaskapp")
                }
            }
        }
    }
}
