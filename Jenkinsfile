//pipeline {
//    agent any
//    stages {
//        stage('Example') {
//            steps {
//		checkout scm: [$class: 'GitSCM', source: 'git@github.com:SeaBa55/automation_devops_backend.git', clean: true, credentialsId: 'ass_test'], poll: false	
//                echo 'Hello World'
//            }
//        }
//    }
//    post { 
//        always { 
//            echo 'I will always say Hello again!'
//        }
//    }
//}
//pipeline {
//    agent { docker { image 'python:3.5.1' } }
//    stages {
//        stage('build') {
//            steps {
//                sh 'python --version'
//            }
//        }
//    }
//}
node("myAgent") {
    timeout(unit: 'SECONDS', time: 5) {
        stage("One"){
            sleep 10
            echo 'hello'
        }
    }
}
