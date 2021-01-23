pipeline {
    agent any
    stages {
        stage("build") {
            steps {
                echo '构建中....'
            }
        }
        stage("test") {
            steps {
                sh 'python test_main.py'
            }
        }
        stage("deploy") {
            steps {
                echo '部署中...'
            }
        }
    }
}
