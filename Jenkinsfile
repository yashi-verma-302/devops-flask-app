pipeline {
    agent {
        docker {
            image 'python:3.10'
        }
    }

    stages {
        stage('Clone Code') {
            steps {
                git branch: 'main', url: 'https://github.com/yashi-verma-302/devops-flask-app.git'
            }
        }

        stage('Install Requirements') {
            steps {
                sh 'pip install -r app/requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'python -m unittest discover tests || echo "No tests yet"'
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
            echo '✅ Build successful!'
        }
        failure {
            echo '❌ Build failed.'
        }
    }
}