pipeline {
    agent any
    environment {
        registry = "keidarb/project3_repo"
        registryCredential = 'docker_hub'
        dockerImage = ''
        }
    options {
        buildDiscarder(logRotator(numToKeepStr: '20', daysToKeepStr: '5' ))
    }
    stages {
        stage('Pull Code') {
            steps {
                script {
                    properties([pipelineTriggers([pollSCM('*/30 * * * *')])])
                }
                git 'https://github.com/keidar/Project4.git'
            }
        }
        stage('run rest app server ') {
            steps {
                script {
                    sh 'nohup python rest_app.py &'

                }
            }
        }

        stage('run backend testing') {
            steps {
                script {
                    sh 'python backend_testing.py'

                }
            }
        }
        stage('run clean environment ') {
            steps {
                script {
                    sh ' python clean_environment.py'

                }
            }
        }
        stage('build docker image ') {
            steps {
                script {
                    sh ' docker build -t project3 .'
                }
            }
        }
         stage('build and push image') {
            steps {
                script {
                    dockerImage = docker.build registry + ":$BUILD_NUMBER"
                    docker.withRegistry('', registryCredential) {
                    dockerImage.push()
                    }
                }
            }
        post{
        always{
            sh "docker rmi $registry:$BUILD_NUMBER"
        }
       }
      }

        stage('Set compose image version ') {
            steps {
                script {
                    sh ' echo IMAGE_TAG=${BUILD_NUMBER} > .env'
                }
            }
        }
        stage('run docker compose ') {
            steps {
                script {
                    sh ' docker-compose up -d '
                }
            }
        }
        stage('run docker backend testing') {
            steps {
                script {
                    sh ' python docker_backend_testing.py'
                }
            }
        }
         stage('run clean docker environment environment ') {
            steps {
                script {
                    sh 'docker rmi project3'
                    sh 'docker-compose down'
                }
            }
        }
         stage('Deploy Helm') {
            steps {
                script {
                    sh 'helm upgrade --install testing keidarb-0.0.1.tgz --set image.tag=${BUILD_NUMBER}'
                }
            }
        }
        stage('Write service to url') {
            steps {
                script {
                    sh 'minikube service testing-keidarb --url > k8s_url.txt'
                }
                sleep 30
            }
        }
        stage('write service to url') {
            steps {
                script {
                    sh 'python k8s_backend_testing.py'
                }
            }
        }
        stage('Delete Helm chart') {
            steps {
                script {
                    sh 'helm delete testing'
                }
            }
        }
    }
}
