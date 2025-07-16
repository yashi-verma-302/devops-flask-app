pipeline {
    agent any

    stages {
        stage('Clone Code') {
            steps {
                git branch: 'main', url: 'https://github.com/yashi-verma-302/devops-flask-app.git'
            }
        }

        stage('Install Python') {
            steps {
                sh '''
                    which python3 || apt-get update && apt-get install -y python3 python3-pip
                    python3 --version
                    pip3 --version
                '''
            }
        }

        stage('Install Requirements') {
            steps {
                sh 'pip3 install -r app/requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'python3 -m unittest discover tests || echo "No tests yet"'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t flask-app .'
            }
        }
    }

    post {
        success {
            echo 'Build successful!'
        }
        failure {
            echo 'Build failed.'
        }
    }
}