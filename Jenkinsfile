pipeline {
    agent any
    stages {
        stage('Example') {
            steps {
		checkout scm: [$class: 'GitSCM', source: 'git@github.com:SeaBa55/automation_devops_backend.git', clean: true, credentialsId: 'ass_test'], poll: false	
                echo 'Hello World'
            }
        }
    }
    post { 
        always { 
            echo 'I will always say Hello again!'
        }
    }
}
