pipeline {
    agent any
    stages {
        stage('verifing') {
            steps {
                sh '''
                docker version
                '''
            }
        }
        stage('start nginx') {
            steps {
                sh 'docker compose down'
            }
        }
        stage('start nginx') {
            steps {
                sh 'docker compose up --build'
                sh 'docker compose ps'
            }
        }
    }
}