pipeline {
    agent any
    stages {
        stage('Checkout Code') {
            steps {
                checkout scm
            }
        }
        stage('Build') {
            steps {
                echo 'Executing the Basic Python Application on Windows...'
                bat 'python app.py'
            }
        }
    }
}
