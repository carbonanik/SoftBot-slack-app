pipeline {
    agent any
    stages {
        stage('verifying') {
            steps {
                sh 'docker version'
            }
        }
        stage('stop softbot') {
            steps {
                sh 'docker compose down'
            }
        }
        stage('copy secrets') {
            steps {
                sh 'cp /home/secret/softbot/.env .'
                sh 'cp /home/secret/softbot/service_account.json .'
            }
        }
        stage('list file') {
            steps {
                sh 'ls -a'
            }
        }
        stage('start softbot') {
            steps {
                sh 'docker compose up --build'
                sh 'docker compose ps'
            }
        }
    }
}