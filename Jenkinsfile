pipeline {
    agent any
    stages {
        stage("构建") {
            steps {
                echo '构建中....'
            }
        }
        stage("单元测试") {
            steps {
                sh 'python test_main.py'
            }
        }
        stage("部署") {
            steps {
                echo '部署中...'
            }
        }
    }
}
