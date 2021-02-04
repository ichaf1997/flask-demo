pipeline{
    agent {
        node {
            label 'docker-node'
        }
    }
    environment {
        docker_repo = '192.168.2.212:8443'
        build_image_name = 'flask-demo'
        deploy_namespace = 'development'
        kubernetes_config = credentials('kubernetes_api_config')
        harbor_authentication = credentials('harbor')
    }
    stages{
        stage("unittest"){
            steps{
                echo "========Execute Test========"
                sh "docker login -u $harbor_authentication_USR -p $harbor_authentication_PSW $docker_repo"
                sh "docker run --rm -v $WORKSPACE:/app $docker_repo/library/python:rc-alpine3.12-withflask python /app/test_main.py" 
            }
            post{
                always{
                    echo "========Test completed========"
                }
                success{
                    echo "========Test executed successfully========"
                }
                failure{
                    echo "========Test execution failed========"
                }
            }
        }
        stage("build"){
            steps{
                echo "====++++build image++++===="
                sh "docker build -t $docker_repo/library/$build_image_name:$BRANCH_NAME-$BUILD_ID ."
            }
            post{
                always{
                    echo "====++++build completed++++===="
                }
                success{
                    echo "====++++build executed successfully++++===="
                }
                failure{
                    echo "====++++build execution failed++++===="
                }
            }
        }
        stage("release"){
            steps{
                echo "====++++executing release++++===="
                sh "docker login -u $harbor_authentication_USR -p $harbor_authentication_PSW $docker_repo"
                sh "docker push $docker_repo/library/$build_image_name:$BRANCH_NAME-$BUILD_ID"
            }
            post{
                always{
                    echo "====++++release completed++++===="
                }
                success{
                    echo "====++++release executed successfully++++===="
                }
                failure{
                    echo "====++++release execution failed++++===="
                }       
            }
        }
        stage("deploy"){
            environment{
                deploy_image = "$docker_repo/library/$build_image_name:$BRANCH_NAME-$BUILD_ID"
            }
            input{
                message 'deploy in Kubernetes Cluster, Continue ?'
                ok 'Yes, continue.'
            }
            steps{
                echo "====++++executing deploy++++===="
                sh 'sed -i "s#APP_IMAGE#$deploy_image#g" deployment/*.yaml'
                // sh "kubectl apply -k deployment/ -n $deploy_namespace"
                sh "chmod a+r $kubernetes_config"
                sh "docker run --rm --name kubectl -v $WORKSPACE/deployment:/resources -v $kubernetes_config:/tmp/config 192.168.2.212:8443/library/kubectl:1.19.3 apply -k /resources -n $deploy_namespace --kubeconfig /tmp/config"
            }
            post{
                always{
                    echo "====++++always++++===="
                }
                success{
                    echo "====++++deploy executed successfully++++===="
                }
                failure{
                    echo "====++++deploy execution failed++++===="
                }        
            }
        }
    }
}


