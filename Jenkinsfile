pipeline {
    agent any

    stages {
        stage('Build Docker Image') {
            steps {
                script {
                    // Ensure Docker is available in the PATH
                    withEnv(['PATH+EXTRA=/usr/bin/docker']) {
                        dockerImage = docker.build("flaskapp")
                    }
                }
            }
        }

        stage('Run Docker Container') {
            steps {
                script {
                    withEnv(['PATH+EXTRA=/usr/local/bin']) {
                        // Stop and remove any previous container running on the same port
                        sh 'docker rm -f flaskapp || true'
                        // Run the new container
                        dockerImage.run("-d -p 5000:5000 --name flaskapp")
                    }
                }
            }
        }
    }
}
