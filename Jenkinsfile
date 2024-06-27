pipeline {
    agent any

    environment {
        registry = "your-docker-registry-url"
        registryCredential = 'docker-hub-credentials'
        dockerImage = ''
    }

    stages {
        stage('Build') {
            steps {
                script {
                    dockerImage = docker.build registry + ":$BUILD_NUMBER"
                }
            }
        }
        stage('Test') {
            steps {
                script {
                    dockerImage.inside {
                        sh 'echo "Running tests"'
                        // Add your test commands here
                    }
                }
            }
        }
        stage('Deploy to Dev') {
            steps {
                script {
                    dockerImage.inside {
                        sh 'docker run -d -p 8880:8080 dog-gif-app'
                    }
                }
            }
        }
        stage('Deploy to Staging') {
            steps {
                script {
                    dockerImage.inside {
                        sh 'docker run -d -p 8800:8080 dog-gif-app'
                    }
                }
            }
        }
        stage('Push to Registry') {
            steps {
                script {
                    docker.withRegistry( '', registryCredential ) {
                        dockerImage.push()
                    }
                }
            }
        }
    }
}

