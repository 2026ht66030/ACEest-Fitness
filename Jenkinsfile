pipeline {
    agent any
    
    stages {
        // --- YOUR EXISTING STAGES (e.g., Checkout, Test) ---
        stage('Checkout Code') {
            steps {
                // Keep your existing checkout mechanism here
                checkout scm 
            }
        }
        
        stage('Run Unit Tests') {
            steps {
                // Keep your existing test execution command here
                sh 'pytest -v'
            }
        }
        
        // --- NEW: DOCKER IMAGE GENERATION STAGE ---
        stage('Build Docker Image') {
            steps {
                script {
                    // Automatically extracts your Git tag (e.g., v1.0, v1.1, v3.1.2)
                    def versionTag = sh(script: "git describe --tags --always", returnStdout: true).trim()
                    
                    // Build the Docker image with the specific version tag
                    sh "docker build -t aceest-fitness:${versionTag} ."
                    
                    // Optional: Also tag it as latest
                    sh "docker tag aceest-fitness:${versionTag} aceest-fitness:latest"
                }
            }
        }
    }
}