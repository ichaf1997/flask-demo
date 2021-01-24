pipeline {
    agent any // 代理通常是一个机器或者容器,表示在哪里运行Pipeline
    stages {
        stage("build") {
            steps {
                echo 'build....'
            }
        }
        stage("test") {
            steps {
                bat 'python test_main.py' // Windows下执行bat
                                          // Unix下执行sh
            }
        }
        stage("deploy") {
            steps {
                echo 'deploy...'
            }
        }
        stage("RetryAndTimeOut") {
            steps {
                retry(3) {                
                    echo 'Test Retry...'
                }
                timeout(time: 3, unit: 'MINUTES') {
                    echo 'Test TimeOut'
                }
            }
        }
    }
}
