pipeline {
    agent any
    environment {
        PATH = "C:\\Users\\MADHAN\\AppData\\Local\\Programs\\Python\\Python312;${env.PATH}"
    }
    stages {
        stage('Checkout Code') {
            steps {
                git branch: 'main', url: 'https://github.com/Aakash0057/Q1_Python_Sum.git'
            }
        }
        stage('Build') {
            steps {
                echo 'Executing Python Sum Program via Clean Environment Variables...'
                bat 'python sum.py'
            }
        }
    }
}
