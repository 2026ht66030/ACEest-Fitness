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

        stage('build') {
            steps {
                echo 'installing python dependencies'
                sh ''' 

                    python3 -m venv .venv 

                    .venv/bin/pip install -r requirements.txt 

                ''' 
            }
        }


        
        stage('Run Unit Tests') {
            steps {
                echo 'Running python test'
                sh 'xvfb-run pytest'
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