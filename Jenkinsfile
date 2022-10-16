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
        stage('start nginx') {
            steps {
                sh 'docker compose up -d --build'
                sh 'docker compose ps'
            }
        }
    }
}