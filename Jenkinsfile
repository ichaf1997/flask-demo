pipeline {
    /* 
    执行环境: 代理通常是一个机器或者容器,表示在哪里运行Pipeline
    any: 在任何可用的代理上执行流水线或阶段
    none: 不指定代理,由每个stage自行指定
    还有很多可选参数如label、node、docker等
    References: https://www.jenkins.io/zh/doc/book/pipeline/syntax/ 
    */
    agent any 

    // 环境变量: 作用域有Pipeline和stage两种
    environment {
        DISABLE_AUTH = 'true'
        DB_ENGINE = 'sqlite'
    } 
    
    // 执行步骤: 一般分为构建、测试、部署
    stages {
        stage("build") {
            steps {
                echo 'build....'
            }
        }
        stage("test") {
            steps {
                /* 
                   Windows下执行bat
                   Unix下执行sh 
                */
                bat 'python test_main.py'                                           
            }
        }
        stage("deploy") {
            steps {
                echo 'deploy...'
            }
        }
        stage("RetryAndTimeOut") {
            steps {
                // 失败最大重试执行次数
                retry(3) {                   
                    echo 'Test Retry...'
                }
                // 执行时间限制,常见单位由SECONDS、MINUTES、HOURS
                timeout(time: 3, unit: 'MINUTES') {  
                    echo 'Test TimeOut'
                }
            }
        }
    }

    // 完成时动作
    post {
        always {
            echo 'This will always run'
            // deleteDir() 总是清理workspace
        }
        success {
            echo 'This will run only if successful'
        }
        failure {
            echo 'This will run only if failed'
            // 失败邮件通知
            /*
            mail to: 'team@example.com',
                subject: "Pipeline执行失败: ${currentBuild.fullDisplayName}",
                body: "执行Pipeline时发生了一些异常 ${env.BUILD_URL}"
             */
        }
        unstable {
            echo 'This will run only if the run was marked as unstable'
        }
        changed {
            echo 'This will run only if the state of the Pipeline has changed'
            echo 'for example, if the Pipeline was previously failing but is now successful'
        }
    }
}
