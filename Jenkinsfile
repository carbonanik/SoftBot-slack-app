pipeline {
    agent any
    stages {
        // stage('verifing') {
        //     steps {
        //         sh '''
        //         docker version
        //         '''
        //     }
        // }
        stage('initializing') {
            steps {
                sh 'ls'
            }
        }
        stage('Test') {
            steps {
                // sh 'rm -r softbot-secret'
                sh 'git clone https://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@github.com/carbonanik/softbot-secret.git'
                sh 'cat softbot-secret/secret.env'
                sh 'cat softbot-secret/service_account.json'
            }
        }
        // stage('stop nginx') {
        //     steps {
        //         sh 'docker compose down'
        //     }
        // }
        // stage('start nginx') {
        //     steps {
        //         sh 'docker compose up --build'
        //         sh 'docker compose ps'
        //     }
        // }
    }
}