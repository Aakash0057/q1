pipeline {
    agent any
    environment {
        PATH = "C:\\Users\\MADHAN\\AppData\\Local\\Programs\\Python\\Python312;${env.PATH}"
    }
    stages {
        stage('Checkout Code') {
            steps {
                checkout scm
            }
        }
        stage('Build') {
            steps {
                echo 'Executing Python Sum Program...'
                bat 'python sum.py 10 20'
            }
        }
    }
}
