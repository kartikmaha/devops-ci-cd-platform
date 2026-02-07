pipeline{
    agent { label 'cicd' }
    
    stages{
        stage("Code Clone"){
            steps{
                echo "Code Clone Stage"
                git url: "https://github.com/kartikmaha/devops-ci-cd-platform.git", branch: "master"
            }
        }
        stage("Code Build & Test"){
            steps{
                echo "Code Build Stage"
                sh "docker build -t devops-app app"
            }
        }
        stage("Push To DockerHub"){
            steps{
                withCredentials([usernamePassword(
                    credentialsId:"dockerHubCreds",
                    usernameVariable:"dockerHubUser", 
                    passwordVariable:"dockerHubPass")]){
                sh 'echo $dockerHubPass | docker login -u $dockerHubUser --password-stdin'
                sh "docker image tag devops-app:latest ${env.dockerHubUser}/devops-app:latest"
                sh "docker push ${env.dockerHubUser}/devops-app:latest"
                }
            }
        }
        stage("Deploy") {
            steps {
                    withCredentials([sshUserPrivateKey(credentialsId: 'my-app-key', 
                                                       keyFileVariable: 'SSH_KEY',
                                                    usernameVariable: 'SSH_USER')]) {
                    sh """
                        export ANSIBLE_HOST_KEY_CHECKING=False
                        ansible-playbook -i ansible/inventory.ini ansible/deploy.yml \
                        --private-key=\$SSH_KEY \
                        --user "$SSH_USER"
                        """
                        }
                    }
                }
            }
        }
