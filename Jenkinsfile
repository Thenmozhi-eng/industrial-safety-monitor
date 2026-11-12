pipeline {
    agent any

    parameters {
        choice(name: 'ENVIRONMENT', choices: ['chemical_plant', 'boiler_room'], description: 'Select Industrial Environment')
    }

    stages {
        stage('Run Parameterized Tests') {
            steps {
                // Environment parameter-a pass panni test run panrathu
                bat ".venv\\Scripts\\pytest -v --html=reports/report_${params.ENVIRONMENT}.html --self-contained-html"
            }
        }
    }
    
    post {
        always {
            publishHTML([
                allowMissing: false,
                alwaysLinkToLastBuild: true,
                keepAll: true,
                reportDir: 'reports',
                reportFiles: "report_${params.ENVIRONMENT}.html",
                reportName: "Safety Report - ${params.ENVIRONMENT}",
                reportTitles: "Report for ${params.ENVIRONMENT}"
            ])
        }
    }
}