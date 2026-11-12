pipeline {
    agent any

    parameters {
        choice(name: 'ENVIRONMENT', choices: ['chemical_plant', 'boiler_room'], description: 'Select Industrial Environment')
    }

    stages {
        stage('Setup') {
            steps {
                bat 'py -m venv .venv'
                bat '.venv\\Scripts\\python -m pip install -r requirements.txt'
            }
        }
        stage('Run Parameterized Tests') {
            steps {
                bat ".venv\\Scripts\\python -m pytest -v -k ${params.ENVIRONMENT} --html=reports/report_${params.ENVIRONMENT}.html --self-contained-html"
            }
        }
    }

    post {
        always {
            publishHTML(target: [
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